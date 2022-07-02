from django.shortcuts import render

import os

# Create your views here.

def index(request):
	if request.method == "POST":
		os.system("git add .")
		os.system("git commit -am 'add new child'")
		os.system("git push")
		return render(request, "recorder/index.html", context={"result": request.POST["first_name"]})

	return render(request, "recorder/index.html", context={"result": "error"})

