from django.contrib import admin
from ..accounts.models import User
# Register your models here.


class CourseAdminUser(admin.ModelAdmin):
    list_display = ['username','name', 'email','date_joined','alter_date' ]
    search_fields = ['username','name', 'email']
    # formatar o slug
    #prepopulated_fields = {'slug': ('name',)}

admin.site.register(User, CourseAdminUser)