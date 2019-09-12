import os
import random, json

PRETVORBA = 'stanje.txt'

class Model:
    def __init__(self):
        self.seznam = []
        self.osvezi_seznam()

    def vnesi_valuto(self, podatki):
        podatki = '{}, {}, {}\n'.format(podatki.get('datum'), podatki.get('koliko EUR'), podatki.get('stevilo'), podatki.get('valuta'))
        with open(PRETVORBA, 'a') as data:
            data.write(podatki)
        self.seznam.append(podatki)

    def razveljavi(self):
        if os.stat(PRETVORBA).st_size != 0:
            self.seznam = self.seznam[:-1]
            lines = self.seznam
            with open(PRETVORBA,'w') as zgo:
                zgo.writelines([item for item in lines]) 
