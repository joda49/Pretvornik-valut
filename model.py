import os
import random, json

PRETVORBA = 'pretvorba.txt'

class Model:
    def __init__(self):
        self.seznam = []
        self.koda = ''
        self.osvezi_seznam()

    def vnesi_podatke(self, podatki):
        podatki = '{}, {}, {}, {}\n'.format(podatki.get('datum'), podatki.get('koliko EUR'), podatki.get('stevilo'), podatki.get('valuta'))
        with open(PRETVORBA, 'a') as data:
            data.write(podatki)
        self.seznam.append(podatki)

    def razveljavi(self):
        if os.stat(PRETVORBA).st_size != 0:
            self.seznam = self.seznam[:-1]
            lines = self.seznam
            with open(PRETVORBA,'w') as zgo:
                zgo.writelines([item for item in lines]) 


    def racunanje(self):
        tuja_valuta = self.seznam[1]
        if self.seznam[:-1] == 'USD':
            tuja_valuta = self.seznam[1] * 1.1135
        elif self.seznam[:-1] == 'HRK':
            tuja_valuta = self.seznam[1] * 7.4795
        elif self.seznam[:-1] == 'GBP':
            tuja_valuta = self.seznam[1] * 0.9055
        elif self.seznam[:-1] == 'HUF':
            tuja_valuta = self.seznam[1] * 336.17
        elif self.seznam[:-1] == 'JPY':
            tuja_valuta = self.seznam[1] * 120.91
        elif self.seznam[:-1] == 'RSD':
            tuja_valuta = self.seznam[1] * 119.55
        elif self.seznam[:-1] == 'BTC':
            tuja_valuta = self.seznam[1] * 9149.14
        return tuja_valuta

    def opozorila(self):
        datum1 = self.seznam[0].split('.')
        if len(datum1) != 3:
            for i in datum1:
                if i.isdigit() == False:
                    return 'Popravi datum'
        if self.seznam[1].isdigit() == False:
            return 'Popravi stevilo evrov'
        else:
            pass
    
    def prikaz_zgo(self):
        zgo = self.seznam[-10:]
        if len(zgo) < 10:
            zgo = [', , , ',', , , ',', , , ',', , , ',', , , '] + zgo
        return zgo

    def osvezi_seznam(self):
        self.seznam = []
        try:
            if os.stat(PRETVORBA).st_size != 0:
                with open(PRETVORBA) as zgodovina:
                    for vrstica in zgodovina:
                        self.seznam.append(vrstica)
        except:
            f = open(PRETVORBA, "w+")
            print('Ustvarjena nova datoteka')
            f.close()

    
    def koda(self):
        if self.koda != '0000':
            return 'Napacno geslo'
        else:
            pass