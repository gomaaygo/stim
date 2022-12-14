from django.db import models

    
class Person(models.Model):
    CHOICES_GENDER = (
        ("f", "Feminino"),
        ("m", "Masculino"),
    )
    
    age = models.IntegerField(verbose_name="Idade", blank=True, null=True)
    gender = models.CharField(max_length=1, verbose_name="Gênero", choices=CHOICES_GENDER)
    used_app_before = models.BooleanField(verbose_name="Utilizou aplicativo antes?", blank=True, null=True)
    austim = models.BooleanField(verbose_name="Possui algum parente autista?", blank=True, null=True)
    class_asd = models.BooleanField(verbose_name="Class ASD", blank=True, null=True)
    jaundice = models.BooleanField(verbose_name="Nasceu com icterícia?", blank=True, null=True)
    
    class Meta:
        verbose_name = 'Pessoa'

    def __str__(self) -> str:
        return str(self.class_asd)
    

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
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=False, null=True)
    result = models.IntegerField(verbose_name="Resultado", blank=True, null=True)
    
    class Meta:
        verbose_name = 'Escala AQ-10 - Criança'

    def __str__(self) -> str:
        return str(self.result)
    
    def save(self, *args, **kwargs):
        result = sum([self.a1_score, self.a2_score, self.a3_score, self.a4_score, self.a5_score, 
                      self.a6_score, self.a7_score, self.a8_score, self.a9_score, self.a10_score])
        self.result = result

        super().save(*args, **kwargs)