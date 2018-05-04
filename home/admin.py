from django.contrib import admin
from .models import Contact, Post
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name',
					'email',
					'message')


@admin.register(Post)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('title',
					'date')
