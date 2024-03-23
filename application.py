from flask import Flask, render_template, request
import requests

application = Flask(__name__)

@application.route('/')
def index():
    external_ip = requests.get('https://api.ipify.org').text
    internal_ip = request.host.split(':')[0]
    user_external_ip = request.remote_addr
    user_internal_ip = request.access_route[0]

    return render_template('index.html', external_ip=external_ip, internal_ip=internal_ip,
                           user_external_ip=user_external_ip, user_internal_ip=user_internal_ip)

if __name__ == '__main__':
    application.run(debug=True)
