from flask import Flask, render_template, request, jsonify
import json 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renderiza la plantilla HTML

def home2():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
