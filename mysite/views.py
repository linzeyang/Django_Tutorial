from django.shortcuts import render_to_response

def start(request):
	return render_to_response('start.html')