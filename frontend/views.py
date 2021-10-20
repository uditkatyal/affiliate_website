from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')

def render_page(request, page_request):
	page_request = page_request.replace(".html", "")

	if page_request == 'favicon.ico':
		return HttpResponse('')

	try:
		return render(request, f'{page_request}.html')
	except:
		return redirect(index)