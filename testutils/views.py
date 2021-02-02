# i have created this file'
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

    
def analyze(request):
    # get the text 
    djtext = request.POST.get('text','default')
    
    # check values of checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

   
    if removepunc== "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params= {'purpose':'Removed Punctuations','analyzed_text' : analyzed }
        djtext= analyzed
     
    
    if fullcaps =="on":
        analyzed=""
        analyzed= djtext.upper()
        params= {'purpose':'Capitalized Text','analyzed_text' : analyzed }
        djtext= analyzed

    
    if newlineremove =="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed= analyzed+char
        params= {'purpose':'Removed Newlines','analyzed_text' : analyzed }
        djtext= analyzed       

    
    if spaceremover =="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params= {'purpose':'Removed Extra Space','analyzed_text' : analyzed } 

 
    if removepunc != "on" and fullcaps != "on" and newlineremove != "on" and spaceremover != "on":
        return HttpResponse("Error")


    return render(request, 'analyze.html',params )