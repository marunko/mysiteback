from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'key')
    search_fields = ('title', 'key')

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'key', 'created_at', 'expires_at', 'is_expired')
    search_fields = ('key',)
    list_filter = ('expires_at',)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'title', 'summary')
    search_fields = ('title', 'text')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'position', 'company', 'start_date', 'end_date', 'reference')
    search_fields = ('position', 'company')
    list_filter = ('start_date', 'end_date')

@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'experience', 'roles')
    search_fields = ('roles',)

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'title')
    search_fields = ('title',)

@admin.register(SkillTag)
class SkillTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill', 'text')
    search_fields = ('text',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'title', 'link')
    search_fields = ('title', 'text')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'title', 'summary', 'link')
    search_fields = ('title', 'description')

@admin.register(Hobbies)
class HobbiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary')
    search_fields = ('title', 'summary')

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'facebook', 'github')
    search_fields = ('phone', 'email')

