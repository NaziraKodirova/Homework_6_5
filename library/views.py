from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def library(request):
    books = [
        {'title': 'O`tkan kunlar', 'author': 'Abdulla Qodiriy'},
        {'title': 'Saodat asri qissalari', 'author': 'Ahmad Lutfiy'},
        {'title': 'Kiprikda qolgan tong', 'author': 'Said Ahmad'},
    ]
    return render(request, 'library/library.html', {'books': books})