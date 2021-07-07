from django.db import models


class CompoundName(models.Model):
    nome_Completo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_Completo
