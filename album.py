#versione OOP
import os.path

class Album:

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename) as file:
            carte = {}
            for line in file:
                k, v = line.strip().split(':')
                carte[int(k.strip())] = int(v.strip())
            file.close()
        self.carte = carte

    def shows(self):
        '''mostra l'album'''
        for k in self.carte:
            print("fig. n:", k, "\t", self.carte[k])

    def add_carta(self, k):
        '''aggiunge all'album un'unità della figurina #k'''
        self.carte[k] += 1
        self.write()
        print("Ho aggiunto la figurina #{}, in tutto ne ho {}.".format(k, self.carte[k]))

    def sottrai_carta(self, k):
        '''sottrae all'album un'unità della figurina #k'''

        if self.carte[k] > 1:
            self.carte[k] -= 1
            self.write()
            print("Ho tolto la figurina #{}, in tutto ne ho {}.".format(k, self.carte[k]))
        elif self.carte[k] == 1:
            togliere = input("Abbiamo solo una figurina #{}. Toglierla ugualmente? Y/N ".format(k))
            if togliere.lower() == ("y"):
                self.carte[k] -= 1
                self.write()
                print("Ho tolto l'unica figurina #{} che avevo.".format(k))
            else:
                print("Non ho tolto l'unica figurina #{}".format(k))
        else:
            print("Non è possibile togliere la figurina #{} perché è mancante".format(k))

    def mancanti(self):
        '''ritorna una list delle figurine mancanti'''
        fig_mancanti = []
        for k in self.carte:
            if self.carte[k] == 0:
                fig_mancanti.append(k)
        return fig_mancanti

    def doppioni(self):
        '''ritorna un dict delle figurine di cui abbiamo più di una unità'''
        fig_doppioni = {}
        for k in self.carte:
            if self.carte[k] > 1:
                fig_doppioni[k] = self.carte[k]
        return fig_doppioni

    def write(self):
        '''scrive il filename'''
        elenco = ""
        for k,v in list(self.carte.items()):
            elenco += str(k) + ":" + str(v) + "\n"
        with open(self.filename,"w") as file:
            file.write(elenco)
            file.close()

    def aggiornamento(self):
        """aggiorna l'album"""
        print("Ecco l'album prima di aggiornare:")
        self.shows()
        print('''AGGIUNGI FIGURINE:
                 Scrivi il n. delle figurine da aggiungere separate da spazio,
                 alla fine INVIO''')
        int_list_to_add = string_to_int_list()
        for k in int_list_to_add:
            self.add_carta(k)
        print('''TOGLI FIGURINE:
                 Scrivi il n. delle figurine da togliere separate da spazio,
                 alla fine INVIO''')
        int_list_to_sub = string_to_int_list()
        for k in int_list_to_sub:
            self.sottrai_carta(k)
        print("Ecco l'album dopo l'aggiornamento:")
        self.shows()
        print("Figurine mancanti: ", self.mancanti())
        print("Figurine doppie o multiple: ", self.doppioni())

# per inizializzare un album, scrivendo il file
def crea_file(filename, n_figurine):
    procedere = not(os.path.exists(filename))
    if os.path.exists(filename):
        sovrascrivere = input(f"Il file {filename} esiste già. Sovrascriverlo? Y/N ")
        if sovrascrivere.lower() == ("y"):
            procedere = True
    if procedere:
        testo_file = ""
        for i in range(n_figurine):
            testo_file = testo_file + f"{i+1}:0\n"
        with open(filename,"w") as file:
            file.write(testo_file)
            file.close()
            print("Creato l'album {} composto da {} figurine".format(filename, n_figurine))
    else:
            print("Non è stato creato nessun nuovo album")

def string_to_int_list():
    string = input('> ')
    string_list = string.split()
    int_list = []
    for item in string_list:
        int_list.append(int(item))
    return int_list
