from django.shortcuts import render




# Create your views here.


def turnos(request):

    context ={}

    return render(request, 'turnos/turnos.html', context)