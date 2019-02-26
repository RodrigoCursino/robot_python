import mechanize
from bs4 import BeautifulSoup

br   = mechanize.Browser()
br.open('http://gravidanza.tmsites.com.br/')
response = br.response()

def select_form(form):
  return form.attrs.get('action', None) == 'http://gravidanza.tmsites.com.br/login'

br.select_form(predicate=select_form)

br.form.set_all_readonly(False)

br.form['email']    = 'admin@admin.com'
br.form['password'] = '123456'

br.submit()



