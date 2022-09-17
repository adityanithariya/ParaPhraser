from django.shortcuts import render

# Views
def index(request):
	return render(request, "python/index.html")
