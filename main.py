from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Скачать приложение
@app.route('/download')
def download():
    return send_from_directory(directory='static', filename='LynxVPN-Setup.exe', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
