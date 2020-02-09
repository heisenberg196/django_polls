from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, q_id):
    return HttpResponse("You are looking at question %s"  %q_id)

def results(request, q_id):
    response = "You are looking at result for Question  %s"
    return HttpResponse(response %q_id)

def vote(request, q_id):
    return HttpResponse("You are voting for question %s" %q_id)

