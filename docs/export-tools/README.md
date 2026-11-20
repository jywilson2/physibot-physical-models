# Textbook export tools

Build **PDF** and **DOCX** of the PhysiBot narrative from Markdown sources.

## Preferred order

1. **Quarto** (when installed): `quarto render textbook/physibot.qmd --to pdf --output-dir textbook/exports`
2. **Host Pandoc + TeX**: `./docs/export-tools/export-stub.sh`
3. **Docker (no host TeX)**: `./docs/export-tools/export-pdf-docker.sh`

## Artifacts

| Path | Notes |
|------|--------|
| `textbook/exports/physibot.pdf` | Sample PDF may be committed for review (~250 KB, CC BY-NC 4.0) |
| `textbook/exports/physibot.docx` | Regenerated locally; usually gitignored |

## Docker recipe

```bash
# From repo root (requires Docker daemon)
./docs/export-tools/export-pdf-docker.sh
# equivalent:
docker build -f docker/Dockerfile.textbook -t physibot/textbook-export:local .
docker run --rm -v "$PWD:/book:rw" -w /book physibot/textbook-export:local
```

## Host packages (Debian/Ubuntu)

```bash
sudo apt-get install -y pandoc texlive-xetex texlive-fonts-recommended \
  texlive-latex-extra lmodern fonts-dejavu librsvg2-bin
./docs/export-tools/export-stub.sh
```

Chapter figures (`../textbook/figures/*.svg`) resolve via Pandoc
`--resource-path=chapters:.`. PDF SVG embedding needs `rsvg-convert`
(`librsvg2-bin`). Math uses `\(...\)` / `\[...\]`; the export script enables
`tex_math_single_backslash` so XeLaTeX receives real math mode.
