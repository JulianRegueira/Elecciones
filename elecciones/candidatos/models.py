from django.db import models

class candidato(models.Model):
    id_candidato = models.AutoField(primary_key=True)
    img_candidato = models.ImageField(upload_to="./candidatos/")
    cantidad_de_votos = models.IntegerField(default=0)