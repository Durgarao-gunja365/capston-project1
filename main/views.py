from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs.txt')

def log_visit(request, page_name):
    ip = request.META.get('REMOTE_ADDR', 'Unknown IP')
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown Browser')
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"{time} - {ip} - {user_agent} - visited {page_name}\n"

    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_line)


def home(request):
    log_visit(request, "Home Page")
    return render(request, 'home.html')

def contact(request):
    log_visit(request, "Contact Page")
    return render(request, 'contact.html')

def view_logs(request):
    logs_list = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(" - ", 3)  # Limit to 4 parts
                if len(parts) == 4:
                    logs_list.append({
                        'time': parts[0],
                        'ip': parts[1],
                        'browser': parts[2],
                        'page': parts[3],
                    })
    return render(request, 'logs.html', {'logs': logs_list})
