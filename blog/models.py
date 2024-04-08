from datetime import timezone

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Royxat(models.Model):
    ism = models.CharField(max_length=500)
    tel_raqam = models.IntegerField()

    def __str__(self):
        return self.ism
class Yangiliklar(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/images')
    text = models.TextField()
    nom = models.CharField(max_length=1000)
    chopetilishVaqti = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=300)

    class Meta:
        ordering = ['-chopetilishVaqti']
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

    def __str__(self):
        return self.nom
class Bizhaqimizda_rasm(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/images')
    nom = models.CharField(max_length=200)
class SONGI_YILLARDA_BAJARILGAN_ISHLAR_XAJMI(models.Model):
    rasm = models.ImageField(upload_to='rasmlar/images')
    text = models.TextField()
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom
class FuterManzil(models.Model):
    email = models.CharField(max_length=200)
    manzil = models.TextField()
    tel_raqam1 = models.IntegerField()
    tel_raqam2 = models.IntegerField()

    def __str__(self):
        return self.email

class Comment(models.Model):
    products = models.ForeignKey(Yangiliklar,
                                 on_delete=models.CASCADE,
                                 related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return f"Comment - {self.body} by {self.user}"

