# Textbook sources

Narrative chapter Markdown lives in `../chapters/` (CC BY-NC 4.0). This
directory holds book-level front matter and export configuration for **PDF**
and **DOCX**.

## Toolchain

| Tool | Role |
|------|------|
| [Quarto](https://quarto.org/) | Preferred: `textbook/physibot.qmd` → PDF / DOCX / HTML |
| [Pandoc](https://pandoc.org/) | Fallback DOCX (and PDF if a LaTeX engine is installed) |
| LaTeX (TeX Live) | Required for Quarto/Pandoc PDF |

## Build commands

From the **repository root**:

```bash
# Quarto (preferred)
quarto render textbook/physibot.qmd --to pdf
quarto render textbook/physibot.qmd --to docx
# Outputs default next to the .qmd unless --output-dir is set:
#   textbook/physibot.pdf
#   textbook/physibot.docx
# Course convention: copy or render into textbook/exports/
mkdir -p textbook/exports
quarto render textbook/physibot.qmd --to pdf --output-dir textbook/exports
quarto render textbook/physibot.qmd --to docx --output-dir textbook/exports
```

Pandoc fallback (concatenates front matter + all chapters):

```bash
./docs/export-tools/export-stub.sh
# Writes textbook/exports/physibot.docx when pandoc is available
# Writes textbook/exports/physibot.pdf when pandoc + pdflatex/xelatex exist
```

## Status

See `../STATUS.md` for whether exports were verified in CI/agents and any
missing packages (Quarto, Pandoc, TeX).
