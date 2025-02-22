from django.db import models

# Create your models here.
class Publikasi(models.Model):
    judul = models.CharField(max_length=255)
    dikutip_oleh = models.IntegerField(default=0)
    tahun = models.IntegerField()
    link_publikasi = models.URLField()

    def __str__(self):
        return self.judul

class PKM(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='pkm_images/')
    tanggal = models.DateField()

    def __str__(self):
        return self.judul

class Research(models.Model):
    STATUS_CHOICES = [
        ('on_progress', 'On Progress'),
        ('done', 'Done'),
    ]
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='research_images/')
    tanggal = models.DateField()
    metodologi = models.TextField(help_text="Metodologi dalam format poin-poin")
    hasil = models.TextField(help_text="Hasil penelitian dalam format poin-poin")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='on_progress')

    def __str__(self):
        return self.judul

class ResearchGallery(models.Model):
    research = models.ForeignKey(Research, on_delete=models.CASCADE, related_name="gallery")
    gambar = models.ImageField(upload_to='research_gallery/')
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Gallery for {self.research.judul}"

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    job_type = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    responsibilities = models.TextField()
    skills = models.TextField()
    qualifications = models.TextField()
    working_time = models.TextField()
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Registration(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    cv = models.FileField(upload_to='cvs/')

    def __str__(self):
        return f"{self.name}"