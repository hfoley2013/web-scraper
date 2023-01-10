import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    citations_needed = soup.find_all("a", title="Wikipedia:Citation needed")
    citation_count = len(citations_needed)
    
    return citation_count

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    citations_needed = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
    statements_needing_citations = 'The following statements need citations:\n'
    
    for element in citations_needed:
        statements_needing_citations += element.parent.get_text() + "\n"
    
    return str(statements_needing_citations)

# Test the function
if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    get_citations_needed_count(url)
    get_citations_needed_report(url)
