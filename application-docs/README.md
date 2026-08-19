# Job Applications

A personal repo for managing job applications: CVs, cover letters, reference letters, and supporting notes. The **text files (`.txt`)** are the editable source of truth; **do not edit any `.pdf` or `.pages` files**—they are generated or finalized documents meant to be sent to companies or kept as archives.

---

## ⚠️ Editing rules

- **Edit only `.txt` files.** Use them to refine content, then update the corresponding PDFs (e.g. in Word/Pages/Google Docs) when you’re ready to export.
- **Do not edit `.pdf` or `.pages` files** in this repo. PDFs are the versions you send; `.pages` are the editable originals. Changing them directly would bypass the workflow below and can get out of sync with the notes.

The `.txt` files are intended for:
1. **AI-assisted improvement of PDFs** — Use the text as input so AI can suggest or rewrite bullets, summaries, or cover letter paragraphs; you then apply those changes in your word processor and export a new PDF.
2. **Automated Q&A** — Use the same text so AI can answer questions about your experience, projects, expectations, or interview prep (e.g. “explain the reverse image search project,” “what are you looking for in your next role?”).

---

## Repository tree and file purposes

```
job_apps/
├── README.md
│   Purpose: This file. Project overview, editing rules, and file index.
│
├── notes-cv.txt
│   Purpose: Plain-text version of your CV/resume. Source for AI to suggest improvements
│            or to answer questions about your experience, skills, and timeline. Mirrors
│            the content you maintain in your CV editor; update this when you change the CV.
│
├── notes-coverletter.txt
│   Purpose: Reusable cover letter narrative (intro, experience summary, what you’re
│            looking for, sign-off). Use with AI to tailor or strengthen cover letters
│            before you paste into your .pages/.docx and export to PDF.
│
├── notes-job-details-long.txt
│   Purpose: Detailed project briefs and interview Q&A material (e.g. Commercetools
│            reverse image search, Grandperspective cloud backup & ETL). For AI to
│            answer deep-dive questions about projects, tradeoffs, and “what would you
│            do differently?” in interviews or application forms.
│
├── mohitNalavadiCV2026.pdf
│   Purpose: Current CV in PDF form. Send this to companies. Do not edit; update via
│            your word processor and notes-cv.txt, then re-export.
│
├── mohitNalavadiCoverLetter2026.pages
│   Purpose: Editable cover letter template in Apple Pages. Do not edit in repo
│            workflow; change content using notes-coverletter.txt and your editor, then
│            update this file and export to PDF.
│
├── mohitNalavadiCoverLetter2026.pdf
│   Purpose: Current generic cover letter PDF. Send or adapt per application. Do not
│            edit; update via .pages and notes-coverletter.txt, then re-export.
│
├── EN_ReferenceLetter_MNalavadi.docx.pdf
│   Purpose: English reference letter (PDF). For applications that request references
│            or reference letters. Do not edit; source is the original .docx elsewhere.
│
├── DE_ReferenceLetter_MNalavadi.docx.pdf
│   Purpose: German reference letter (PDF). Same use as above, German version. Do not
│            edit; source is the original .docx elsewhere.
│
└── old/
        Purpose: Archive of past applications, old CVs/cover letters, scripts, and
                 2025 application artifacts. Never touch; reference only.
```

---

## Suggested workflow

1. **CV:** Keep `notes-cv.txt` in sync with your real CV. Use it with AI to improve wording or structure, then apply changes in your CV editor and export `mohitNalavadiCV2026.pdf`.
2. **Cover letter:** Draft or refine in `notes-coverletter.txt` (optionally with AI). Copy into `mohitNalavadiCoverLetter2026.pages`, customize per role if needed, then export to PDF.
3. **Interview / form Q&A:** Use `notes-job-details-long.txt` and `notes-cv.txt` so AI can answer questions about projects, expectations, and experience consistently.
4. **Reference letters:** Attach `EN_ReferenceLetter_MNalavadi.docx.pdf` or `DE_ReferenceLetter_MNalavadi.docx.pdf` when requested; do not edit these PDFs in this repo.

---

## Summary

| What you edit | What you don’t edit |
|---------------|---------------------|
| `*.txt` (notes-cv, notes-coverletter, notes-job-details-long) | All `.pdf` and `.pages` files |
| | Everything in `old/` (never touch) |

The text files are the single source of truth for AI-assisted improvements and for answering questions about your background and expectations.
