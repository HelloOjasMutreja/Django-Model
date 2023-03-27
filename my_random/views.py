from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

queries = [
    {'id':1, 'name':'Lets try'},
    {'id':2, 'name':'Lets sing'},
    {'id':3, 'name':'Lets dance'},
]

def home(request):
    context = {'queries': queries}
    return render(request, 'my_random/home.html', context)    
# end def
def query(request, pk):
    query = None
    for i in queries:
        if i['id'] == int(pk):
            query = i

    context = {'query': query}
    return render(request, 'my_random/query.html', context)     
# end def