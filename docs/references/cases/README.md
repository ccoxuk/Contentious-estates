# Case Law References

This directory contains PDF copies of key judgments and case law.

## Key Cases

Typical references include:

- Ilott v Mitson [2017] UKSC 17 (Supreme Court landmark case)
- Cowan v Foreman [2019] EWCA Civ 1336 (standing to bring claims)
- Nahajec v Fowle [2016] EWHC 3166 (Ch) (maintenance test)
- Re Lilleyman (Deceased) [2012] EWHC 821 (Ch)

## File Naming

Format: `case-{short-title}-{year}.pdf`

Use the year of the decision, not the citation year if different.

Examples:
- `case-ilott-v-mitson-2017.pdf`
- `case-cowan-v-foreman-2019.pdf`
- `case-nahajec-v-fowle-2016.pdf`

## Metadata

Each PDF must have a corresponding metadata file in `/docs/references/metadata/`.

Required metadata fields:
- `title`: Full case name
- `type`: "case"
- `jurisdiction`: Court jurisdiction
- `date`: Date of judgment
- `citation`: Neutral citation and/or law report citation
- `source_url`: BAILII or official source URL
- `filename`: PDF filename

Optional fields:
- `court`: Specific court (e.g., "Supreme Court", "Court of Appeal")
- `judges`: List of judges
- `summary`: Brief summary of the decision
- `keywords`: Relevant legal concepts
