# Scheduled Web Scraper with Django and Celery
<hr>

### Quick Setup
Starting venv:
```bash
python3 -m venv venv
source venv/bin/activate
```
Installing requirements:
```bash
python -m pip install pip --upgrade
python -m pip install -r requirements.txt
```
Create .env in src/.env with:
```python
CELERY_BROKER_REDIS_URL="redis://localhost:6170"
DEBUG=True
```
Running:
```bash
python manage.py runserver
```
```bash
celery -A config worker --beat info
```

### In this project I used
<ul>
  <li>Django</li>
  <li>Celery</li>
  <li>Selenium</li>
  <li>Jupyter</li>
  <li>BeautifulSoup4</li>
</ul>

<hr>

### What I learned
<ul>
  <li>Django + Celery integration</li>
  <li>Django + Jupyter integration</li>
  <li>Selenium with Jupyter</li>
  <li>Proxy scraping with Selenium + Bright Data</li>
  <li>Parsing data with BeautifulSoup4</li>
  <li>Celery tasks for scheduled scrape events (in Django Admin)</li>
</ul>
