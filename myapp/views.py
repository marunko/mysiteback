from django.shortcuts import render
from .serializations import *
from .models import *
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"})

class ProtectedDataView(APIView):
    def get(self, request):
        token_key = request.GET.get("token")  # Extract token from query params
        if not token_key:
            return Response({"error": "Token is required."}, status=status.HTTP_403_FORBIDDEN)
        
        # Validate token
        token = get_object_or_404(Token, key=token_key)
        if token.is_expired():
            token.delete()  # Delete expired token immediately
            return Response({"error": "Token has expired."}, status=status.HTTP_403_FORBIDDEN)
        
        # Get associated tag
        tag = token.tag
        
        # Fetch data related to this tag
        about_me = AboutMe.objects.filter(tag=tag)
        experiences = Experience.objects.filter(tag=tag)
        skills = Skills.objects.filter(tag=tag)
        certifications = Certification.objects.filter(tag=tag)
        projects = Projects.objects.filter(tag=tag)
        hobbies = Hobbies.objects.all()  # No tag field, return all

        # Serialize data
        data = {
            "about_me": AboutMeSerializer(about_me, many=True).data,
            "experiences": ExperienceSerializer(experiences, many=True).data,
            "skills": SkillsSerializer(skills, many=True).data,
            "certifications": CertificationSerializer(certifications, many=True).data,
            "projects": ProjectsSerializer(projects, many=True).data,
            "hobbies": HobbiesSerializer(hobbies, many=True).data,
        }
        
        return Response(data, status=status.HTTP_200_OK)

def validate_token(request):
    token_key = request.GET.get("token")
    if not token_key:
        return Response({"error": "Token is required."}, status=status.HTTP_403_FORBIDDEN)
    
    token = get_object_or_404(Token, key=token_key)
    if token.is_expired():
        token.delete()  # Delete expired token immediately
        return Response({"error": "Token has expired."}, status=status.HTTP_403_FORBIDDEN)
    
    return token.tag

class AboutMeView(APIView):
    def get(self, request):
        tag = validate_token(request)
        if isinstance(tag, Response):
            return tag
        about_me = AboutMe.objects.filter(tag=tag).first()
        if about_me is None:
            return Response({"detail": "No AboutMe found for this tag."}, status=status.HTTP_404_NOT_FOUND)
        return Response(AboutMeSerializer(about_me).data, status=status.HTTP_200_OK)

class ExperienceView(APIView):
    def get(self, request):
        tag = validate_token(request)
        if isinstance(tag, Response):
            return tag
        experiences = Experience.objects.filter(tag=tag).order_by('-start_date')
        data = ExperienceSerializer(experiences, many=True).data
        
        for item in data:
            item['job_roles'] = JobRoleSerializer(
                JobRole.objects.filter(experience=item['id']), 
                many=True
            ).data
        return Response(data, status=status.HTTP_200_OK)


class SkillsView(APIView):
    def get(self, request):
        tag = validate_token(request)
        if isinstance(tag, Response):
            return tag
        skills = Skills.objects.filter(tag=tag)
        data = SkillsSerializer(skills, many=True).data
        for item in data:
            item['skill_tags'] = SkillTagSerializer(SkillTag.objects.filter(skill=item['id']), many=True).data
        return Response(data, status=status.HTTP_200_OK)

class CertificationsView(APIView):
    def get(self, request):
        tag = validate_token(request)
        if isinstance(tag, Response):
            return tag
        certifications = Certification.objects.filter(tag=tag)
        return Response(CertificationSerializer(certifications, many=True).data, status=status.HTTP_200_OK)

class ProjectsView(APIView):
    def get(self, request):
        tag = validate_token(request)
        if isinstance(tag, Response):
            return tag
        projects = Projects.objects.filter(tag=tag)
        return Response(ProjectsSerializer(projects, many=True).data, status=status.HTTP_200_OK)

class ProjectByTitleView(APIView):
    def get(self, request, title):
        tag = validate_token(request)
        if isinstance(tag, Response):
            return tag
        project = get_object_or_404(Projects, title__iexact=title, tag=tag)
        return Response(ProjectsSerializer(project).data, status=status.HTTP_200_OK)
    
class HobbiesView(APIView):
    def get(self, request):
        tag = validate_token(request)
        if isinstance(tag, Response):
            return tag
        hobbies = Hobbies.objects.all()
        return Response(HobbiesSerializer(hobbies, many=True).data, status=status.HTTP_200_OK)

class CheckTokenView(APIView):
    def get(self, request):
        try:
            tag = validate_token(request)
        except:
            return Response({"access": False}, status=status.HTTP_403_FORBIDDEN)
        if isinstance(tag, Response):
            return Response({"access": False}, status=status.HTTP_403_FORBIDDEN)
        
        return Response({"access": True}, status=status.HTTP_200_OK)
    
class ContactsView(APIView):
    def get(self, request):
        contacts = Contacts.objects.first()
        if isinstance(contacts, Contacts):     
            return Response(ContactsSerializer(contacts).data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)