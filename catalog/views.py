from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ToDoForm as form
import json

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request,'index.html' ,{'form': form()})
    elif request.method == 'POST':
        return redirect("next/")
    return render(request,'index.html' ,{'form': form()})
def next(request):
    if request.method == 'GET':
        return render(request,'next.html',{'clue':"Bem então vamos começar:\n As vezes algumas “mensagens” que nos fazem lembrar de algo/alguem podem vir de onde menos esperamos:", "clue1":"Dica: Talvez de uma música vinda do Brasil",'form': form()})
    else:
        try:
            f=form(request.POST)
            code= f.save(commit=False)
            codigo=code.code.lower()
            if(codigo=="será que um dia"):
                code.save()
                return redirect('mallu')
        except ValueError:
            return render(request,'next.html',{'clue':"Bem então vamos começar:\n As vezes algumas “mensagens” que nos fazem lembrar de algo/alguem podem vir de onde menos esperamos:","clue1":"Dica: Talvez de uma música vinda do Brasil",'form': form()})
    return  render(request,'next.html',{'clue':"Bem então vamos começar:\n As vezes algumas “mensagens” que nos fazem lembrar de algo/alguem podem vir de onde menos esperamos:","clue1":"Dica: Talvez de uma música vinda do Brasil",'form': form()})

def mallu(request):
    if request.method == 'GET':
        return render(request,'next.html',{'clue':"Bem erro meu,\n todos sabemos que talvez a cor do site não seja a tua favorita. No entanto, era a que achei que ficasse melhor","clue1":'Dica: Lembra te de ser "bué international"','form': form()})
    else:
        try:
            f=form(request.POST)
            f.save(commit=False).user = request.user
            code= f.save(commit=False)
            codigo=code.code.lower()
            if(codigo=="blue"):
                code.save()
                return redirect('blue')
        except ValueError:
            return render(request,'next.html',{'clue':"Bem erro meu,\n todos sabemos que talvez a cor do site não seja a tua favorita. No entanto, era a que achei que ficasse melhor","clue1":'Dica: Lembra te de ser "bué international"','form': form()})
    return  render(request,'next.html',{'clue':"Bem erro meu,\n todos sabemos que talvez a cor do site não seja a tua favorita. No entanto, era a que achei que ficasse melhor","clue1":'Dica: Lembra te de ser "bué international"','form': form()})


def blue(request):
    if request.method == 'GET':
        return render(request,'next.html',{'clue':"Visto que já que chegaste aqui, decidi fazer uma playlist para ti :).Ouve um pouco dela enquanto estas a recuperar o folgo,pois já te esforçaste imenso, e enquanto tentas descobrir a solução para a charada.Pensei que era uma exelente ideia que a charada fosse sobre o ar,pois nitidamente deves estar com falta dele :)).A Charada é a seguinte:\nQual ar é o mais caro?","link": "https://open.spotify.com/playlist/1vMiE1aERAZCL5nenuCMFg?si=9d40c0d2e1894ff1&pt=450f99639e97adab17dd1dc7312585b2","clue1":'"But I crumble completely when you cry"','form': form()})
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
            return render(request,'next.html',{'clue':"Bem já que chegaste aqui ,fiz uma playlist para ti espero que gostes e que ajude a descobrir a resolver a proxima charada e a recuperar o folgo,pois a nitidamente a menina a esta altura já deve estar sem ar xD.Por isso,a charada é sobre o ar:\nQual ar é o mais caro?","clue1":'"But I crumble completely when you cry"',"link": "https://open.spotify.com/playlist/1vMiE1aERAZCL5nenuCMFg?si=9d40c0d2e1894ff1&pt=450f99639e97adab17dd1dc7312585b2",'form': form()})
    return  render(request,'next.html',{'clue':"Bem já que chegaste aqui ,fiz uma playlist para ti espero que gostes e que ajude a descobrir a resolver a proxima charada e a recuperar o folgo,pois a nitidamente a menina a esta altura já deve estar sem ar xD.Por isso,a charada é sobre o ar:\nQual ar é o mais caro?","clue1":'"But I crumble completely when you cry"',"link": "https://open.spotify.com/playlist/1vMiE1aERAZCL5nenuCMFg?si=9d40c0d2e1894ff1&pt=450f99639e97adab17dd1dc7312585b2",'form': form()})

def _505_(request):
    if request.method == 'GET':
        return render(request,'next.html',{'clue':"Espero que saibas tanto eu como a tua irmã gostamos muito de ti.Por isso decidimos ambos em te oferecer o bilhete para o Kalorama onde para poderes ver os Arctic Monkeys :)"})
