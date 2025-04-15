from firecrawl import FirecrawlApp

# Replace 'fc-YOUR_API_KEY' with your actual API key
app = FirecrawlApp(api_key="fc-fc-238e26dfc8784046b5e17416d42a2f48")

# Crawl a website:
try:
    crawl_status = app.crawl_url(
        'https://firecrawl.dev',
        params={
            'limit': 100,
            'scrapeOptions': {'formats': ['markdown', 'html']}
        },
        poll_interval=30
    )
    print("Crawl Status:", crawl_status)
except Exception as e:
    print("An error occurred:", e)