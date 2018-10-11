# versione non OOP

import os.path

def crea_file(filename, n_figurine): # parametri: nome del file da creare,numero di figurine complessivo
    if os.path.exists(filename):           # controllo se il file esiste per non sovrascrivere il file esistente
        sovrascrivere = input(f"Il file {filename} esiste già. Sovrascriverlo? Y/N ")
        if sovrascrivere.lower() == ("y"):
            testo_file = ""
            for i in range(n_figurine):
                testo_file = testo_file + f"{i+1}:0\n"
            target = open(filename, 'w')
            target.write(testo_file)
            target.close()
            print(f"Creato l'album {filename} con {n_figurine}")
        else:
            print(f"Uscita senza sovrascrivere l'album {filename}")

def forma_dictionary(filename):   # ritorna un dictionary dal file
    target = open(filename, 'r')
    dict = {}
    for line in target:
        k, v = line.strip().split(':')
        dict[int(k.strip())] = int(v.strip())
    target.close()
    return dict

def aggiungi_fig(k, dict):
    dict[k] += 1
    print(f"In tutto ho {dict[k]} fig numero {k}.")
    return dict

def sottrai_fig(k, dict):
    if dict[k] > 0:
        dict[k] -= 1
        print(f"Mi sono rimaste {dict[k]} fig numero {k}.")
    else:
        print(f"Non sono presenti figurine n. {k}")
    # TODO: aggiungere controllo se ho una sola figurina di quel numero. Voglio toglierla ugualmente? Y/N

    return dict

def mancanti(dict):
    fig_mancanti = []
    for k in dict:
        if dict[k] == 0:
            fig_mancanti.append(k)
    return fig_mancanti

def doppioni(dict):
    fig_doppioni = {}
    for k in dict:
        if dict[k] > 1:
            fig_doppioni[k] = dict[k]
    return fig_doppioni

def aggiorna(filename):
    print("Ecco l'album prima di aggiornare:")
    dict = view_album(filename)
    print()
    print("AGGIUNGI FIGURINE")
    int_list_to_add = string_to_int_list()
    for k in int_list_to_add:
        dict = aggiungi_fig(k, dict)

    print()
    print("TOGLI FIGURINE")
    int_list_to_sub = string_to_int_list()
    for k in int_list_to_sub:
        dict = sottrai_fig(k, dict)
    # trasformo il dict in stringa
    elenco = ""
    for k in dict:
        elenco = elenco + str(k) + ":" + str(dict[k]) + "\n"
    # print("elenco: ", elenco)

    target = open(filename, 'w')
    target.write(elenco)
    target.close()
    print("Aggiornamento effettuato")
    print("Ecco l'album dopo l'aggiornamento:")
    dict = view_album(filename)
    print("Figurine mancanti: ", mancanti(dict))
    print("FIgurine doppie o multiple: ", doppioni(dict))


def view_album(filename):
    dict = forma_dictionary(filename)
    for k in dict:
        print("fig. n:", k, "\t", dict[k])
    return dict

def string_to_int_list():
    print("Scrivi il n. delle figurine separate da spazio, alla fine INVIO")
    string = input('> ')
    string_list = string.split()
    int_list = []
    for item in string_list:
        int_list.append(int(item))
    return int_list

aggiorna("fig.txt")
# crea_file("fig.txt",10)
