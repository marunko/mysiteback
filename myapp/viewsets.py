from rest_framework import viewsets
from .models import Contacts, Token, Tag, AboutMe, Experience, JobRole, Skills, SkillTag, Certification, Projects, Hobbies
from .serializations import ContactsSerializer, TokenSerializer, TagSerializer, AboutMeSerializer, ExperienceSerializer, JobRoleSerializer, SkillsSerializer, SkillTagSerializer, CertificationSerializer, ProjectsSerializer, HobbiesSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer    

class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class JobRoleViewSet(viewsets.ModelViewSet):
    queryset = JobRole.objects.all()
    serializer_class = JobRoleSerializer

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class SkillTagViewSet(viewsets.ModelViewSet):
    queryset = SkillTag.objects.all()
    serializer_class = SkillTagSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class HobbiesViewSet(viewsets.ModelViewSet):
    queryset = Hobbies.objects.all()
    serializer_class = HobbiesSerializer

class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer