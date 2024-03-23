from flask import Flask, render_template, request
import requests

application = Flask(__name__)

def get_location(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    data = response.json()
    if data['status'] == 'success':
        return f"{data['city']}, {data['regionName']}, {data['country']}"
    else:
        return "Location not found"

@application.route('/')
def index():
    external_ip = requests.get('https://api.ipify.org').text
    
    user_external_ip = request.access_route[0]

    # Получение локации пользователя по внешнему IP-адресу
    user_location = get_location(user_external_ip)

    return render_template('index.html', external_ip=external_ip, 
                           user_external_ip=user_external_ip, 
                           user_location=user_location)

if __name__ == '__main__':
    application.run(debug=True)
