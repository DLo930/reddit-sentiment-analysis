Compile the whole set of notes by running either
	# pdflatex all
or
	# make all


Chapter writing hygiene:
- Individual chapters are normal, stand-alone Latex files (possibly
  files that input other files)
- Define the lecture/chapter title using \lectitle
- Do not leave text after \end{document}.  You can instead bracket it
  between \begin{comment} and \end{comment}


TODO:
- Add labels and cross-references
- Remove references to things done in class
- Add exercises
- Add frontmatter blurbs
- Add references and index words
