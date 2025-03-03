
from .models import *
from rest_framework import serializers

# Serializers
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title', 'key']

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['id','tag', 'key', 'created_at', 'expires_at']


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ['id', 'tag', 'title', 'text', 'summary']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'tag', 'position', 'company', 'start_date', 'end_date', 'reference']


class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRole
        fields = ['id', 'experience', 'roles']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['id', 'tag', 'title']


class SkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag
        fields = ['id', 'skill', 'text']


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id','tag', 'title', 'text', 'image_path', 'link']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id','tag', 'title', 'description','summary','image_path', 'link']


class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ['id', 'title', 'summary', 'image_path']

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'phone', 'email', 'facebook', 'github']