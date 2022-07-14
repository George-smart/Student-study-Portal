from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pix = models.ImageField(null=True, blank=True, upload_to='profile_images/')
    phone = models.PositiveBigIntegerField()
    address= models.CharField(max_length=300)
    school = models.CharField(max_length=500)
    department = models.CharField(max_length=300)
    faculty = models.CharField(max_length=300)
    level = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('create_dashboard')



class HomeWorks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title



class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dashboard = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('dashboard')

class Feedback(models.Model):
    subject = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.subject
