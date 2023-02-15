# Project: Wikipedia Missing Citations Report Generator

## Author: Harper Foley

### Links and Resources

* [BeautifulSoup 4 Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Setup

* Required Libraries
  * `pip install pytest`
  * `pip install beautifulsoup4`
  * `pip install requests`

### How to use

* To set up this repo create a local repository on your machine
* Create a virtual environment for Python
  * `python3.11 -m venv .venv`
* Activate the venv file
  * `source .venv/bin/activate`
* Install `pytest`
  * `pip install pytest`
* Install`beautifulsoup4`
  * `pip install beautifulsoup4`
* Install `requests`
  * `pip install requests`
* Use `git clone` to clone the repo to your local machine
  * `git clone https://github.com/hfoley2013/web-scraper.git`
* Your repo is now ready to run the **Wikipedia Missing Citations Report Generator** program
* Run the code using `python modules/scraper.py`
* You will be prompted for a search URL in the command line
* Enter a Wikipedia URL into the CLI and hit `enter`
* The program will run and give you the count of the number of citations needed and the statements that require citation

## Tests

* How do you run tests?
  * Tests are conducted via `pytest`
  * You may need to specify the location of the tests as follows:
    * `pytest tests/test_scraper.py`
