from django.db import models

# Create your models here.
class Publikasi(models.Model):
    judul = models.CharField(max_length=255)
    dikutip_oleh = models.IntegerField(default=0)
    tahun = models.IntegerField()
    link_publikasi = models.URLField()

    def __str__(self):
        return self.judul
