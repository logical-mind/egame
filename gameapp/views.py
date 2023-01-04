from django.shortcuts import render


def juego(request):
    return render(request, "juegos.html")  

    
