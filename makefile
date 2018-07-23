make:
	vim makefile

venv:
	virtualenv -p python3 venv

deps:
	./venv/bin/pip3 install -r requirements.txt

run:
	./venv/bin/jupyter notebook

shell:
	./venv/bin/ipython

scrape:
	./venv/bin/scrapy runspider crawlers/example.py -s LOG_FILE=crawlers/example.log
