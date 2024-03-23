import requests
from flask import Flask, render_template, request

application = Flask(__name__)

def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except Exception as e:
        print("Error getting external IP:", e)
        return None

@application.route('/')
def index():
    ip_address = get_external_ip()
    return render_template('index.html', ip_address=ip_address)

if __name__ == '__main__':
    application.run(debug=True)
