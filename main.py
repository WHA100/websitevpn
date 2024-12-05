from flask import Flask, render_template, request, redirect, make_response, url_for
import threading
import requests

app = Flask(__name__)

# Тексты для разных языков
LANGUAGES = {
    "en": {
        "why_choose": "Why Choose LynxVPN?",
        "lightning_fast": "Lightning Fast",
        "lightning_fast_desc": "Move at the speed of a lynx with optimized servers worldwide.",
        "security": "Top-Notch Security",
        "security_desc": "State-of-the-art encryption for unbeatable safety.",
        "no_logs": "No Logs Policy",
        "no_logs_desc": "Your data is your business – we keep it that way.",
        "servers": "Our Global Server Locations",
        "servers_desc": "Enjoy lightning-fast connections with servers in:",
        "contact_us": "Contact us",
        "email": "support@lynxvpn.com",
        "copyright": "© 2024 LynxVPN. All Rights Reserved.",
        "language": "Language"
    },
    "ru": {
        "why_choose": "Почему выбрать LynxVPN?",
        "lightning_fast": "Молниеносная скорость",
        "lightning_fast_desc": "Работайте со скоростью рыси благодаря оптимизированным серверам по всему миру.",
        "security": "Высокий уровень безопасности",
        "security_desc": "Современное шифрование для непревзойденной защиты.",
        "no_logs": "Политика без логов",
        "no_logs_desc": "Ваши данные — это только ваше дело, и мы это уважаем.",
        "servers": "Наши серверы по всему миру",
        "servers_desc": "Наслаждайтесь сверхбыстрыми соединениями с серверами в:",
        "contact_us": "Свяжитесь с нами",
        "email": "support@lynxvpn.com",
        "copyright": "© 2024 LynxVPN. Все права защищены.",
        "language": "Язык"
    }
}

@app.route("/")
def home():
    # Определяем язык из cookie (по умолчанию "en")
    lang = request.cookies.get("lang", "en")
    return render_template("index.html", lang=lang, texts=LANGUAGES[lang])

@app.route("/set_language/<lang>")
def set_language(lang):
    if lang not in LANGUAGES:
        lang = "en"  # Если язык некорректен, ставим "en"
    resp = make_response(redirect(url_for("home")))
    resp.set_cookie("lang", lang, max_age=60*60*24*365)  # Запоминаем язык на год
    return resp

def ping():
    """Функция для поддержания активности сервера на Render."""
    threading.Timer(49, ping).start()  # Запускаем каждые 49 секунд
    try:
        # Замените на ваш реальный URL сайта на Render
        requests.get("https://<your_render_url>")
    except requests.exceptions.RequestException:
        pass

# Запускаем фоновый пинг при старте приложения
ping()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

