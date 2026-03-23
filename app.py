from flask import Flask, jsonify , request

app =Flask(__name__)

#https://API.com/
@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a mi API de MCIB-B"})

@app.route('/api/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    
    if a is None or b is None:
        return jsonify({'error': 'los parámetros a y b deben existir'}), 400
    
    if type(a) != int or type(b) != int:
        return jsonify({'error': 'los parámetros a y b deben ser enteros'}), 400
    
    return jsonify({'resultado': a + b})
@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({'nombre': "Jonathan Solórzano", 
                    'version': "1.0.0"
                    })
if __name__ == '__main__': #esta linea ejecuta la aplicacion cuando yo en terminal haga python app.py
    app.run(debug=True, host='0.0.0.0', port=8080)