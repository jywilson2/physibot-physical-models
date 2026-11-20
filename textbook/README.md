# Textbook sources

Narrative chapter Markdown lives in `../chapters/` (CC BY-NC 4.0). This
directory holds book-level front matter and export configuration for **PDF**
and **DOCX**.

## Toolchain

| Tool | Role |
|------|------|
| [Quarto](https://quarto.org/) | Preferred: `textbook/physibot.qmd` → PDF / DOCX / HTML |
| [Pandoc](https://pandoc.org/) + TeX Live | Fallback via `../docs/export-tools/export-stub.sh` |
| Docker + `Dockerfile.textbook` | Reproducible PDF/DOCX with no host TeX |

## Build commands

From the **repository root**:

```bash
# Quarto (preferred when installed)
mkdir -p textbook/exports
quarto render textbook/physibot.qmd --to pdf --output-dir textbook/exports
quarto render textbook/physibot.qmd --to docx --output-dir textbook/exports

# Pandoc + host TeX
./docs/export-tools/export-stub.sh

# Docker (no host TeX)
./docs/export-tools/export-pdf-docker.sh
```

## Sample artifact

`exports/physibot.pdf` may be committed as a review sample (CC BY-NC 4.0).
Regenerate before release; DOCX stays local/gitignored by default.

## Status

See [`../STATUS.md`](../STATUS.md) and [`../docs/export-tools/README.md`](../docs/export-tools/README.md).
