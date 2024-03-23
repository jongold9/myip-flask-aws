from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/')
def index():
    # Получение IP-адреса посетителя
    ip_address = request.headers.get('X-Forwarded-For')
    return render_template('index.html', ip_address=ip_address)

if __name__ == '__main__':
    application.run(debug=True)
