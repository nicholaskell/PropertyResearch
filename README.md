# Property Search

A normalized research repository for rural property due diligence and comparison.

## Workflow

1. Discover a candidate (Zillow search, listing link, address, etc.).
2. Research the property in its own ChatGPT conversation.
3. Save/update one Markdown record under `properties/<STATE>/`.
4. Use the portfolio-analysis rules to compare all researched properties.
5. Revisit records when price, status, broadband, zoning, or other material facts change.

## Source of truth

- `criteria.md` — buyer goals and research requirements.
- `property-template.md` — normalized property record format.
- `portfolio-rules.md` — cross-property scoring and ranking rules.
- `project-instructions.md` — short instructions for the ChatGPT Property Investigator project.

Chat = working research notebook.  
Markdown record = durable property database.
