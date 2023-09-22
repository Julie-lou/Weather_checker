import requests
# from pyfiglet import figlet_format


api_key = 'b2c6fa006e10994755ee5c7ebefeeaf6'
endpoint = "https://openweathermap.org"

# r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=london&units=imperial&APPID=b2c6fa006e10994755ee5c7ebefeeaf6')

def get_weather(city):
    # city =('Enter a city: ')
    # r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}')
    r = requests.get(f'{endpoint}/data/2.5/weather?q=London&units=imperial&APPID=b{api_key}')
    return r.json()
# print(get_weather(city))

    

    
    
 

   




 

    



    
    
 
'''
    this function should return data 
    requested from https://api.openweathermap.org/data/2.5/weather

    '''
    # your code here!


