# momonala.github.io

Personal portfolio/resume site for Mohit Nalavadi. Static HTML built on the Start Bootstrap
"Resume" theme, served directly by GitHub Pages from `index.html` at the repo root — pushing to
`main` publishes the site, no build or deploy step required.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) for the Python test/lint tooling (there is no application code; `tests/test_nothing.py` is a placeholder so CI has something to run)

## Project Structure

```
momonala.github.io/
├── index.html            # The entire site (single page, section-anchored nav)
├── css/
│   └── resume.min.css    # Compiled stylesheet (committed directly, not built by CI)
├── js/
│   └── resume.min.js     # Scroll-spy / nav-collapse behavior
├── img/                  # Profile photo
├── scss/                 # Sass source for resume.min.css
├── gulpfile.js           # Gulp pipeline to recompile scss/ → css/ (no package.json is
│                          # committed, so `npm install` must be set up manually before this runs)
├── vendor/                # Bootstrap, Font Awesome, jQuery (committed, not fetched via CDN)
├── application-docs/      # Personal CV/cover letter/reference materials, unrelated to the site build
└── tests/
    └── test_nothing.py   # Placeholder so CI has a test suite to run
```

## Editing

Edit `index.html` directly for content changes. For style changes, either edit `css/resume.min.css`
directly, or edit the `scss/` source and recompile with Gulp (requires setting up `package.json`/
`node_modules` locally first, since neither is committed).
