from django.db import models
from django.core import validators
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


current_year=datetime.now().year
# Create your models here.


def user_profile_upload_path(instance, filename):
    return f'userprofile/{instance.user.username}/{filename}'

class Education(models.Model):
    school_name=models.CharField(name='school', max_length=500)
    classes=models.CharField(name='classes', max_length=500)
    passed_year=models.IntegerField(validators=[
        validators.MinValueValidator(1995),
        validators.MaxValueValidator(current_year+5)
    ])
    marks=models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
    )

    # def __str__(self) -> str:
    #     return str(self.classes)
    


class Internships(models.Model):
    company=models.CharField(name='company', max_length=500)
    working_year=models.FloatField(
        validators=[validators.MaxValueValidator(100)]
    )

    def __str__(self):
        return self.company
    class Meta:
        verbose_name_plural='Internships'
    

class Project(models.Model):
    theme=models.CharField(name='theme', max_length=500)
    completeness=models.IntegerField(
        validators=[MaxValueValidator(100),MinValueValidator(0)]
    )
    def __str__(self):
        return self.theme


class Academic(models.Model):
    acadmic=models.TextField()


class Position(models.Model):
    position=models.CharField(name='position', max_length=500)
    role=models.TextField(name='role')
    def __str__(self):
        return self.position

class Links(models.Model):
    platform=models.CharField(name='platform', max_length=500)
    link=models.URLField(max_length=500)
    def __str__(self):
        return self.platform
    class Meta:
        verbose_name_plural = "Links"


    def get_favicon(self):
        url=self.link
        parsed_url = urlparse(url)
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
        }
        if(parsed_url.netloc =='auth.geeksforgeeks.org'):
            parsed_url=urlparse("https://www.geeksforgeeks.org/")
        url=parsed_url.scheme + '://' + parsed_url.netloc

        try:
            response = requests.get(url,headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, "html.parser")
            favicon = soup.find_all('link', rel="icon")
            favicon = favicon[-1]
            
            favicon_url = urlparse(favicon['href'])
            
            resp = requests.get(url + favicon_url.path)
            if resp.status_code == 200:
                return url + favicon_url.path
            
            resp=requests.get(favicon_url)
            if resp.status_code == 200:
                return favicon_url
        except Exception as e:
            print(e)
  


    

class skill(models.Model):
    skill=models.CharField(name='skill', max_length=50)
    stars=models.IntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(100)
        ]
    )

    def __str__(self) -> str:
        return self.skill





class modified_user(models.Model):
    user=models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    profile = models.ImageField(upload_to=user_profile_upload_path, height_field=None, width_field=None, max_length=None,blank=True)
    first_name=models.CharField(name='first_name', max_length=50,blank=False,null=False)
    last_name=models.CharField(name='last_name', max_length=50,blank=True,null=True)
    phone_number = PhoneNumberField()
    email=models.EmailField(name='email', max_length=254,blank=False,null=False)
    education=models.ManyToManyField(Education, verbose_name='education',blank=True)
    internships=models.ManyToManyField(Internships, verbose_name='internships',blank=True)
    academic_project=models.ManyToManyField(Project, verbose_name=("project"),blank=True)
    academic=models.ManyToManyField( Academic,verbose_name="academic",blank=True)
    skill=models.ManyToManyField(skill, verbose_name=("skill"),blank=True)
    position=models.ManyToManyField(Position, verbose_name=("position"),blank=True)
    links=models.ManyToManyField(Links, verbose_name=("link"),blank=True)



    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        upload_path=f"userprofile/{self.user.username}"
        self.profile.upload_to = upload_path
        super().save(*args, **kwargs)
    

    
class about(models.Model):
    user=models.ForeignKey(User, verbose_name='about', on_delete=models.CASCADE)
    discription=models.TextField( name='discription')
    date=models.DateField(auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return self.user.username