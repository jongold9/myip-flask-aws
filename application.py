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
    # Получение внешнего IP-адреса сервера
    external_ip = requests.get('https://api.ipify.org').text

    # Получение внутреннего IP-адреса сервера
    internal_ip = request.host.split(':')[0]

    # Получение внешнего и внутреннего IP-адреса пользователя
    user_external_ip = request.remote_addr
    user_internal_ip = request.access_route[0]

    # Получение локации пользователя по внешнему IP-адресу
    user_location = get_location(user_internal_ip)

    return render_template('index.html', external_ip=external_ip, internal_ip=internal_ip,
                           user_external_ip=user_external_ip, user_internal_ip=user_internal_ip,
                           user_location=user_location)

if __name__ == '__main__':
    application.run(debug=True)
