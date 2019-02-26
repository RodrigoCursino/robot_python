from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

urlNota  = "https://www.nfp.fazenda.sp.gov.br/login.aspx"
urlTeste = "http://gravidanza.tmsites.com.br/"

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(ChromeDriverManager().install())

USER     = "21242425802"
PASSWORD = "050579"

browser.get(urlTeste)
print(browser.title)
#print(browser.find_element_by_name('ctl00$ConteudoPagina$Login1$UserName').send_keys('UserName'))
# assert "La Gravidanza" in browser.title
# browser.find_element_by_name("div")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in browser.page_source
# browser.close()
