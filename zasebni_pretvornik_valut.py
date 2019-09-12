import model
import bottle
from bottle import route, run, Response, template

app = bottle.default_app()

pretvornik = model.Model()

@route('/')
def password():
    return bottle.template('prvi zavihek.html')

@bottle.post('/')
def nadaljuj():
    poskus = bottle.request.forms.get('PIN')
    if pretvornik.koda(poskus) == True:
        return bottle.template('pretvornik valut.html', rezultat = '')
    else:
         return bottle.template('prvi zavihek.html')


@bottle.post('/pretvornik_valut/')
def vnesi():
    pretvornik.vnesi_podatke({'datum': bottle.request.forms.get('datum'), 'koliko EUR': bottle.request.forms.get('koliko EUR'), 'valuta': bottle.request.forms.get('valuta')} )
    rezult = pretvornik.racunanje()
    return bottle.template('pretvornik valut.html', rezultat = rezult)




@bottle.get('/reset/')
def razveljavi():
    return bottle.template('pretvornik valut.html')



@bottle.post('/zgodovina/')
def zgodovina():
    return bottle.template('zgodovina.html')

bottle.run(reloader=True, debug=True)