import fs from 'fs';
import path from 'path';

const repoRoot = process.cwd();
const bibPath = path.join(repoRoot, 'paper', 'references.bib');
const papersPath = path.join(repoRoot, 'PAPERS.md');
const sectionsDir = path.join(repoRoot, 'paper', 'sections');

const fieldDefs = [
  {
    id: 'foundations-methods',
    title: 'Foundations & Agentic Methods',
    chapters: '1-3, 11-12',
    focus: 'Definitions, agentic operating loops, training, adaptation, self-improvement, and evaluation.',
    badge: '0f766e',
    sectionFiles: ['01_introduction.tex', '02_foundations.tex', '03_operating_loop.tex', '11_training.tex', '12_evaluation.tex'],
  },
  {
    id: 'image-generation',
    title: 'Image Generation & Editing',
    chapters: '4',
    focus: 'Text-to-image, image editing, controllable synthesis, restoration, and image-centric agents.',
    badge: 'e11d48',
    sectionFiles: ['04_image_generation.tex', '04_modalities.tex'],
  },
  {
    id: 'video-animation',
    title: 'Video & Animation',
    chapters: '5',
    focus: 'Text-to-video, animation, motion, temporal consistency, storytelling, and video editing.',
    badge: '7c3aed',
    sectionFiles: ['05_video_animation.tex'],
  },
  {
    id: 'three-d-cad-world',
    title: '3D / CAD / World',
    chapters: '6',
    focus: '3D assets, CAD, scene construction, world models, physics, and embodied visual generation.',
    badge: '0284c7',
    sectionFiles: ['06_3d_cad_world.tex'],
  },
  {
    id: 'scientific-visualization',
    title: 'Scientific Visualization',
    chapters: '7',
    focus: 'Charts, visual analytics, scientific figures, data-to-visualization systems, and visual aids.',
    badge: '0891b2',
    sectionFiles: ['07_scientific_visualization.tex'],
  },
  {
    id: 'structured-documents',
    title: 'Structured Documents & Diagrams',
    chapters: '8',
    focus: 'Presentations, documents, diagrams, layouts, storybooks, and structured visual artifacts.',
    badge: 'b45309',
    sectionFiles: ['08_structured_documents.tex'],
  },
  {
    id: 'ui-web',
    title: 'UI / Web Creation',
    chapters: '9',
    focus: 'Interfaces, browser agents, website generation, design-to-code, and interactive UI workflows.',
    badge: 'be185d',
    sectionFiles: ['09_ui_web.tex'],
  },
  {
    id: 'cross-domain-applications',
    title: 'Cross-Domain Applications',
    chapters: '10',
    focus: 'Systems that transfer agentic visual-generation patterns across domains and applications.',
    badge: '475569',
    sectionFiles: ['10_cross_domain.tex'],
  },
];

const fieldPriority = fieldDefs.map((field) => field.id);

function readText(filePath) {
  return fs.readFileSync(filePath, 'utf8').replace(/\r\n/g, '\n');
}

function findMatchingBrace(text, start) {
  let depth = 0;
  let inQuote = false;
  let escaped = false;
  for (let i = start; i < text.length; i += 1) {
    const char = text[i];
    if (escaped) {
      escaped = false;
      continue;
    }
    if (char === '\\') {
      escaped = true;
      continue;
    }
    if (char === '"') {
      inQuote = !inQuote;
      continue;
    }
    if (inQuote) continue;
    if (char === '{') depth += 1;
    if (char === '}') {
      depth -= 1;
      if (depth === 0) return i;
    }
  }
  throw new Error(`Unclosed BibTeX entry at character ${start}`);
}

function findTopLevelComma(text) {
  let depth = 0;
  let inQuote = false;
  let escaped = false;
  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    if (escaped) {
      escaped = false;
      continue;
    }
    if (char === '\\') {
      escaped = true;
      continue;
    }
    if (char === '"') {
      inQuote = !inQuote;
      continue;
    }
    if (inQuote) continue;
    if (char === '{') depth += 1;
    if (char === '}') depth -= 1;
    if (char === ',' && depth === 0) return i;
  }
  return -1;
}

function readValue(text, start) {
  let i = start;
  while (/\s/.test(text[i] ?? '')) i += 1;
  if (text[i] === '{') {
    const end = findMatchingBrace(text, i);
    return { value: text.slice(i, end + 1), end: end + 1 };
  }
  if (text[i] === '"') {
    let escaped = false;
    for (let j = i + 1; j < text.length; j += 1) {
      if (escaped) {
        escaped = false;
        continue;
      }
      if (text[j] === '\\') {
        escaped = true;
        continue;
      }
      if (text[j] === '"') return { value: text.slice(i, j + 1), end: j + 1 };
    }
    throw new Error(`Unclosed quoted BibTeX value at character ${i}`);
  }

  let j = i;
  while (j < text.length && text[j] !== ',') j += 1;
  return { value: text.slice(i, j).trim(), end: j };
}

function parseFields(text) {
  const fields = {};
  let i = 0;
  while (i < text.length) {
    while (i < text.length && /[\s,]/.test(text[i])) i += 1;
    if (i >= text.length) break;
    const nameStart = i;
    while (i < text.length && /[A-Za-z]/.test(text[i])) i += 1;
    const name = text.slice(nameStart, i).toLowerCase();
    while (i < text.length && /\s/.test(text[i])) i += 1;
    if (text[i] !== '=') {
      while (i < text.length && text[i] !== ',') i += 1;
      continue;
    }
    i += 1;
    const parsed = readValue(text, i);
    fields[name] = parsed.value;
    i = parsed.end;
  }
  return fields;
}

function parseBibTeX(text) {
  const entries = [];
  const entryStart = /@(article|inproceedings|incollection|inbook|book|misc|phdthesis|mastersthesis|techreport|unpublished)\s*\{/gi;
  let match;
  while ((match = entryStart.exec(text)) !== null) {
    const openBrace = entryStart.lastIndex - 1;
    const closeBrace = findMatchingBrace(text, openBrace);
    const body = text.slice(openBrace + 1, closeBrace);
    const comma = findTopLevelComma(body);
    if (comma < 0) continue;
    const key = body.slice(0, comma).trim();
    const fields = parseFields(body.slice(comma + 1));
    entries.push({ type: match[1].toLowerCase(), key, fields });
    entryStart.lastIndex = closeBrace + 1;
  }
  return entries;
}

function unwrap(value) {
  let result = (value ?? '').trim();
  let changed = true;
  while (changed && result.length >= 2) {
    changed = false;
    if ((result.startsWith('{') && result.endsWith('}')) || (result.startsWith('"') && result.endsWith('"'))) {
      result = result.slice(1, -1).trim();
      changed = true;
    }
  }
  return result;
}

function texToText(value) {
  let result = unwrap(value);
  result = result.replace(/\\url\{([^{}]*)\}/g, '$1');
  result = result.replace(/\\href\{([^{}]*)\}\{([^{}]*)\}/g, '$2');
  result = result.replace(/\\([&%_#$])/g, '$1');
  result = result.replace(/\\LaTeX/g, 'LaTeX').replace(/\\TeX/g, 'TeX');
  const accentMap = {
    "'a": 'á', "'e": 'é', "'i": 'í', "'o": 'ó', "'u": 'ú', "'A": 'Á', "'E": 'É', "'I": 'Í', "'O": 'Ó', "'U": 'Ú',
    '`a': 'à', '`e': 'è', '`i': 'ì', '`o': 'ò', '`u': 'ù', '`A': 'À', '`E': 'È', '`I': 'Ì', '`O': 'Ò', '`U': 'Ù',
    '^a': 'â', '^e': 'ê', '^i': 'î', '^o': 'ô', '^u': 'û', '^A': 'Â', '^E': 'Ê', '^I': 'Î', '^O': 'Ô', '^U': 'Û',
    '"a': 'ä', '"e': 'ë', '"i': 'ï', '"o': 'ö', '"u': 'ü', '"A': 'Ä', '"E': 'Ë', '"I': 'Ï', '"O': 'Ö', '"U': 'Ü',
    '~a': 'ã', '~n': 'ñ', '~o': 'õ', '~A': 'Ã', '~N': 'Ñ', '~O': 'Õ',
    'ua': 'ă', 'uA': 'Ă', 'oa': 'å', 'oA': 'Å', 'va': 'ǎ', 've': 'ě', 'vs': 'š', 'vS': 'Š',
  };
  result = result.replace(/\{\\([\'`^"~uov])\s*\{?([A-Za-z])\}?\}/g, (match, accent, letter) => accentMap[`${accent}${letter}`] ?? letter);
  result = result.replace(/\\([\'`^"~uov])\s*\{?([A-Za-z])\}?/g, (match, accent, letter) => accentMap[`${accent}${letter}`] ?? letter);
  result = result.replace(/\\c\s*\{?([cCsS])\}?/g, (match, letter) => ({ c: 'ç', C: 'Ç', s: 'ş', S: 'Ş' })[letter]);
  result = result.replace(/\\[a-zA-Z]+\s*/g, '');
  for (let i = 0; i < 4; i += 1) result = result.replace(/\{([^{}]*)\}/g, '$1');
  return result.replace(/\s+/g, ' ').trim();
}

function escapeCell(value) {
  return texToText(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\|/g, '&#124;')
    .replace(/\r?\n/g, ' ');
}

function formatAuthors(value) {
  return texToText(value).split(/\s+and\s+/i).join('; ');
}

function formatMonth(value) {
  const month = texToText(value).toLowerCase();
  const names = { jan: 'Jan', feb: 'Feb', mar: 'Mar', apr: 'Apr', may: 'May', jun: 'Jun', jul: 'Jul', aug: 'Aug', sep: 'Sep', oct: 'Oct', nov: 'Nov', dec: 'Dec' };
  return names[month] ?? month;
}

function formatDate(fields) {
  const year = texToText(fields.year);
  const month = formatMonth(fields.month);
  return month ? `${year}-${month}` : year;
}

function formatPublication(entry) {
  const f = entry.fields;
  const venue = texToText(f.journal || f.booktitle || f.publisher || '');
  const parts = [];
  if (venue) parts.push(venue);
  if (f.volume) parts.push(`vol. ${texToText(f.volume)}`);
  if (f.number) parts.push(`no. ${texToText(f.number)}`);
  if (f.pages) parts.push(`pp. ${texToText(f.pages)}`);
  if (f.publisher && venue !== texToText(f.publisher)) parts.push(texToText(f.publisher));
  if (!venue && f.howpublished) parts.push(texToText(f.howpublished));
  if (f.note && texToText(f.note) !== texToText(f.howpublished)) parts.push(texToText(f.note));
  let typeLabel = 'record';
  if (entry.type === 'inproceedings' || entry.type === 'incollection') typeLabel = 'conference paper';
  else if (entry.type === 'article' && f.journal) typeLabel = 'journal article';
  else if (entry.type === 'article') typeLabel = 'preprint / article';
  else if (entry.type === 'misc') typeLabel = 'preprint / project';
  else if (entry.type === 'book') typeLabel = 'book';
  else if (entry.type === 'inbook') typeLabel = 'book chapter';
  return `<code>${escapeCell(typeLabel)}</code>${parts.length ? `<br><small>${parts.map(escapeCell).join(' · ')}</small>` : ''}`;
}

function classifyUrl(url) {
  if (!url) return null;
  const lower = url.toLowerCase();
  if (lower.includes('arxiv.org')) return 'arXiv';
  if (lower.includes('doi.org')) return 'DOI';
  if (lower.includes('openreview.net')) return 'OpenReview';
  if (lower.includes('github.com')) return 'Code / Project';
  if (lower.includes('openai.com') || lower.includes('deepmind.google') || lower.includes('research.google')) return 'Project page';
  return 'Paper / Page';
}

function link(label, url) {
  return url ? `[${label}](${url})` : '';
}

function formatLinks(entry) {
  const f = entry.fields;
  const urls = [];
  const url = texToText(f.url);
  const doi = texToText(f.doi);
  const eprint = texToText(f.eprint);
  if (url) urls.push({ label: classifyUrl(url), url });
  if (eprint && !urls.some((item) => item.url.toLowerCase().includes('arxiv.org'))) {
    urls.push({ label: 'arXiv', url: `https://arxiv.org/abs/${eprint}` });
  }
  if (doi) {
    const doiUrl = doi.startsWith('http') ? doi : `https://doi.org/${doi}`;
    if (!urls.some((item) => item.url === doiUrl)) urls.push({ label: 'DOI', url: doiUrl });
  }
  return urls.map((item) => link(item.label, item.url)).filter(Boolean).join(' · ') || '—';
}

function extractCitations(text) {
  const keys = new Set();
  const citeRegex = /\\cite[a-zA-Z*]*\{([^}]*)\}/g;
  let match;
  while ((match = citeRegex.exec(text)) !== null) {
    for (const key of match[1].split(',')) {
      if (key.trim()) keys.add(key.trim());
    }
  }
  return keys;
}

function buildSectionFieldMap() {
  const map = new Map();
  for (const field of fieldDefs) {
    for (const filename of field.sectionFiles) {
      const filePath = path.join(sectionsDir, filename);
      if (!fs.existsSync(filePath)) continue;
      for (const key of extractCitations(readText(filePath))) {
        if (!map.has(key)) map.set(key, new Set());
        map.get(key).add(field.id);
      }
    }
  }
  return map;
}

function classifyByTitle(entry) {
  const haystack = `${texToText(entry.fields.title)} ${texToText(entry.fields.journal)} ${texToText(entry.fields.booktitle)}`.toLowerCase();
  const rules = [
    ['ui-web', /web|browser|website|user interface|ui\b|interface|design.to.code|sketch2code|pix2code|bolt\.new|lovable|replit|gameui|g[uú]i|front.end|frontend|software visualization/],
    ['scientific-visualization', /visualization|visual analytics|data2vis|plot|chart|scientific figure|visual aid|infographic/],
    ['structured-documents', /presentation|slide|document|diagram|layout|storybook|manim|theater program|report/],
    ['three-d-cad-world', /\b3d\b|cad|world model|gaussian splat|nerf|scene|shape|xr|virtual reality|physics|embodied|robot manipulation/],
    ['video-animation', /video|animation|movie|\b4d\b|text.to.video|image.to.video|cogvideo|phenaki|genie|sora|veo|mocogan|ray3/],
    ['image-generation', /image|text.to.image|diffusion|gan|vae|dalle|imagen|maskgit|controlnet|retouch|restoration|t2i|visual generation/],
  ];
  for (const [fieldId, pattern] of rules) {
    if (pattern.test(haystack)) return fieldId;
  }
  return 'foundations-methods';
}

function classifyEntry(entry, sectionMap) {
  const citedFields = [...(sectionMap.get(entry.key) ?? [])];
  const domainFields = citedFields.filter((fieldId) => fieldId !== 'foundations-methods');
  if (domainFields.includes('cross-domain-applications')) return 'cross-domain-applications';

  const titleField = classifyByTitle(entry);
  if (titleField !== 'foundations-methods') {
    if (domainFields.includes(titleField) || domainFields.length === 0) return titleField;
  }
  if (domainFields.length > 0) {
    for (const fieldId of fieldPriority) {
      if (domainFields.includes(fieldId)) return fieldId;
    }
  }
  return 'foundations-methods';
}

function sortEntries(entries) {
  return entries.sort((a, b) => {
    const yearA = Number(texToText(a.fields.year)) || 0;
    const yearB = Number(texToText(b.fields.year)) || 0;
    if (yearA !== yearB) return yearB - yearA;
    return texToText(a.fields.title).localeCompare(texToText(b.fields.title));
  });
}

function renderFieldOverview(grouped) {
  const lines = [
    '## Field Overview',
    '',
    '| Field | Chapters | Records | Publication years | Scope |',
    '| --- | --- | ---: | --- | --- |',
  ];
  for (const field of fieldDefs) {
    const entries = grouped.get(field.id) ?? [];
    const years = [...new Set(entries.map((entry) => texToText(entry.fields.year)).filter(Boolean))].sort((a, b) => Number(b) - Number(a));
    const span = years.length ? (years.length === 1 ? years[0] : `${years[years.length - 1]}-${years[0]}`) : '—';
    lines.push(`| [${field.title}](#${field.id}) | ${field.chapters} | ${entries.length} | ${span} | ${field.focus} |`);
  }
  return lines.join('\n');
}

function renderField(field, entries) {
  const years = [...new Set(entries.map((entry) => texToText(entry.fields.year)).filter(Boolean))].sort((a, b) => Number(b) - Number(a));
  const yearSummary = years.map((year) => `${year}: ${entries.filter((entry) => texToText(entry.fields.year) === year).length}`).join(' · ');
  const lines = [];
  lines.push(`<a id="${field.id}"></a>`);
  lines.push('<details>');
  const badgeUrl = `https://img.shields.io/badge/${encodeURIComponent(field.title.toUpperCase())}-${entries.length}%20papers-${field.badge}?style=flat-square&labelColor=111827`;
  lines.push(`<summary><strong>${field.title}</strong> · <code>Ch. ${field.chapters}</code> · <img src="${badgeUrl}" alt="${field.title}: ${entries.length} papers" height="20"></summary>`);
  lines.push('');
  lines.push(`> ${field.focus}`);
  lines.push('');
  lines.push(`<small><strong>Year distribution:</strong> ${yearSummary || 'No records assigned.'}</small>`);
  lines.push('');
  lines.push('| # | Paper | Authors | Date | Publication details | Paper / DOI / Page | BibTeX |');
  lines.push('| ---: | --- | --- | --- | --- | --- | --- |');
  entries.forEach((entry, index) => {
    const f = entry.fields;
    const title = escapeCell(f.title);
    const authors = escapeCell(formatAuthors(f.author));
    const date = escapeCell(formatDate(f));
    const key = escapeCell(entry.key);
    lines.push(`| ${index + 1} | **${title}** | <small>${authors}</small> | ${date} | ${formatPublication(entry)} | ${formatLinks(entry)} | [\`${key}\`](paper/references.bib) |`);
  });
  lines.push('');
  lines.push('</details>');
  lines.push('');
  return lines.join('\n');
}

function renderIndex(entries) {
  const grouped = new Map(fieldDefs.map((field) => [field.id, []]));
  const sectionMap = buildSectionFieldMap();
  for (const entry of entries) grouped.get(classifyEntry(entry, sectionMap)).push(entry);
  for (const field of fieldDefs) sortEntries(grouped.get(field.id));

  const lines = [
    '# Surveyed Papers',
    '',
    'Complete bibliography index for [Agentic Visual Generation: A Survey](README.md). The primary navigation is by research field; publication year is retained inside every row and used for sorting within each field. The BibTeX source remains authoritative.',
    '',
    `**Records:** ${entries.length}`,
    '',
    renderFieldOverview(grouped),
    '',
    '## Browse by Field',
    '',
    'Each field is collapsed by default for a compact reading experience. Expand a field to see the complete table, including full author lists, date, venue, volume/issue/pages when available, paper or DOI links, and the BibTeX key.',
    '',
  ];
  for (const field of fieldDefs) lines.push(renderField(field, grouped.get(field.id)));
  return lines.join('\n');
}

function readmeFieldTable(grouped, language) {
  const rows = [
    language === 'zh' ? '| 领域 | 对应章节 | 文献数 | 覆盖年份 |' : '| Field | Chapters | Records | Years |',
    '| --- | --- | ---: | --- |',
  ];
  for (const field of fieldDefs) {
    const entries = grouped.get(field.id) ?? [];
    const years = [...new Set(entries.map((entry) => texToText(entry.fields.year)).filter(Boolean))].sort((a, b) => Number(b) - Number(a));
    const span = years.length ? (years.length === 1 ? years[0] : `${years[years.length - 1]}-${years[0]}`) : '—';
    const title = `[${field.title}](PAPERS.md#${field.id})`;
    rows.push(`| ${title} | ${field.chapters} | ${entries.length} | ${span} |`);
  }
  return rows.join('\n');
}

function updateReadme(filePath, language, grouped) {
  const text = readText(filePath);
  const startHeadingCandidates = language === 'zh' ? ['## 收录论文', '## 论文集合'] : ['## Surveyed Papers', '## Paper Collection'];
  const endHeading = language === 'zh' ? '## 一眼了解' : '## At A Glance';
  const start = startHeadingCandidates.map((heading) => text.indexOf(heading)).find((index) => index >= 0);
  const end = text.indexOf(endHeading);
  if (start < 0 || end < 0 || end <= start) throw new Error(`Could not locate README section boundaries in ${filePath}`);

  const section = language === 'zh'
    ? [
        '## 论文集合',
        '',
        '当前综述追踪 **389 条 BibTeX 文献记录**。主页只按研究领域组织，年份保留在领域表格的 `Date` 列中，并作为每个领域内部的排序依据。',
        '',
        '<p align="center">',
        '  <a href="PAPERS.md"><img src="https://img.shields.io/badge/浏览-389%20篇完整领域索引-0f766e?style=for-the-badge&logo=readme&logoColor=white" alt="浏览 389 篇完整领域索引"></a>',
        '  <a href="paper/references.bib"><img src="https://img.shields.io/badge/来源-references.bib-2563eb?style=for-the-badge&logo=latex&logoColor=white" alt="来源 references.bib"></a>',
        '</p>',
        '',
        readmeFieldTable(grouped, 'zh'),
        '',
        '> 每个领域都可以完整展开或收起。展开后会显示论文名称、完整作者、年份/月份、会议或期刊、卷期页码、论文/DOI/项目链接，以及对应的 BibTeX key。',
        '',
        '详细索引：[`PAPERS.md`](PAPERS.md) · 权威元数据：[`paper/references.bib`](paper/references.bib)',
        '',
      ].join('\n')
    : [
        '## Paper Collection',
        '',
        'The survey currently tracks **389 BibTeX records**. The homepage is organized by research field; publication year is retained in each field table as the `Date` column and used for within-field sorting.',
        '',
        '<p align="center">',
        '  <a href="PAPERS.md"><img src="https://img.shields.io/badge/Explore-389%20paper%20field%20index-0f766e?style=for-the-badge&logo=readme&logoColor=white" alt="Explore 389 paper field index"></a>',
        '  <a href="paper/references.bib"><img src="https://img.shields.io/badge/Source-references.bib-2563eb?style=for-the-badge&logo=latex&logoColor=white" alt="Source references.bib"></a>',
        '</p>',
        '',
        readmeFieldTable(grouped, 'en'),
        '',
        '> Every field can be expanded or collapsed. Expanded tables provide the complete paper title, full author list, date, venue, volume/issue/pages when available, paper/DOI/project links, and BibTeX key.',
        '',
        'Detailed index: [`PAPERS.md`](PAPERS.md) · Authoritative metadata: [`paper/references.bib`](paper/references.bib)',
        '',
      ].join('\n');

  let nextText = `${text.slice(0, start)}${section}\n${text.slice(end)}`;
  const oldCollectionHeading = language === 'zh' ? '## 论文集合' : '## Paper Collection';
  const collectionStart = nextText.indexOf(oldCollectionHeading, start + section.length);
  const nextEnd = nextText.indexOf(endHeading, collectionStart);
  if (collectionStart >= 0 && nextEnd > collectionStart) {
    nextText = `${nextText.slice(0, collectionStart)}${nextText.slice(nextEnd)}`;
  }
  fs.writeFileSync(filePath, nextText, 'utf8');
}

const entries = parseBibTeX(readText(bibPath));
const sectionMap = buildSectionFieldMap();
const grouped = new Map(fieldDefs.map((field) => [field.id, []]));
for (const entry of entries) grouped.get(classifyEntry(entry, sectionMap)).push(entry);

fs.writeFileSync(papersPath, renderIndex(entries), 'utf8');
updateReadme(path.join(repoRoot, 'README.md'), 'en', grouped);
updateReadme(path.join(repoRoot, 'README_zh-CN.md'), 'zh', grouped);

console.log(`Rebuilt field index for ${entries.length} BibTeX entries.`);
