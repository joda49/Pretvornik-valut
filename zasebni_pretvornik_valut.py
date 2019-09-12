import model
import bottle
from bottle import route, run, Response, template

app = bottle.default_app()

pretvornik = model.Model()

@route('/')
def password():
    return bottle.template('password.html')

@bottle.post('/')
def nadaljuj():
    pretvornik.koda()
    return bottle.template('pretvornik valut.html')

@bottle.get('/pretvornik valut/')
def vnesi():
    pretvornik.vnesi_podatke({'datum': bottle.request.forms.get('datum'), 'koliko EUR': bottle.request.forms.get('koliko EUR'), 'valuta': bottle.request.forms.get('valuta')} )
    # Tukaj ne vem kaj naj naredim
    bottle.redirect('/')

@bottle.get('/')
def opozorilo():
    pretvornik.opozorila()
    bottle.redirect('/')

@bottle.get('/reset/')
def razveljavi():
    pretvornik.reset_funkcija()
    bottle.redirect('/')

@bottle.get('/izračunaj/')
def racunanje():
    return bottle.template(, koliko EUR = '' )
#Kako se naredi oni drsnik in kako ono polje kamor mi vrže izračun


@bottle.post('/zgodovina/')
def zgodovina():
    pretvornik.prikaz_zgo()
    bottle.redirect('/')

bottle.run(reloader=True, debug=True)







