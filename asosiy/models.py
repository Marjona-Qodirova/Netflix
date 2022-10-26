from django.db import models



class Aktyor(models.Model):
    ism=models.CharField(max_length=50)
    yosh=models.PositiveSmallIntegerField()
    davlat=models.CharField(max_length=30)
    jins=models.CharField( max_length=15 , choices=[("Erkak", "Erkak") ,("Ayol", "Ayol")])
    def __str__(self):
        return self.ism
class Kino(models.Model):
    nom=models.CharField(max_length=50)
    reyting=models.FloatField()
    aktyorlar=models.ManyToManyField( Aktyor)
    def __str__(self):
        return self.nom




