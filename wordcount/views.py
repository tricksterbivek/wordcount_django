from django.http import HttpResponse
from django.shortcuts import render
import re
import operator

def home(request):
    return render(request,"home.html")

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=re.findall(r'\w+', fulltext)
    worddictinary={}
    for word in wordlist:
        if word in worddictinary:
            worddictinary[word]+=1
        else:
            worddictinary[word]=1
    sortedwords=sorted(worddictinary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,"count.html",{'fulltext':fulltext,'count':len(wordlist),'worddictionary':sortedwords})
