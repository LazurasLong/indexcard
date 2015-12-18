# IndexCard RPG

Publications and sources for the IndexCard RPG.

The in-progress/next version is kept in the root:

  * `pandoc-template.tex`: Template used for generating `out.pdf` (unfinished!)
  * `somefont.ttf`: Font used in `pandoc-template.tex`
  * `out.pdf`: An example output
  * `source.md`: The only thing which is edited. The
    master copy. This source is used to produce `out.pdf`
    with `pandoc`, `somefont.ttf`, and `pandoc-template.tex`.

These names are subject to change.

Whenever there's an official release, `out.pdf` is generated,
but renamed to something like `RELEASE-SEMVER.pdf` where `SEMVER`
is the [semantic version](http://semver.org/) for that release.

## Required for Building

I *strongly* recommend using pandoc to output `out.tex` from
`source.md`, just to see!

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
