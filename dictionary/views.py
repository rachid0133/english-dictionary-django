from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.

def index(request):
    return render(request,'index.html')

def word(request):
    search = request.GET.get('search0')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonym = dictionary.synonym(search)
    antonym = dictionary.antonym(search)
    # if meaning.keys()=='Noun':
    #     meaning=meaning['Noun']
    # elif meaning.keys()=='Verb':
    #     meaning = meaning['Verb']
    context = {
        'meaning': meaning,
        'synonym': synonym,
        'antonym': antonym
    }
    return render(request, 'word.html', context)