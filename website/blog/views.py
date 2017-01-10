from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader,Context
from django.shortcuts import render_to_response

'''
def index(req):
    t = loader.get_template('index1.html')
    c = Context({})
    return HttpResponse(t.render(c))

'''
book_list = ['pyth','abc','java']

def abc(req):
    return render_to_response('index1.html',{'book_list':book_list})



    # Create your views here.
