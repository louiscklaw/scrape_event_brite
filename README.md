# SCRAPING EVENT BRITE

### purpose
    * to scrape the event brite about event information, simply try the scrape lib of python
    * transform webpage information to a csv

### setup environment
    * `sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`
    * `sudo apt-get install python3 python3-dev`

### to run
    * `pipenv run scrapy runspider scrape_event_brite.py`
    * the result is stored into `CSV_OUTPUT_FILE` defined inside script
