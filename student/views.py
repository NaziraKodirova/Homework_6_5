from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def student(request):
    student = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Alice', 'last_name': 'Johnson'},
    ]
    return render(request, 'student/student.html', {'student': student})
