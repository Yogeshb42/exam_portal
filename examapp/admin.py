from django.contrib import admin
from .models import Result, ExamModel, CustomUser

admin.site.register(CustomUser)
admin.site.register(Result)
admin.site.register(ExamModel)
admin.site.site_title = 'Exam Portal'
admin.site.site_header = 'Exam Portal'
