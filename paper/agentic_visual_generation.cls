
%%======== Pckage options and base class ========
%\newboolean{logo}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hust}
\LoadClassWithOptions{article}
% pdfTeX exposes \pdfoutput; XeLaTeX does not.
\ifdefined\pdfoutput\pdfoutput=1\fi

% Layout
\RequirePackage[top=2.75cm, bottom=2.5cm, left=2.5cm, right=2.5cm, columnsep=0.65cm]{geometry}
\RequirePackage{microtype}
\RequirePackage{placeins}
\RequirePackage{hyphenat}
\RequirePackage{setspace}
\RequirePackage{parskip}
\RequirePackage[latin, english]{babel}
\RequirePackage{lipsum}
\RequirePackage{etoolbox}
\RequirePackage{fancyhdr}  % custom headers/footers
\RequirePackage{ulem}  % 引用下划线
\ifdefined\pdftexversion\DisableLigatures[f]{family=sf*}\fi
\RequirePackage{graphicx}
\RequirePackage{subcaption}


\RequirePackage{booktabs}
\RequirePackage{algorithm}
\RequirePackage{algpseudocode}
\RequirePackage{nicematrix}
\RequirePackage{multirow}
\RequirePackage{bm}
\newcommand{\nm}[1]{#1}
\RequirePackage[most]{tcolorbox}
\RequirePackage{xcolor}
% AI4GC / Zhejiang University reading-version palette.
\definecolor{hustbg}{HTML}{004EA2}
\definecolor{hustblue}{HTML}{004EA2}
\definecolor{hustred}{HTML}{1F2937}
\definecolor{hustgray}{HTML}{4B5563}
% Abstract background: a light tint of the Zhejiang University blue.
\colorlet{abstractbg}{hustblue!8}
\newcommand{\hustblue}[1]{{\bfseries\color{hustblue} #1}}
% Red emphasis preserves the template's existing \textbf font and sizing.
\newcommand{\hustred}[1]{{\color{hustred}\textbf{#1}}}
\algrenewcommand{\algorithmicrequire}{\sffamily\bfseries\color{hustblue}Input:}
\algrenewcommand{\algorithmicensure}{\sffamily\bfseries\color{hustblue}Output:}
% Reading-version header marks. These files are supplied in assets/.
% Vector PDF generated from the transparent assets/zju-logo.svg source.
\newcommand{\hustlogo}{assets/zju-logo.pdf}
\newcommand{\hustlogowidth}{24mm}
\newcommand{\aiGClogo}{assets/ai4gc-logo.png}
\newcommand{\aiGClogowidth}{18mm}
\newcommand{\githublogo}{assets/github-logo.pdf}
\newcommand{\githublogowidth}{3.5mm}
\newcommand{\githubmark}{\raisebox{-0.55mm}{\includegraphics[height=\githublogowidth]{\githublogo}}\hspace{0.8mm}}
% Optional full-width content placed immediately after the title and abstract
% in two-column mode.
\newcommand{\hustfrontmatter}{}

% References %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\RequirePackage{hyperref}
\RequirePackage[noabbrev,nameinlink]{cleveref}
\hypersetup{
  colorlinks,
  linkcolor=hustblue,
  citecolor=hustblue,
  urlcolor=hustblue
}



\RequirePackage[numbers, sort&compress]{natbib}
%\RequirePackage[round,authoryear]{natbib}
\def\bibfont{\small}

%%========  Bibliography using bibtex ========
\addto{\captionsenglish}{\renewcommand{\refname}{References}}
\newcommand{\citeas}[1]{\Needspace*{8\baselineskip}\noindent\bibentry{#1}}



% Section and caption format
\newcommand{\sectionfont}
{\fontsize{12}{10}\selectfont}

\newcommand{\subsectionfont}
{\fontsize{11}{10}\selectfont}

\RequirePackage{titlesec}
\titleformat*{\paragraph}{\itshape}
\titleformat*{\section}{\sectionfont\sffamily\bfseries\hustblue}
\titleformat*{\subsection}{\subsectionfont\sffamily\bfseries\hustblue}


%一级二级三级标题用12 11 10
\titleformat*{\subsubsection}{\normalsize\sffamily\bfseries\hustblue}


\newcommand{\bffont}
{\fontsize{8.8}{10}\selectfont}

% Use HUST red for inline emphasis while preserving the original font settings.
\DeclareTextFontCommand{\textbf}{\color{hustred}\bffont\bfseries\sffamily}



\RequirePackage{caption}
\DeclareCaptionLabelSeparator{custom}{}
\DeclareCaptionFormat{custom}{{\sffamily\textbf{#1 #2}} #3}
\captionsetup{singlelinecheck=true,format=custom,labelsep=custom,font=small}
\captionsetup[sub]{singlelinecheck=true,format=custom,labelsep=custom,font=small}


\ifXeTeX
  \RequirePackage{fontspec}
  \setsansfont[Path=assets/,BoldFont=ByteSans-Bold.ttf]{ByteSans-Bold.ttf}
  \newfontfamily\bytesansmediumfont[Path=assets/]{ByteSans-Medium.ttf}
\else
  \RequirePackage[T1]{fontenc}
  \DeclareFontFamily{T1}{bytesans}{}
  \DeclareFontShape{T1}{bytesans}{m}{n}{<-> s * [1] assets/bytesans}{}
  \pdfmapline{+bytesans < assets/ByteSans-Bold.ttf <T1-WGL4.enc}
  \renewcommand{\sfdefault}{bytesans}%
  \DeclareFontFamily{T1}{bytesansmedium}{}
  \DeclareFontShape{T1}{bytesansmedium}{m}{n}{<-> s*[1] assets/bytesansmedium}{}
  \pdfmapline{+bytesansmedium < assets/ByteSans-Medium.ttf <T1-WGL4.enc}
\fi
\renewcommand{\rmdefault}{cmr}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Authors, affiliations, infos %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\renewcommand\addtolist[5][]{
  \begingroup
    \if\relax#3\relax\def\sep{}\else\def\sep{#5}\fi
    \let\protect\@unexpandable@protect
    \xdef#3{\expandafter{#3}\sep #4[#1]{#2}}%
  \endgroup
}

\newcommand{\authorfont}
 {\fontsize{8.8}{10}\selectfont}

\newcommand\authorlist{}
\newcommand\authorformat[2][]{\authorfont {\sffamily #2$^{#1}$}}
\renewcommand\author[2][]{\addtolist[#1]{#2}{\authorlist}{\authorformat}{, }}

%给affiliation换成medium字体

\newcommand{\affiliationfont}
 {\fontsize{8.6}{10}\selectfont}

\newcommand\affiliationlist{}
\ifXeTeX
  \newcommand\affiliationformat[2][]{{\affiliationfont {\bytesansmediumfont $^{#1}$#2}}}
\else
  \newcommand\affiliationformat[2][]{{\affiliationfont {\fontfamily{bytesansmedium}\selectfont $^{#1}$#2}}}
\fi
\newcommand\affiliation[2][]{\addtolist[#1]{#2}{\affiliationlist}{\affiliationformat}{\par}}

\newcommand{\contributionfont}
 {\fontsize{7.4}{8.6}\selectfont}

\newcommand\contributionlist{}
\newcommand\contributionformat[2][]{{\contributionfont $^{#1}$#2}}
\newcommand\contribution[2][]{\addtolist[#1]{#2}{\contributionlist}{\contributionformat}{, }}

\newcommand{\emailfont}{\fontsize{7.2}{8.4}\selectfont}
\newcommand\emaillist{}
\newcommand\emailformat[2][]{%
  {\emailfont\ttfamily\color{hustgray}%
    \if\relax\detokenize{#1}\relax
      \href{mailto:#2}{#2}%
    \else
      #1: \href{mailto:#2}{#2}%
    \fi}%
}
\newcommand\email[2][]{\addtolist[#1]{#2}{\emaillist}{\emailformat}{, }}

\newcommand{\checkdatafont}
{\fontsize{7.92}{10}\selectfont}

\newcommand\checkdatalist{}
\newcommand\checkdataformat[2][]{{\small {\sffamily\bfseries\color{hustred} #1:} {\color{hustgray}#2}}}
\newcommand\checkdata[2][]{\addtolist[#1]{#2}{\checkdatalist}{\checkdataformat}{\par}}


\newcommand{\abstractinfont}
 {\fontsize{8.6}{10.2}\selectfont}

\renewcommand{\abstract}[1]{\def\abstractlist{{\abstractinfont #1}}}
\renewcommand\date[1]{\checkdata[Date]{#1}}
\newcommand\correspondence[1]{\checkdata[Correspondence]{#1}}


\newcommand{\titlefont}
 {\fontsize{15}{17}\selectfont}

\renewcommand{\title}[1]{\newcommand{\titlelist}{\titlefont{\sffamily #1}}}


\newcommand{\abstractfont}
 {\fontsize{10.5}{11}\selectfont}

\newcommand{\beginabstract}{\abstractfont{\sffamily\bfseries \hustblue{Abstract}\par}}

\newcommand{\beginappendix}{\appendix{\titlefont\sffamily \hustblue{Appendix}\par}}


\usepackage[subfigure]{tocloft}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}} % 目录后一行连续的点
\renewcommand{\cftsecfont}{\sffamily}
%\renewcommand{\cftsubsecfont}{\sffamily\large}
\renewcommand{\cftsecpagefont}{\sffamily}{\color{hustblue}}
\renewcommand{\cfttoctitlefont}
{\sffamily\sectionfont\hustblue}


%%======== Header and Footer Content ========
\fancypagestyle{firststyle}{
    \fancyhead{}
    \fancyfoot{}
}

%去除页眉页脚横线
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}



% rules for title box at top of first page
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%此处为标题两侧线段，0.5pt 长160mm
\newcommand{\@toptitlebar}{
  \hustblue{\hrule height 0.5pt }
  \vskip 6mm
  %\vskip -\parskip%
}
\newcommand{\@bottomtitlebar}{
  \vskip 6mm
  %\vskip -\parskip
  \hustblue{\hrule height 0.5pt}
  %\vskip 0.09in%
}


% Titlebox %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Abstract box uses gray background style (inspired by fairmeta)

\newcommand{\mymaketitle}{%
  \thispagestyle{empty}%
  \begin{tcolorbox}[
    enhanced, frame hidden, colback=abstractbg,
    left=8mm, right=8mm, top=9mm, bottom=8mm,
    arc=10pt, before skip=0pt, after skip=0pt,
    grow to left by=1.5pt, grow to right by=1.5pt]
    \setlength{\parindent}{0cm}
    \setlength{\parskip}{0cm}
    \begin{center}
      \href{https://www.zju.edu.cn/english/}{\includegraphics[height=24mm]{\hustlogo}}\hspace{9mm}%
      \href{https://ai4gc.org/}{\includegraphics[height=22mm]{\aiGClogo}}\\[4mm]
      {\titlelist\par}
      \vspace{3mm}
      {\authorlist\par}
      \vspace{2mm}
      {\affiliationlist\par}
      \vspace{2mm}
      {\contributionlist\par}
      \ifdefempty{\emaillist}{}{\vspace{1.5mm}\emaillist\par}
    \end{center}
    \vspace{3mm}
    \begin{center}
      \beginabstract
    \end{center}
    \vspace{1.5mm}
    \abstractlist\par
    \vspace{3mm}
    {\setlength{\parskip}{0cm}\ifdefempty{\checkdatalist}{}{\checkdatalist\par}}
  \end{tcolorbox}
  \FloatBarrier
}


% Remember the requested layout so the main document can temporarily use
% full-width front matter before switching to the two-column body.
\newif\ifhusttwocolumn
\if@twocolumn
  \husttwocolumntrue
\else
  \husttwocolumnfalse
\fi

\if@twocolumn%
\renewcommand{\maketitle}{
\twocolumn[%
 \vskip 3mm
  \mymaketitle
  \hustfrontmatter
  \vskip 8mm
]
}%
\else%
\renewcommand{\maketitle}{
  \mymaketitle
  \vskip 8mm
  %\setlength{\parskip}{4mm}
}%
\fi
