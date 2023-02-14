from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web=response.text

soup=BeautifulSoup(yc_web, "html.parser")
articles= soup.find_all(name='span', class_='titleline')
article_texts = []
article_links =[]
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)

links = soup.find_all(class_="titleline")
article_links = [link_tag.find(name="a").get("href") for link_tag in links]
article_upvotes = [score.getText() for score in soup.find(name='span', class_='score')]

with open("movies.txt", mode="w") as file:
    i=1
    for movie in article_texts:
        file.write(f"{i}) {movie}\n")
        i+=1




