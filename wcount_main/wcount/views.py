from django.http import HttpResponse
from django.shortcuts import render

#empty one
def home(request):
	return HttpResponse('yaruda ivan slow ah..')
	#return render(request,'homepage')

def aboutPage(request):
	#return HttpResponse('ada nanthan ba ipothaiku aboutPage')
	return render(request,'about.html')

def newpage(request):
	#return HttpResponse('idhula pudhusu vera')
	matteru_pass= request.GET['matteru']
	mlist=matteru_pass.split()

	separate_count={}

	for loop in mlist:
		if loop in separate_count:
			separate_count[loop]+=1
		else:
			separate_count[loop]=1

	return render(request,'newpage.html',{'matteru':matteru_pass,'count':len(matteru_pass),'separate_count':separate_count})

def thakaliPage(request):
	return render(request,'thakali.html')
