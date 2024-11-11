from django.apps import apps
from celery import shared_task
import helpers


@shared_task
def scrape_product_url_task(url):
    ProductScrapeEvent = apps.get_model("products", "ProductScrapeEvent")
    # open url
    html = helpers.scrape(url=url, solve_captcha=False)
    # scrape url
    data = helpers.extract_amazon_product_data(html)
    # save scraped data
    ProductScrapeEvent.objects.create_scrape_event(data, url=url)
    return
