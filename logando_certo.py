import mechanize
from bs4 import BeautifulSoup

browser = mechanize.Browser()
# browser.addheaders.append(("Accept-Encoding", "gzip, deflate, br"))
# browser.addheaders.append(("Cache-Control", "max-age=0"))
# browser.addheaders.append(("Accept-Language", "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"))
# browser.addheaders.append(("Referer", "https://www.nfp.fazenda.sp.gov.br/login.aspx"))
# browser.addheaders.append(("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"))


urlNota  = "https://www.nfp.fazenda.sp.gov.br/login.aspx"
urlTeste = "http://gravidanza.tmsites.com.br/"



browser.open(urlNota)

# def select_form(form):
#   return form.attrs.get('action', None) == 'http://gravidanza.tmsites.com.br/login'
#
# browser.select_form(predicate=select_form)
#
# browser.form.set_all_readonly(False)
#
# browser.form['email']    = 'admin@admin.com'
# browser.form['password'] = '123456'
#
# browser.submit()

page = BeautifulSoup(browser.response().read(), features="html5lib")

print(page.prettify())