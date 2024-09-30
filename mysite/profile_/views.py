from django.http import HttpResponse

# Create your views here.
def info_profile(request):
    return HttpResponse("Ciao Valerio, ecco il tuo profilo.")


