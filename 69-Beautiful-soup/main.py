import requests
from bs4 import BeautifulSoup

# Beautiful soup
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the BBC News (http://www.bbc.co.uk/news)

URL = 'https://www.bbc.co.uk/news'
ARTICLE_CLASS = 'gs-c-promo-heading__title'

def main():
  content = requests.get(URL).text
  soup = BeautifulSoup(content, features='html5lib')

  articles = soup.find_all(class_=ARTICLE_CLASS)
  articles = list(dict.fromkeys(articles))

  if len(articles):
    print('Articles:')
    
    for article in articles:
      print(f'* {article.text}')

if __name__ == '__main__':
  main()