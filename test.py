from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=79454fcdc4618cae64f45852c90a80b1')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    humidity_py = float (json_object['main']['humidity'])
    country_py = json_object['sys']['country']
    #temp_f = float((temp_k - 273.15)) * 1.8 + 32
    temp_c = float(temp_k-273)

    return render_template('temperature.html', temp=temp_c, humidity=humidity_py, country = country_py)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
