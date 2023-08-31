import requests
import json
print()
query = input("What type of news are you interested in = ")
api_key = "Enter your News app api Here"
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-07-25&sortBy=publishedAt&apiKey={api_key}"

req = requests.get(url)
data = json.loads(req.text)
articles = data["articles"]
for index,article in enumerate(articles,start=1):
    print(f"{index}.\t{article['title']}")
print()
choice = int(input("Enter which news you want to hear and enter index no accordingly (0 to quit) = "))
required_article = articles[choice-1]
print(f"Author = {required_article['author']}")
print(f"Title = {required_article['title']}")
print(f"Description = {required_article['description']}")
print(f"Details are = {required_article['content']}")
print(f"For more details you can visit this URL {required_article['url']}")