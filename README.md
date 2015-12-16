# Required for Building

To build `source.md` to PDF you'll need `pandoc`.

Follow the install guide for your system:

  * Install: http://pandoc.org/installing.html

Command to build:

```
pandoc --latex-engine=xelatex --template=./pandoc-template.tex \
       source.md -o out.pdf
```

## OSX

Additional steps to get things working...

  * `sudo ln -s /usr/texbin/pdflatex /usr/local/bin/`
  * `sudo ln -s /usr/texbin/xelatex /usr/local/bin/`

See also:

  * https://gist.github.com/georgiana-gligor/fd247d02f8a44ce745db
  * http://www.tug.org/mactex/morepackages.html
  * http://stackoverflow.com/questions/13214797/markdown-to-pdf-using-pandoc-since-xetex-deprecation
