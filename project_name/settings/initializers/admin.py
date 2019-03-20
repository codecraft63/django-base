from django.contrib import admin

# Personalized admin site settings like title and header
admin.site.site_title = "{{ project_name|title }} Admin"
admin.site.site_header = "{{ project_name|title }} Administration"
