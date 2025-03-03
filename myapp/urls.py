from django.urls import path, include
from .views import *
from .viewsets import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'example', views.ExampleAPI) 
router.register(r'token', TokenViewSet)
router.register(r'tags', TagViewSet)
router.register(r'about-me', AboutMeViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'job-role', JobRoleViewSet)
router.register(r'skills', SkillsViewSet)
router.register(r'skill-tags', SkillTagViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'hobbies', HobbiesViewSet)
router.register(r'contacts', ContactsViewSet)

urlpatterns = [
    path('hello/', hello_world),
    path('root/', include(router.urls)),
    path('general-view/', ProtectedDataView.as_view(), name='token'),
    path('about-me-key/', AboutMeView.as_view(), name='token'),
    path('experience-key/', ExperienceView.as_view(), name='token'),
    path('skills-key/', SkillsView.as_view(), name='token'),
    path('certifications-key/', CertificationsView.as_view(), name='token'),
    path('projects-key/', ProjectsView.as_view(), name='token'),
    path('projects-key/<str:title>/', ProjectByTitleView.as_view(),name='title'),
    path('hobbies-key/', HobbiesView.as_view(), name='token'),# ??
    path('check-token/', CheckTokenView.as_view(),name='token'),
    path('contacts/',ContactsView.as_view()),
]