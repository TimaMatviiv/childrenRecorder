from django.shortcuts import render

# Create your views here.

def index(request):
	if request.method == "POST":
		
		return render(request, "recorder/index.html", context={"result": request.POST["username"]})

	return render(request, "recorder/index.html", context={"result": "error"})

