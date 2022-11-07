from django.db import models
from django.core.validators import (
    RegexValidator, EmailValidator, URLValidator
)
from django.conf import settings


class MetaElements(models.Model):
    site_name = models.CharField(max_length=50)
    description_site = models.CharField(max_length=150)
    title = models.CharField(max_length=50)
    spotimage = models.ImageField(upload_to="img/")
    keywords =  models.CharField(max_length=150, blank=True, null=True)
    copyright_site = models.CharField(max_length=150)
    copyright_url = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )
    canonnical_link = models.CharField(max_length=205, blank=True)


class SocialLinks(models.Model):
    section_name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=150)
    facebook = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )
    twiter = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )
    instagram = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )
    twich = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )
    youtube = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )
    linkedin = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )


class Contact(models.Model):
    section_name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500)
    location = models.CharField(max_length=100, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=250, validators=[EmailValidator], default=settings.DEFAULT_FROM_EMAIL)


class HeroSettings(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to="img", default="img/logo.png")
    background_image = models.ImageField(upload_to="img", default="img/img7.webp")
    background_video = models.FileField(help_text="solo vidoes mp4", upload_to="vid", default="vid/reel_un_cuarto.mp4", blank=True)


class ShowReel(models.Model):
    section_name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    video = models.URLField()
    background_image = models.ImageField(upload_to="img/showreel", default="img/img7.webp")


class ServicesSection(models.Model):
    section_name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500, blank=True, null=True)


class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)


class PortafolioSection(models.Model):
    section_name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500, blank=True, null=True)


class Portafolio(models.Model):
    name = models.CharField(max_length=150)
    thumbnails = models.ImageField(blank=True ,upload_to="img/portfolio", default="img/img4.jpg")
    video = models.URLField()
    slug = models.SlugField()


class AboutUsSection(models.Model):
    section_name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500)
    thumbnails = models.ImageField(blank=True ,upload_to="img/about", default="img/img4.jpg")
    titulo = models.CharField(max_length=100, blank=True, null=True)
    info = models.CharField(max_length=250, blank=True, null=True)
    title_mision = models.CharField(max_length=50)
    mision = models.CharField(max_length=250)
    title_vision = models.CharField(max_length=50)
    vision = models.CharField(max_length=259)

class TeamSection(models.Model):
    section_name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500, blank=True, null=True)

class Team(models.Model):
    thumbnails = models.ImageField(upload_to="img/team", default="img/img4.jpg")
    name = models.CharField(max_length=50)
    possition = models.CharField(max_length=50)
    facebook = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )
    twiter = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )
    instagram = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )
    linkedin = models.URLField(max_length=205, blank=True, null=True, validators=[URLValidator] )


class Comment(models.Model):
    foto = models.ImageField(upload_to="img/comments", default="img/img4.jpg")
    nombre = models.CharField(max_length=150)
    posicion = models.CharField(max_length=150, help_text="Da una descripcion pequeña de lo que haces")
    timestamp = models.DateTimeField(auto_now=True)
    comentario = models.TextField()


class GaleriaSection(models.Model):
    section_name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500, blank=True, null=True)

class Galeria(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img", default="img/img7.webp")