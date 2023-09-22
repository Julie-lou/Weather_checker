from weather_check import get_weather
from pyfiglet import figlet_format
import requests
# your code here!
print('--------------------------------------------------')
print('               ⛧°｡⋆༺♱༻⋆｡°⛧')
print('Welcome to weather forcasting app!⛅  🌞  ⛈️   🌩️')
print('-------------------------------------------------')

api_key = 'b2c6fa006e10994755ee5c7ebefeeaf6'
endpoint = "https://openweathermap.org"
a = True
b = False
while a == True:
    city = input("Enter a city or country: ")
    def get_weather():
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}')
        if r.json()['cod'] == '404':
            print(figlet_format('Invalid   city   name', font = 'standard'))
            print('-----------------------------------------------')
            print('❗Please make sure to enter a correct city name❗')
            print('-----------------------------------------------')
            
        else:
            weather = r.json()['weather'][0]['main']
            temp = r.json()['main']['temp']
            print('-------------------------------------------------')
            print(f'------->The weather in {city} is {weather}      ')
            print(f'------->The temperature in {city} is {temp} °F  ')
        
    
            if weather == 'Clouds':
                print('It is a Cloudy day ⛅🌂❗')
                print(figlet_format('Prepare   your   umbrella  !  !', font = 'standard'))
            elif weather == 'Sunny' or weather =='Sun':
                print('It is a Sunny day! 🌞🕶️🧴 ')
                print(figlet_format('Apply   your   sunscreen,   always  !  !', font ='standard'))
            elif weather == 'Rain' or weather == 'Rainy':
                print('It is a Rainy day! ⛈️🌂💧')
                print(figlet_format('Don''t   forget   to   bring   your   umbrella  !  !', font = 'standard'))
            elif weather == 'Clear':
                print('Today the weather is GREAT!😎🏖️ ')
                print(figlet_format('Go   out   and   have   fun  !  ! ', font= 'standard'))
            elif weather == 'Storms' or weather == 'Thunderstorm':
                 print('It is rain storming today!!🌩🌪 ⚡️ ')
                 print(figlet_format('Better   not   going   out   today  !  !', font ='standard'))
    get_weather()
    a == False
    decision = input('Do you want to continue?(y/n): ')
    if decision == 'y':
          a == True
    else:
          print(figlet_format('Thank   You, Have   a   nice   day  !', font = 'standard'))
          break
    
     

