from flask import Flask
import random

app = Flask(__name__)
lista_fatti = ["Ciao io sono Mario","Ciao io sono Andrea","Giacomo è vivo ed è fra noi"]

#Nomi
@app.route("/")
def indice():
    return f'<h1>Ciao! Qui trovi gli alunni del corso python pro!</h1><a href="/fatto_casuale">Vedi un fatto casuale!</a>'

#Fatto casuale
@app.route("/fatto_casuale")
def fatti(): 
    return f'<p>{random.choice(lista_fatti)}</p>'

#Testa o Croce
@app.route("/testa_croce")
def lancia_moneta():
    risultato = random.choice(["Testa", "Croce"])
    return risultato
if __name__ == "__main__":
    print("Risultato del lancio della moneta:", lancia_moneta())
