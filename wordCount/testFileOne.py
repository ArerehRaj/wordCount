from django.http import HttpResponse
from django.shortcuts import render
import operator

# run the server --> python manage.py runserver
def homePageRequest(request):
    return render(request,'home.html',{'variable':'Key --> Raj Here'})
    # return HttpResponse('<h2>Hello Dear User</h2>')

def userNameRequest(request):
    return HttpResponse('<h1>Hello user with username : Are_Reh_Raj !!!</h1>')

def count(request):
    text = request.GET['userText']
    wordlist = text.split()
    emptyDict = {}

    for word in wordlist:
        if word in emptyDict:
            emptyDict[word] += 1
        else:
            emptyDict[word] = 1
    
    sortedList = sorted(emptyDict.items(),key = operator.itemgetter(1),reverse = True)
    return render(request,'count.html',{'text':text,'count':len(wordlist),'sorted':sortedList})

def about(request):
    age = 18
    gender = 'Male'
    return render(request,'about.html',{'age':age,'gender':gender})