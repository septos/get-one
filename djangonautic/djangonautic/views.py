from django.http import HttpResponse

#masukan render untuk merender HTML5
from django.shortcuts import render

def homepage(request):
   # return HttpResponse(home)       #bisa memasukan string atau langsung masukan value kedalam ()
   return render(request, 'homepage.html')
def about(request):
   # return HttpResponse('about')
   return render(request, 'about.html')