from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ToDoForm as form
import json

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request,'index.html' ,{'form': form()})
    else:
        try:
            f=form(request.POST)
            code= f.save(commit=False)
            codigo=code.code.lower()
            if(codigo=="será que um dia"):
                code.save()
                print(code.id)
                return redirect('next/')
        except ValueError:
            return render(request,'index.html',{'form': form()})
    return render(request,'index.html' ,{'form': form()})

def next(request):
    if request.method == 'GET':
        return render(request,'next.html',{'clue':"Bem erro meu,\n todos sabemos que talvez a cor do site não seja a tua favorita mas foi a que achei que ficasse mais bonita",'form': form()})
    else:
        try:
            f=form(request.POST)
            f.save(commit=False).user = request.user
            code= f.save(commit=False)
            codigo=code.code.lower()
            if(codigo=="blue" or codigo=="azul"):
                code.save()
                return redirect('blue')
        except ValueError:
            return render(request,'next.html',{'clue':"Bem erro meu,\n todos sabemos que talvez a cor do site não seja a tua favorita mas foi a que achei que ficasse mais bonita",'form': form()})
    return  render(request,'next.html',{'clue':"Bem erro meu,\n todos sabemos que talvez a cor do site não seja a tua favorita mas foi a que achei que ficasse mais bonita",'form': form()})


def blue(request):
    if request.method == 'GET':
        return render(request,'next.html',{'clue':"Bem já que chegaste aqui ,fiz uma playlist para ti ________________espero que gostes e que ajude a descobrir o ultimo codigo",'form': form()})
    else:
        try:
            f=form(request.POST)
            f.save(commit=False).user = request.user
            code= f.save(commit=False)
            codigo=code.code.lower()
            if(codigo=="505"):
                code.save()
                return redirect('_505_')

        except ValueError:
            return render(request,'next.html',{'clue':"Bem já que chegaste aqui ,fiz uma playlist para ti ________________espero que gostes e que ajude a descobrir o ultimo codigo",'form': form()})
    return  render(request,'next.html',{'clue':"Bem já que chegaste aqui ,fiz uma playlist para ti ________________espero que gostes e que ajude a descobrir o ultimo codigo",'form': form()})

def _505_(request):
    if request.method == 'GET':
        return render(request,'next.html',{'clue':"Espero que saibas tanto eu como a tua irmã gostamos muito de ti.Por isso decidimos ambos em te oferecer o bilhete para o Kalorama onde para poderes ver os Arctic Monkeys :)"})
