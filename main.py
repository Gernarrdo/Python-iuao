# Import
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variabili che consentono di calcolare il consumo energetico degli apparecchi
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La prima pagina
@app.route('/')
def index():
    return render_template('index.html')
# La seconda pagina
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# La terza pagina
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Calcolo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Il modulo
@app.route('/form')
def form():
    return render_template('form.html')

#I risultati del modulo
@app.route('/submit', methods=['POST'])
def submit_form():
    # Dichiarare le variabili per la raccolta dei dati
    name = request.form['name']

    # È possibile salvare i dati o inviarli via e-mail
    return render_template('form_result.html', 
                           # Inserire le variabili qui
                           name=name,
                           )

app.run(debug=True)

def submit_form(form_data, filename="form.txt"):
    
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            for key, value in form_data.items():
                f.write(f"{key}: {value}\n")
            f.write("\n")  # Aggiunge una riga vuota tra le voci del modulo
        print("Modulo salvato con successo.")
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")

# Esempio di utilizzo
form_data = {
    "Nome": "Gianmpier Fabrizio",
    "Email": "giampier.fabrizio@example.com",
    "Messaggio": "Vorrei maggiori informazioni sui vostri servizi."
}

submit_form(form_data)
