import requests
def getNews():
    API_KEY = 'Your NewsAPI'
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + API_KEY
    news = requests.get(url).json()
    articles = news["articles"]
    my_articles = []
    my_news = []
    for article in articles:
        my_articles.append(article["title"])
        my_articles.append(article["description"])
    for i in range(20):
        my_news.append(my_articles[i])
    return my_news
