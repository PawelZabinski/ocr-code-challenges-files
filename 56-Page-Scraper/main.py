import requests
import json
import ehp

# Page Scraper
# Have the programme connect to a site and pulls out all the links, or images, and save them to a list.

class PageScraper:

  def __init__(self, url):
    self.url = url
    self.parser = ehp.Html()
    self.dom = self.__dom()

  def __dom(self):
    req = requests.get(self.url)
    html = req.text

    dom = self.parser.feed(html)

    return dom
  
  def links(self):
    for link in self.dom.find('a'):
      yield link.attr['href']
    
  def images(self):
    for image in self.dom.find('img'):
      yield image.attr['src']

def main():
  url = 'https://' + input('Enter a URL: https://')
  pageScraper = PageScraper(url)

  links = [i for i in pageScraper.links()]
  images = [i for i in pageScraper.images()]

  with open('links.json', 'r') as f:
    encoded = f.read()

  decoded = json.loads(encoded) if len(encoded) else []
  
  for i in decoded:
    if i['site'] == url:
      return
  
  decoded.append({ 'site': url, 'links': links, 'images': images })
  
  with open('links.json', 'w') as f:
    encoded = json.dumps(decoded, indent=2)

    f.write(encoded)

if __name__ == '__main__':
  main()