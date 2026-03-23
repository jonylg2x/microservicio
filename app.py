from flask import Flask, jsonify , request

app =Flask(__name__)
@app.route('/api/sumar', methods=['POST'])

##API basica para ilustrar el funcionamiento de un request http
