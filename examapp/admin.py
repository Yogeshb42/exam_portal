from django.contrib import admin
from .models import Result, QuesModel, CustomUser

admin.site.register(CustomUser)
admin.site.register(Result)
admin.site.register(QuesModel)
admin.site.site_title = 'Exam Portal'
admin.site.site_header = 'Exam Portal'
