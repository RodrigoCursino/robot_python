from bs4 import BeautifulSoup
import mechanize

br = mechanize.Browser()
redditFile = br.open("http://gravidanza.tmsites.com.br/")
redditHtml = redditFile.read()
#redditFile.close()

soup = BeautifulSoup(redditHtml,features="html5lib")
redditAll = soup.find_all("form")
for links in soup.find_all('form'):
    print (links.get('action'))