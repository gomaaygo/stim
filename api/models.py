from django.db import models


class AQChild(models.Model):
    a1_score = models.IntegerField(verbose_name="AQ-1", blank=False, null=False)
    a2_score = models.IntegerField(verbose_name="AQ-2", blank=False, null=False)
    a3_score = models.IntegerField(verbose_name="AQ-3", blank=False, null=False)
    a4_score = models.IntegerField(verbose_name="AQ-4", blank=False, null=False)
    a5_score = models.IntegerField(verbose_name="AQ-5", blank=False, null=False)
    a6_score = models.IntegerField(verbose_name="AQ-6", blank=False, null=False)
    a7_score = models.IntegerField(verbose_name="AQ-7", blank=False, null=False)
    a8_score = models.IntegerField(verbose_name="AQ-8", blank=False, null=False)
    a9_score = models.IntegerField(verbose_name="AQ-9", blank=False, null=False)
    a10_score = models.IntegerField(verbose_name="AQ-10", blank=False, null=False)
    result = models.IntegerField(verbose_name="Resultado", blank=False, null=False)
    
    class Meta:
        verbose_name = 'Escala AQ-10 - Criança'

    def __str__(self) -> str:
        return str(self.result)