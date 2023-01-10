import pytest
from modules.scraper import get_citations_needed_count, get_citations_needed_report

def test_get_citations_needed_count():
    url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    actual_citation_count = get_citations_needed_count(url)
    expected_citation_count = 0
    assert actual_citation_count == expected_citation_count

def test_get_citations_needed_report():
    url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    actual_citation_report = get_citations_needed_report(url)
    expected_citation_report = 'The following statements need citations:\n'
    assert actual_citation_report == expected_citation_report
