from flask import Flask, render_template
import requests
from dotenv import load_dotenv, dotenv_values
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

metaData= MetaData()

cities= Table('Cities', metaData, 
            Column ('id', Integer(),primary_key=True, autoincrement=True),
            Column('nombre', String(100), unique=True)
             )
#config= dotenv_values('.env')
#app= Flask(__name__)
#engine= create_engine('sqlite:///weather.db')

config = dotenv_values('.env')
 
app=Flask(__name__)

def get_weather_data(city):
    API_KEY= config['API_KEY']
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=es&units=metric'
    r = requests.get(url).json()
    print(r)
    return r

@app.route('/prueba')
def prueba():
    clima= get_weather_data('cuenca')
    temperatura=str(clima['main']['temp'])
    descripcion=str(clima['weather'][0]['description'])
    icono=str(clima['weather'][0]['icon'])

    r_json={ 
        'ciudad':'cuenca',
        'temperatura': temperatura,
        'descripcion':descripcion,
        'icono':icono}
    return render_template('weather.html',clima= r_json)
    

@app.route('/about')
def about():
    return render_template('MI_CV.html')


@app.route('/clima')
def clima():
    return 'Obten todo sobre el clima'

if __name__ == '__main__':
    app.run(debug=True)
