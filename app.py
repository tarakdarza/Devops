from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Route pour l'ancienne page de logs
@app.route('/logs', methods=['GET', 'POST'])
def show_logs():
    log_lines = []
    with open('log.csv', 'r') as f:
        log_lines = f.readlines()
    return render_template('logs.html', logs=log_lines)

# Nouvelle route pour /logs1 avec un formulaire de filtrage
@app.route('/logs1', methods=['GET', 'POST'])
def show_logs1():
    level_filter = request.form.get('level', 'all')
    log_lines = []
    
    # Lire le fichier de logs et filtrer selon le niveau d'événement
    with open('log.csv', 'r') as f:
        for line in f:
            # Appliquer le filtre si un niveau est sélectionné
            if level_filter == 'all' or level_filter in line:
                log_lines.append(line)
    
    # Envoyer les logs filtrés et le niveau de filtre sélectionné à la page HTML
    return render_template('logs1.html', logs=log_lines, level_filter=level_filter)



@app.route('/results')
def show_results():
    results = {
        "Nombre d'erreurs": 5,
        "Nombre de requêtes GET": 120,
        "Nombre de requêtes POST": 30
    }
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# Ceci est un commentaire de test pour Jenkins