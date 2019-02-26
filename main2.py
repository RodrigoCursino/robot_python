import mechanize

LOGIN_URL   = 'https://www.nfp.fazenda.sp.gov.br/login.aspx'
USERNAME    = '21242425802'
PASSWORD    = '050579'
SEARCH_URL  = 'http://www.example.com/search?'
FIXED_QUERY = 'food=spam&' 'utensil=spork&' 'date=the_future&'

result_no = 0
br = mechanize.Browser()
br.open(LOGIN_URL)
br.response()

def select_form(form):
  return form.attrs.get('id', None) == 'aspnetForm'

br.select_form(select_form)


