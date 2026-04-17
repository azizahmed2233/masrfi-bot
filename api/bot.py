from http.server import BaseHTTPRequestHandler
import requests
from bs4 import BeautifulSoup
import json

# --- ضع بياناتك الحقيقية هنا ---
TOKEN = "8174849194:AAEpILwIDT6c04y4ysYgYG5T
CfuidMwOKjo"
CHAT_ID = "8665814266"

def get_data():
    try:
        url = "https://www.masrfi.net/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "موقع مصرفي"
        return f"✅ تم فحص الموقع بنجاح.\nالموقع المكتشف: {title}\nالبوت يعمل الآن!"
    except Exception as e:
        return f"❌ خطأ في الاتصال بالموقع: {str(e)}"

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        result = get_data()
        send_msg(result)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("Done! Check your Telegram.".encode())
