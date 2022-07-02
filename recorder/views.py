from django.shortcuts import render
from .models import Child

import os

# Create your views here.

def index(request):
	if request.method == "POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		village = request.POST["village"]
		ended_class = request.POST["ended_class"]
		parent_name = request.POST["parent_name"]
		parent_phone_number = request.POST["parent_phone_number"]
		health_problems = request.POST["health_problems"]

		child = Child(first_name=first_name, 
			last_name=last_name, 
			village=village, 
			ended_class=ended_class, 
			parent_name=parent_name,
			parent_phone_number = parent_phone_number,
			health_problems = health_problems
		)
		child.save()

		os.system("git add .")
		os.system("git commit -am 'add new child'")
		os.system("git push")
		return render(request, "recorder/index.html", context={"result": "alright"})

	return render(request, "recorder/index.html", context={"result": "error"})

