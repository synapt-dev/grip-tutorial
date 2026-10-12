from pathlib import Path

from demo_docs.pages import titles

DOCS = Path(__file__).resolve().parents[1] / "docs"


def test_every_page_has_a_title():
    found = titles(DOCS)
    assert found, "no pages found"
    assert all(found.values()), found
