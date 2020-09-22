from django.db import models

# Create your models here.

class Kota(models.Model):
    CHOICES = [('Tersedia', 'Tersedia'), ('Penuh', 'Penuh')]
    nama_kota = models.TextField()
    status = models.TextField(choices=CHOICES, default = 'Tersedia')
    def __str__(self):
        return self.nama_kota


class Outlet(models.Model):
    kota = models.ForeignKey(Kota, on_delete=models.CASCADE)
    alamat = models.TextField()
