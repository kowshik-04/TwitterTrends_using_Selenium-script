from flask import Flask, render_template, jsonify, request
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    result = subprocess.run(['python', 'selenium_script.py'], capture_output=True, text=True)
    try:
        output = json.loads(result.stdout)
    except json.JSONDecodeError:
        output = {'error': 'Failed to decode JSON from script output'}
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
