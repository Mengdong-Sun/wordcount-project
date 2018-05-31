from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = dict()

    for word in wordlist:
        if word in worddict:
            #Increse number
            worddict[word] += 1
        else:
            #Add to dict
            worddict[word] = 1
    sorteddict = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sorteddict': sorteddict})

def about(request):
    return render(request, 'about.html')
