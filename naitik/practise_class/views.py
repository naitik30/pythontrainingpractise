# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import student
# Create your views here.
def data_list(request):
	student_data = student..objects.all()
	context = {
		"data": student_data,
    }
	return render(request, "blog.html", context)
