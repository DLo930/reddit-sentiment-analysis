% This file is courtesy of Adam Blank (adamblan@cs), written for 15-151 and
% modified for 15-122.

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{122handout}

\LoadClass[11pt, letterpaper]{article}

\RequirePackage{fullpage}

\newcommand{\mfcs}{}
\newcommand{\elinenumber}{\end{linenumbers} \resetlinenumber}
\pagestyle{empty}

% \edef\oldtt{\ttdefault}
% \usepackage[scaled]{beramono}
% \usepackage[T1]{fontenc}
% \renewcommand*\ttdefault{\oldtt}

\usepackage[normalem]{ulem}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{xspace}
\usepackage{marvosym}
\usepackage{wrapfig}
\usepackage{enumerate}
\usepackage{textcomp}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{amstext}
\usepackage{amscd}
\usepackage{amsmath}
\usepackage{xspace}
\usepackage{theorem}
\usepackage{float}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{ifthen}
\usepackage{versions}
\usepackage{calc}
\usepackage{multicol}
\usepackage{pdflscape}
%\usepackage{tabu}
\usepackage[english]{babel}
\usepackage{import}  % Like input and include, but respects subdirectories
\usepackage{lineno}
\usepackage{datetime}
\newdateformat{wwwddmmm}
 {\dayofweekname{\THEDAY}{\THEMONTH}{\THEYEAR}
   \monthname[\THEMONTH] \ordinaldate{\THEDAY}}
\usepackage{framed}
\usepackage{../misc/latex/edition}  % Course semester
\usepackage{../misc/latex/c0}       % Listings style for c0

% Directories containing code and pictures
\newcommand{\code}{code}
\newcommand{\img}{img}


\newcommand{\back}{\textbackslash}

\newcommand{\band}{\&\&\;}
\newcommand{\xor}{\textasciicircum}

\newcommand{\cn}{C0\xspace}
\newcommand{\loopinv}{//@loop\_invariant\;}
\newcommand{\charconst}[1]{\texttt{\textquotesingle{#1}\textquotesingle}}

%\renewcommand{\familydefault}{\sfdefault}

\RequirePackage[usenames,dvipsnames]{xcolor}
\definecolor{colour}{rgb}{0,0,1}
\definecolor{checkpoint}{rgb}{1,0,0}
\newcommand{\solutionColor}{OliveGreen}
\newcommand{\sollineColor}{Green}


\setlength{\hoffset}{0in}
\setlength{\voffset}{-.5in}
\setlength{\textwidth}{6.5in}
\setlength{\oddsidemargin}{0in}
\setlength{\evensidemargin}{0in}
\setlength{\topmargin}{0in}
\setlength{\textheight}{9.2in}
\setlength{\headheight}{.5in}
\setlength{\headsep}{0pt}
\setlength{\marginparwidth}{59pt}

\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 1pt}
\setlength{\abovedisplayskip}{8pt plus 3pt minus 6pt}
\setlength{\intextsep}{15pt plus 3pt minus 6pt}

\renewcommand{\section}{\@startsection{section}{1}{0mm}%
                                  {1ex plus -1ex minus -.5ex}%
                                  {0.1ex plus -.2ex}%
                                  {\normalfont\Large\bfseries}}%
\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
                                    {0.5ex plus 1ex minus .2ex}%
                                    {-1em}%
                                    {\normalfont\normalsize\bfseries}}

%%%
\ifcsname issolution\endcsname%
 \relax
\else
 \newcommand{\issolution}{false}
\fi


%
% Default parameter values
%
\newcommand{\TheEdition}{\SEASON~\YEAR}
\newcommand{\mfcsedition}[1]{\renewcommand{\TheEdition}{#1}}

\newcommand{\TheNumber}{}
\newcommand{\mfcsnumber}[1]{\renewcommand{\TheNumber}{#1}}

\newcommand{\TheDate}{}
\newcommand{\mfcsdate}[1]{\renewcommand{\TheDate}{\wwwddmmm{#1}}}

\newcommand{\TheAuthor}{Josh Zimmerman}
\newcommand{\mfcsauthor}[1]{\renewcommand{\TheAuthor}{#1}}

\newcommand{\TheDocname}{}
\newcommand{\mfcsdocname}[1]{\renewcommand{\TheDocname}{#1}}

\renewcommand{\labelenumi}{(\alph{enumi})}

\definecolor{colour}{rgb}{0,0,0.6}

%
% Make the homework header
%

%%%%%%%%%%%%%%%%%% Toggling of document types %%%%%%%%%%%%%%%%%%%%%%
\newcommand{\ifthen}[2]{\ifthenelse{#1}{#2}{}}

\newcommand{\TheType}{Recitation}
\newcommand{\TheFlavorA}{}
\newcommand{\TheFlavorB}{}
\newboolean{ShowAuthor}
\setboolean{ShowAuthor}{true}
\newboolean{ShowSection}
\setboolean{ShowSection}{true}
\newboolean{ShowEdition}
\setboolean{ShowEdition}{true}
\newboolean{ShowNumbers}
\setboolean{ShowNumbers}{true}
\newboolean{ShowSolutions}
\setboolean{ShowSolutions}{true}
\newboolean{ShowDate}
\setboolean{ShowDate}{true}

\newcommand{\showEdition}{\setboolean{ShowEdition}{true}}
\newcommand{\hideEdition}{\setboolean{ShowEdition}{false}}
\newcommand{\showNumbers}{\setboolean{ShowNumbers}{true}}
\newcommand{\hideNumbers}{\setboolean{ShowNumbers}{false}}
\newcommand{\showDate}{\setboolean{ShowDate}{true}}
\newcommand{\hideDate}{\setboolean{ShowDate}{false}}
\newcommand{\showAuthor}{\setboolean{ShowAuthor}{true}}
\newcommand{\hideAuthor}{\setboolean{ShowAuthor}{false}}
\newcommand{\showSection}{\setboolean{ShowSection}{true}}
\newcommand{\hideSection}{\setboolean{ShowSection}{false}}


% Colored underline for solution
\newcommand\soluline{\bgroup\markoverwith
{\textcolor{\sollineColor}{\rule[-0.5ex]{2pt}{0.4pt}}}\ULon}

%%% Code to measure the remainder of a line of text
\usepackage{tikz}
\usetikzlibrary{calc}
\usetikzlibrary{shapes.arrows}

\newcommand{\currentsidemargin}{%
  \ifodd\value{page}%
    \oddsidemargin%
  \else%
    \evensidemargin%
  \fi%
}

\newcommand{\measureremainder}[1]{%
\begin{tikzpicture}[overlay,remember picture]
  % Helper nodes
  \path (current page.north west) ++(\hoffset, -\voffset)
    node[anchor=north west, shape=rectangle, inner sep=0, minimum width=\textwidth, minimum height=\textheight]
    (pagearea) {};

  \path (pagearea.north west) ++(1in+\currentsidemargin,-1in-\topmargin-\headheight-\headsep)
    node[anchor=north west, shape=rectangle, inner sep=0, minimum width=\textwidth, minimum height=\textheight]
    (textarea) {};

    % Measure distance to right text border
  \path let \p0 = (0,0), \p1 = (textarea.east) in
    [/utils/exec={\pgfmathsetlength#1{\x1-\x0}\global#1=#1}];
\end{tikzpicture}%
}

%% Single-line answers placeholders; see also \recitation, etc
\newlength{\answerLength}
\newcommand{\answerline}[2][]{% Line that extends to the right margin
  \ifthenelse{\equal{#1}{}}
    {\measureremainder{\answerLength}}%
    {\setlength{\answerLength}{#1}}%
  \soluline{\hspace*{\answerLength}}%
}
\newcommand{\shortanswerline}[1]{% Line of a specific length
  \settowidth{\answerLength}{#1}%
  \setlength{\answerLength}{1.8\answerLength}%
  \soluline{\hspace*{\answerLength}}%
}

%%% Formating a recitation
\newcommand{\recitation}{
  \renewcommand{\TheNumber}{$-\infty$}%  Various parameter settings
  \showEdition
  \hideNumbers
  \hideDate
  \hideAuthor
  \hideSection
  \makeatletter%   Redefine the \section command
  \renewcommand{\section}{
    \@startsection{section}{1}{0mm}%
                  {1ex plus -1ex minus -.5ex}%
                  {0.1ex plus -.2ex}%
                  {\normalfont\Large\bfseries%
                   \sffamily\color{colour}%
                      \ifthen{\boolean{ShowNumbers}}%
                      {\arabic{TheQuestionNumber}. %
                       \addtocounter{TheQuestionNumber}{1}%
                       \setcounter{ThePartNumber}{0}%
                     }}}%
  \renewcommand{\checkpoint}{%  Define the \checkpoint command
    \@startsection{section}{1}{0mm}%
                  {0.7ex plus -1ex minus -0.0ex}% was {1ex plus -1ex minus -.5ex}
                  {0.1ex plus -.2ex}%
                  {\normalfont\Large\bfseries%
                   \sffamily\color{checkpoint}
                   Checkpoint \arabic{TheCheckpointNumber}%
                   \addtocounter{TheCheckpointNumber}{1}%
                 }}%
  \makeatother%
  \ifthenelse{\equal{\issolution}{true}}%  Set up solution toggle
    {\solutions}
    {\setboolean{ShowSolutions}{false}%
     \let\solution\comment%
     \let\solutionFmt\comment}%
   \renewcommand{\TheType}{Recitation}
}

\newcommand{\lab}{
  \renewcommand{\TheNumber}{$-\infty$}
  \showEdition
  \hideNumbers
  \hideDate
  \hideAuthor
  \hideSection
  \makeatletter%   Redefine the \section command
  \renewcommand{\section}{
    \@startsection{section}{1}{0mm}%
                  {1ex plus -1ex minus -.5ex}%
                  {0.1ex plus -.2ex}%
                  {\normalfont\Large\bfseries%
                   \sffamily\color{colour}%
                   \ifthen{\boolean{ShowNumbers}}%
                      {\arabic{TheQuestionNumber}. }%
                   \addtocounter{TheQuestionNumber}{1}%
                   \setcounter{ThePartNumber}{0}%
                  }}%
  \makeatother%
  \ifthenelse{\equal{\issolution}{true}}%  Set up solution toggle
    {\solutions}
    {\setboolean{ShowSolutions}{false}%
     \let\solution\comment%
     \let\solutionFmt\comment}%
   \renewcommand{\TheType}{Lab}
}

\newcommand{\quiz}{
  \renewcommand{\TheNumber}{$-\infty$}
  \showEdition
  \hideAuthor
  \hideSection
  \ifthenelse{\equal{\issolution}{true}}
    {\solutions}
    {\setboolean{ShowSolutions}{false}
      \let\solution\comment%
      \let\solutionFmt\comment%
      \renewcommand{\TheType}{Quiz}}
}

\newcommand{\solutions}{
  \showEdition
  \hideDate
  \setboolean{ShowSolutions}{true}
  \let\solution\solutionsave
  \renewcommand{\answerline}[1]{%
    \soluline{\text{\color{\solutionColor} ##1}}%
  }
  \renewcommand{\shortanswerline}[1]{%
    \soluline{\text{\color{\solutionColor} ##1}}%
  }
  \renewcommand{\TheFlavorB}{ \textcolor{\solutionColor}{Solutions}}
}

\newcommand{\docs}{
  \showEdition
  \hideDate
  \hideSection
  \setboolean{ShowSolutions}{false}
  \renewcommand{\TheType}{\TheDocname}
}

\newenvironment{solution}[1][]{
  \par\medskip\color{\solutionColor}%
  \soluline{\textbf{Solution:}} #1%
}

\let\solutionsave\solution

%% Standalone solution formatting, e.g., new page
\newenvironment{solutionFmt}{}{}

\newcommand{\purpose}[1]{%
  \ifthen{\boolean{ShowPurpose}}{%
      \emph{Purpose:} #1
      $ $\\\\
  }%
}

\newcommand{\labcollab}{

%Unless arranged \textit{well in advance} with an instructor, you may
%\textit{only} attend the lab you're registered for.

\textbf{Collaboration:}
In lab, we encourage collaboration and
discussion as you work through the problems.
These activities, like recitation, are meant to get you to review what
we've learned, look at problems from a different perspective and allow
you to ask questions about topics you don't understand. We encourage
discussing problems with your neighbors as you work through
this lab!}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% \newcommand{\MakeHeader}[3]{~\vspace{-.4in}\\%
%    {\color{colour}%
%       {\noindent \Large%
%           \textbf{\textsf{15-122: Principles of Imperative Computation}}
%        \vspace{-1ex} \\ \rule[1mm]{\textwidth}{.3mm} \\%
%        \textbf{\textsf{\TheType\;#1\TheFlavorA\TheFlavorB
%                        \hfill \TheAuthor}}\vspace{.5ex}%
%       }}}
\newcommand{\MakeHeader}[3]{
~\vspace{-.4in}\\%
{\color{colour}%
  {\noindent \Large%
    \textbf{\textsf{\courseNumber: \courseName{}
    \ifthen{\boolean{ShowSection}}{}}}%
    \hfill
    \ifthen{\boolean{ShowEdition}}{\TheEdition}%
  }%
  \vspace{-1ex} \\
  \rule[1mm]{\textwidth}{.3mm} \\%
  {\noindent \Large%
   \makebox[\textwidth][l]{%
     \textbf{%
       \textsf{\TheType\;#1\TheFlavorA\TheFlavorB \hfill
               \ifthen{\boolean{ShowAuthor}}{\TheAuthor}%
%                \ifthen{\boolean{ShowDate}}%
               { #2}%
             }%
           }%
         }%
  }\medskip\par%
}%
}

%
% Make the section headers
%

\newcounter{TheQuestionNumber}
\newcounter{ThePartNumber}[TheQuestionNumber]
\newcounter{TheCheckpointNumber}

\newenvironment{question-base}[2]{%
            {\section*{\textbf{\textsf{\color{colour}%
                \ifthen{\boolean{ShowNumbers}}%
                       {\arabic{TheQuestionNumber}. }{#1}}}%
                \addtocounter{TheQuestionNumber}{1}%
                \setcounter{ThePartNumber}{0}}%
}}

\newenvironment{checkpoint}{%
            {\section*{\textbf{\textsf{\color{checkpoint}%
                Checkpoint \arabic{TheCheckpointNumber}%
                \addtocounter{TheCheckpointNumber}{1}%
                }}}}}

\newenvironment{question}[2][]{%
    \begin{question-base}{#2}{#1}%
}{%
    \end{question-base}%
}

% Retrieve question from file
\newcommand{\defaultQuestionLocation}{questions}
\newcommand{\inputQuestion}[2][\defaultQuestionLocation/]{%
  \subimport{#1}{#2}
}

\def\indented#1{\list{}{}\item[]}
\let\indented=\endlist

\renewenvironment{part}{%
    \addtocounter{ThePartNumber}{1}%
    \begin{indented}%
    \begin{enumerate}[{\bf (\arabic{TheQuestionNumber}.\alph{ThePartNumber})}]%
        \item%
}{\end{enumerate}\end{indented}}


\AtBeginDocument{{\MakeHeader{\TheNumber}{\TheDate}{}}}

\renewcommand{\documentclass}{}

% Grade school op: allows formatting of things like:
%      1
%    + 1
%     __
%      2
% \gsop{+}{1}{1}{2}
\newcommand{\gsop}[4]{
    \begin{minipage}{0.5cm}%
    \begin{align*}%
           &&\!\!#2\,\\[-0.5em]%
         #1&&\!\!#3\,\\\hline%
           &&\!\!#4\,%
    \end{align*}%
    \end{minipage}%
}


%% Class options
\DeclareOption{recitation}{\recitation}
\DeclareOption{lab}{\lab}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\usepackage{etoolbox}
\makeatletter
\patchcmd{\@addmarginpar}{\ifodd\c@page}{\ifodd\c@page\@tempcnta\m@ne}{}{}
\makeatother
\reversemarginpar

\tikzset{yellowFill/.style={top color=Yellow!20, bottom color=Yellow!80}}
\tikzset{yellowArrow/.style={draw=Black,yellowFill, single arrow, minimum
    height=#1, single arrow, single arrow head extend=0cm,}}

\tikzset{orangeFill/.style={top color=Orange!20, bottom color=Orange!80}}
\tikzset{orangeArrow/.style={draw=Black,orangeFill, single arrow, minimum
    height=#1, single arrow, single arrow head extend=0cm,}}

\tikzset{greenFill/.style={top color=Green!20, bottom color=Green!80}}
\tikzset{greenArrow/.style={draw=Black,greenFill, single arrow, minimum
    height=#1, single arrow, single arrow head extend=0cm,}}

\newcommand{\PT}[4][1cm]{%
\bgroup
\marginparwidth=1cm
\marginpar{\tikz[baseline=#4]\node [#3=#1] {\textbf{#2}\hspace*{-1mm}};}
\egroup}

\newcommand{\onePT}[1][0.5ex]{\PT{1pt}{yellowArrow}{#1}}
\newcommand{\twoPT}[1][0.5ex]{\PT{2pt}{orangeArrow}{#1}}
\newcommand{\threePT}[1][0.5ex]{\PT{3pt}{greenArrow}{#1}}


%% Displays tags for an exercise in 'answer' mode
\newcommand{\TAGS}[1]
{\ifthenelse{\equal{\issolution}{true}}%
  {\rule{0em}{0ex}%
   \marginpar{\footnotesize%
     \fcolorbox{black}{Gray!25}{%
       \parbox[t]{2cm}{\raggedright\textbf{TAGS:}\\#1}}}%
   \ignorespaces}%
  {}}%


\endinput
