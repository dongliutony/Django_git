from django.shortcuts import render_to_response, RequestContext

# Create your views here.
def my_view(request):

    a = range(1,10)
    b = 'string'
    c = 2
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))