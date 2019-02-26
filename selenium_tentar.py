from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

urlNota  = "https://www.nfp.fazenda.sp.gov.br/login.aspx"
urlTeste = "http://gravidanza.tmsites.com.br/"

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(urlNota)

USER     = "21242425802"
PASSWORD = "050579"

wait = WebDriverWait(browser, 5)

user   = browser.find_element_by_id('UserName').send_keys("21242425802")
passwd = browser.find_element_by_id('Password').send_keys(PASSWORD)

print(user)