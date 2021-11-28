from django.contrib import admin
from django.urls.resolvers import CheckURLMixin
from .models import Books, Customer, UserInput
admin.site.register(UserInput)
admin.site.register(Books)
admin.site.register(Customer)

# Register your models here.
