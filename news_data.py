import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

# 1. Define Categories and Google News RSS URLs
categories = {
    'Politics': 'https://news.google.com/rss/search?q=politics&hl=en-IN&gl=IN&ceid=IN:en',
    'Sports': 'https://news.google.com/rss/search?q=sports&hl=en-IN&gl=IN&ceid=IN:en',
    'Business': 'https://news.google.com/rss/search?q=business&hl=en-IN&gl=IN&ceid=IN:en',
    'Technology': 'https://news.google.com/rss/search?q=technology&hl=en-IN&gl=IN&ceid=IN:en',
    'Entertainment': 'https://news.google.com/rss/search?q=entertainment&hl=en-IN&gl=IN&ceid=IN:en',
    'Health': 'https://news.google.com/rss/search?q=health&hl=en-IN&gl=IN&ceid=IN:en',
    'Science': 'https://news.google.com/rss/search?q=science&hl=en-IN&gl=IN&ceid=IN:en',
    'Environment': 'https://news.google.com/rss/search?q=environment&hl=en-IN&gl=IN&ceid=IN:en'
}

# 2. Function to fetch and parse RSS feed
def fetch_articles_from_rss(url):
    articles = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='xml')
    items = soup.findAll('item')
    
    for item in items:
        title = item.title.text
        description = item.description.text if item.description else ''
        articles.append(title + " " + description)
    
    return articles

# 3. Fetch data for each category
news_data = []

for category, rss_url in categories.items():
    print(f"Fetching articles for {category}...")
    try:
        articles = fetch_articles_from_rss(rss_url)
        for article in articles[:150]:  # Get up to 150 articles per category
            news_data.append({'text': article.strip(), 'category': category})
    except Exception as e:
        print(f"Error fetching {category}: {e}")
    time.sleep(1)

# 4. Save to CSV
df = pd.DataFrame(news_data)
df.drop_duplicates(subset='text', inplace=True)
df.dropna(inplace=True)
df.to_csv('news_dataset_rss.csv', index=False)

print("\n✅ RSS Dataset created successfully! Total samples:", len(df))
