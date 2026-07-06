from flask import Flask, render_template, send_from_directory
from PIL import Image
import os
import warnings
try:
    from openai import OpenAI
    openai_available = True
except ImportError:
    OpenAI = None
    openai_available = False
    print("Warning: openai package not installed. Install it with: pip install openai")

from flask import Flask, send_from_directory, request, jsonify, send_file

# create a single Flask app instance (avoid reassigning later)
app = Flask(__name__)

api_key = (
    os.environ.get('OPENAI_API_KEY')
    or os.environ.get('OPENAI_ADMIN_KEY')
    or os.environ.get('DEEPSEEK_API_KEY')
    or os.environ.get('API_KEY')
)

client = None
if api_key:
    if openai_available:
        try:
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.deepseek.com")

            response = client.chat.completions.create(
                model="deepseek-v4-pro",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant Développeur Full-Stack Formateur support IT Agent IA actif"},
                    {"role": "user", "content": "Agis en tant que développeur senior en React, Python, JavaScript, Java, HTML, PHP et TypeScript."},
                    {"role": "technical", "content": "Utilise Next.js 15, Tailwind CSS, Materialiaze, Bootstrap et Zod"},
                ],
                stream=False,
                reasoning_effort="high",
                technical_skills="high",
                extra_body={"thinking": {"type": "enabled"}}
            )

            print(response.choices[0].message.content)
        except Exception as e:
            print("Warning: appel OpenAI échoué:", e)
    else:
        print("Warning: openai package not installé. Install it avec: pip install openai")
else:
    print(
        "Warning: aucune clé API trouvée. Définissez OPENAI_API_KEY, OPENAI_ADMIN_KEY, DEEPSEEK_API_KEY ou API_KEY."
    )


@app.route('/')
def index():
    return send_from_directory(os.path.dirname(__file__), 'index.html')


@app.route('/training', methods=['GET', 'POST'])
def training():
    if request.method == 'POST':
        return jsonify({"message": "Bienvenue! Le module de formation DevOps Full-stack va bientôt être disponible."})
    # GET: servir la page training.html située dans le même dossier que ce script
    return send_from_directory(os.path.dirname(__file__), 'training.html')


@app.route('/demonstrations')
def demonstrations():
    return send_from_directory(os.path.dirname(__file__), 'demonstrations.html')

@app.route('/widget')
def widget():
    return send_from_directory(os.path.dirname(__file__), 'widget.html')


@app.route('/resources/practika')
def practika_resource():
    pdf_path = "/home/mercipowerhouse/Bureau/kamilou_DocPostulation/documentationsrvCaméra02final.pdf"
    return send_file(pdf_path, as_attachment=False, mimetype='application/pdf')


@app.route('/assistant', methods=['POST'])
def assistant():
    data = request.get_json(silent=True) or {}
    question = (data.get('question') or '').strip()
    if not question:
        return jsonify({
            'answer': 'Posez une question pour recevoir une ressource ou un cas pratique.'
        })

    if client:
        try:
            response = client.chat.completions.create(
                model='deepseek-v4-pro',
                messages=[
                    {'role': 'system', 'content': 'Vous êtes un assistant de formation DevOps Full-stack. Répondez avec des ressources pratiques et des cas concrets.'},
                    {'role': 'user', 'content': question},
                ],
                stream=False,
                reasoning_effort='high',
                technical_skills='high',
                extra_body={'thinking': {'type': 'enabled'}}
            )
            return jsonify({'answer': response.choices[0].message.content})
        except Exception as e:
            print('Warning: appel OpenAI échoué:', e)

    return jsonify({
        'answer': (
            'Je ne peux pas accéder à l’API externe pour l’instant. ' \
            'Posez une question comme "Comment créer un pipeline CI/CD ?" ou ' \
            '"Quelle ressource pour apprendre Kubernetes ?"'
        )
    })


if not api_key:
    warnings.warn(
        'Aucune clé API OpenAI/Deepseek trouvée. Exportez OPENAI_API_KEY, OPENAI_ADMIN_KEY, DEEPSEEK_API_KEY ou API_KEY.'
    )

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PROCESSED_FOLDER'] = 'static/images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Créer les dossiers s'ils n'existent pas
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def process_image(input_path, output_path):
    """Exemple de traitement d'image avec PIL"""
    with Image.open(input_path) as img:
        # Créer une miniature
        img.thumbnail((300, 300))
        img.save(output_path)
        return True
    return False

# @app.route('/')
# def demonstrations():
#     return render_template('demonstrations.html')

@app.route('/process', methods=['POST'])
def process_uploaded_image():
    # Ici vous ajouteriez la logique pour traiter les images uploadées
    pass

# -------------------------------------------------------------------
# 2) Flask
# -------------------------------------------------------------------
# (L'instance `app` est déjà créée en haut du fichier)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)