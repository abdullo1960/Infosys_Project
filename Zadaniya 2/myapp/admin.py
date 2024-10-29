from django.contrib import admin

from myapp.models import MessageModel, Testimonial, TeamModel

# Register your models here.

admin.site.register(MessageModel)
admin.site.register(Testimonial)
admin.site.register(TeamModel)