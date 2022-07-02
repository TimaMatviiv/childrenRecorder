from django.shortcuts import render
from .models import Child

import os

# Create your views here.

def index(request):
	users = Child.objects.all()
	context = {
		"users": users
	}
	
	return render(request, "recorder/index.html", context=context)


def add_child(request):
	first_name = ""
	last_name = ""
	village = ""
	ended_class = ""
	parent_name = ""
	parent_phone_number = ""
	health_problems = ""

	if request.method == "POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		village = request.POST["village"]
		ended_class = request.POST["ended_class"]
		parent_name = request.POST["parent_name"]
		parent_phone_number = request.POST["parent_phone_number"]
		health_problems = request.POST["health_problems"]

		message_text = ""
		if not first_name:
			message_text = "Введіть будь ласка ім'я!"
		elif not last_name:
			message_text = "Введіть будь ласка прізвище"
		elif not village:
			message_text = "Введіть будь ласка місце проживання!"
		elif not ended_class:
			message_text = "Введіть будь ласка який клас закінчила дитина!"
		elif not parent_name:
			message_text = "Введіть будь ласка ім'я батьків!"
		elif not parent_phone_number:
			message_text = "Введіть будь ласка номер телефону батьків!"

		if message_text:
			context = {
				"message": True,
				"class": "danger",
				"message_text": message_text,
				"first_name": first_name,
				"last_name": last_name,
				"village": village,
				"ended_class": ended_class,
				"parent_name": parent_name,
				"parent_phone_number": parent_phone_number,
				"health_problems": health_problems
			}

			return render(request, "recorder/add.html", context=context)

		child = Child(
			first_name = first_name,
			last_name = last_name,
			village = village,
			ended_class = ended_class,
			parent_name = parent_name,
			parent_phone_number = parent_phone_number,
			health_problems = health_problems
		)
		child.save()

		first_name = ""
		last_name = ""
		village = ""
		ended_class = ""
		parent_name = ""
		parent_phone_number = ""
		health_problems = ""
		
		context = {
			"message": True,
			"class": "success",
			"message_text": "Успішно додано!"
		}

		os.system("git add .")
		os.system("git commit -am 'update db'")
		os.system("git push")
		return render(request, "recorder/add.html", context=context)
	return render(request, "recorder/add.html", context={"message": False})
