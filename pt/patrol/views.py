from django.shortcuts import render
from . import functions


# функция отображения html-страниц
def home(request):
    functions.close_connection()

    if request.POST:
        error = functions.connection_ssh(request)
        if error != "":
            return render(request, 'home.html', {'error': error})
        else:
            args = functions.detect()
            return render(request, 'info.html', args)
    return render(request, 'home.html')

