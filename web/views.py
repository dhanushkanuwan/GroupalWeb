from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	context = {}
	return render(request, 'web/index.html', context)

def login(request):
	if (request.method == 'POST'):
		username = request.POST['username']
    	password = request.POST['password']
    	user = authenticate(username=username, password=password)
    	if user is not None:
    		login(request, user)
    		# Redirect to 
    else:
    	# Get request
	context = {}
	return render(request, 'web/login.html', context)

def register(request):
	if (request.methosd== 'POST'):

		# Validate the posted fields and register the user.
		return HttpResponseRedirect()

	else:
		# Get request

	return render(request, 'web/register.html', None)

def groups(request):
	return render(request, 'web/groups.html', None)
