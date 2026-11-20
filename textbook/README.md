# Textbook sources

Narrative chapter Markdown lives in `../chapters/`. This directory holds
book-level front matter and export configuration for **PDF** and **DOCX**.

## Intended toolchain

- Primary: [Quarto](https://quarto.org/) (`book` project) **or** Pandoc from concatenated Markdown.
- Outputs: `exports/physibot.pdf`, `exports/physibot.docx` (not generated in PMT-2).

## Build (later)

```bash
# Quarto (preferred when installed)
quarto render textbook/physibot.qmd

# Or Pandoc stub
./docs/export-tools/export-stub.sh
```

PMT-2 only ships structure + stubs — full narrative and verified exports are later tasks.
