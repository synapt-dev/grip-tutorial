from pathlib import Path


def titles(directory: Path) -> dict:
    """Each markdown page in `directory` mapped to its title, the text of its first line after '# '."""
    out = {}
    for page in sorted(Path(directory).glob("*.md")):
        first = page.read_text().splitlines()[0] if page.read_text() else ""
        out[page.name] = first[2:] if first.startswith("# ") else None
    return out
