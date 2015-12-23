pandoc --latex-engine=xelatex --template=./pandoc-template.tex \
       rulesets.md -o rulesets.pdf
pandoc --latex-engine=xelatex --template=./pandoc-template.tex \
       forever-maze.md -o forever-maze.pdf
