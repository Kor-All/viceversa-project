from django.shortcuts import render

def myhome(request):
	return render(request, 'myhome.html')