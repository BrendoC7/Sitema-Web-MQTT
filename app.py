from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/status')
def status():
    return "<h2>Status do Broker: Online</h2>"  # Você pode substituir por um render_template se tiver um HTML

if __name__ == '__main__':
    app.run(debug=True)
