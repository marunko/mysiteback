
# Create your models here.
from django.db import models
from django.utils.timezone import now, timedelta
from django.utils.crypto import get_random_string

# API is a category of Jobs like IT, Construction etc, for management 
# actual access to info must be made by Temporary keys 
class Tag(models.Model):
    title = models.CharField(max_length=255)
    key = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

# this key will be spreaded in url /parameter or ?query=key
class Token(models.Model): # remove ? 
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='token')
    key = models.CharField(max_length=14, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.key = get_random_string(length=14, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        self.expires_at = now() + timedelta(days=90)
        super().save(*args, **kwargs)

    def is_expired(self):
        return now() > self.expires_at

    def __str__(self):
        return f"{self.key} (Expires: {self.expires_at})"

class AboutMe(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='about_me')
    title = models.CharField(max_length=255)
    text = models.TextField()
    summary = models.CharField(max_length=255, blank=True, null=True)  # New field

    def __str__(self):
        return self.title


class Experience(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='experiences')
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    reference = models.URLField(null=True, blank=True) #references to disk
# references path link
    def __str__(self):
        return f"{self.position} at {self.company}"


class JobRole(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='job_roles')
    #position = models.CharField(max_length=255)
    roles = models.TextField()

    def __str__(self):
        return self.position


class Skills(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='skills')
    title = models.CharField(max_length=255)
    #text = models.TextField()

    def __str__(self):
        return self.title


class SkillTag(models.Model):
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE, related_name='skill_tags')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Certification(models.Model):
    #api KEY !!???
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,default=1, related_name='certification')
    title = models.CharField(max_length=255)
    text = models.TextField()
    image_path = models.CharField(max_length=255)  # String path to the image
    link = models.URLField()

    def __str__(self):
        return self.title


class Projects(models.Model):
    #API key
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,default=1, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    summary = models.CharField(max_length=255, blank=True, null=True)  # New field
    image_path = models.CharField(max_length=255)  # String path to the image
    link = models.URLField()

    def __str__(self):
        return self.title


class Hobbies(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    image_path = models.CharField(max_length=255)  # String path to the image

    def __str__(self):
        return self.title

class Contacts(models.Model):
    phone = models.CharField(max_length=25)
    email=models.CharField(max_length=255)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.phone    