from django.shortcuts import render

def home(request):
    context={
        'name':'Ceyda'
    }
    return render(request, 'pages/home.html', context=context)