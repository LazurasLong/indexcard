# IndexCard RPG

Publications and sources for the IndexCard RPG.

  * `ruleset.pdf`: Core game rules, plus some example
    supplemental rulesets
  * `forever-maze.pdf`: Example novelesque *path cards*

Info about other files:

  * `topdf.sh`: You can run this script to generate `rulesets.pdf`
    and `forever-maze.pdf` from their Markdown sources.
  * `pandoc-template.tex`: Template used for generating PDFs
    from markdown source (`rulesets.md`, `forever-maze.md`)
  * `somefont.ttf`: Font used in `pandoc-template.tex`
  * `rulesets.md`: The only thing which is edited. The
    master copy. This source is used to produce `rulesets.pdf`
    with `pandoc`, `somefont.ttf`, and `pandoc-template.tex`.

`pandoc` is used to convert the `*.md` files to PDF (see below!).

## Releases

Whenever there's an official release, `rulesets.pdf` is generated,
but renamed to something like `RELEASE-SEMVER.pdf` where `SEMVER`
is the [semantic version](http://semver.org/) for that release.

## Required for Building

I *strongly* recommend using pandoc to output `out.tex` from
`source.md`, just to see!

To build the markdown files to PDF you'll need `pandoc`.

Follow the install guide for your system:

  * Install: http://pandoc.org/installing.html

You can use the `topdf.sh` script to generate the PDFs from the
Markdown source, which basically does this command:

```
pandoc --latex-engine=xelatex --template=./pandoc-template.tex \
       rulesets.md -o rulesets.pdf
```

I personally have been building with `pandoc` 1.15.1.1.

## OSX

Additional steps to get things working...

  * `sudo ln -s /usr/texbin/pdflatex /usr/local/bin/`
  * `sudo ln -s /usr/texbin/xelatex /usr/local/bin/`

See also:

  * https://gist.github.com/georgiana-gligor/fd247d02f8a44ce745db
  * http://www.tug.org/mactex/morepackages.html
  * http://stackoverflow.com/questions/13214797/markdown-to-pdf-using-pandoc-since-xetex-deprecation
