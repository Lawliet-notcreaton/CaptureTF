from django.shortcuts import render
from django.db import connection
from .models import Product

# Create your views here.

def index(request):
    return render(request, 'CTF/lessons/sqli_app/index.html')

def search(request):
    query = request.GET.get('query', '')
    if query:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sqli_app_product WHERE name LIKE '%%%s%%'" % query)
        products = cursor.fetchall()
    else:
        products = None
    return render(request, 'CTF/lessons/sqli_app/search.html', {'products': products})