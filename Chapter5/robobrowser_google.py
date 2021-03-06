from robobrowser import RoboBrowser

browser = RoboBrowser(parser='html.parser')

browser.open('https://www.google.com/')

form = browser.get_form(action='/search')
form['q'] = 'Python'
browser.submit_form(form, list(form.submit_fields.values())[0])

for a in browser.select('h3 > a'):
    print(a.text)
    print(a.get('href'))
    print()