from django.db import models
from django.core.validators import MinLengthValidator

class Menyu(models.Model):
    nom = models.CharField(max_length=40, blank=True, null=True, validators=[MinLengthValidator(3)])
    nomru = models.CharField(max_length=40, blank=True, null=True, validators=[MinLengthValidator(3)])
    nomeng = models.CharField(max_length=40, blank=True, null=True, validators=[MinLengthValidator(3)])
    nomturk = models.CharField(max_length=40, blank=True, null=True, validators=[MinLengthValidator(3)])

    isSubmyu = models.BooleanField(default=True)
    rasm = models.FileField(null=True, blank=True)
    url = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self) -> str:
        return self.nom


class SubMenyu(models.Model):
    nom = models.CharField(max_length=100, blank=True, null = True, validators=[MinLengthValidator(3)])
    nomru = models.CharField(max_length=100, blank=True, null = True, validators=[MinLengthValidator(3)])
    nomeng = models.CharField(max_length=100, blank=True, null = True, validators=[MinLengthValidator(3)])
    nomturk = models.CharField(max_length=100, blank=True, null = True, validators=[MinLengthValidator(3)])

    text1 = models.TextField( blank=True, null = True, validators=[MinLengthValidator(3)])
    text1ru = models.TextField( blank=True, null = True, validators=[MinLengthValidator(3)])
    text1eng = models.TextField( blank=True, null = True, validators=[MinLengthValidator(3)])
    text1turk = models.TextField( blank=True, null = True, validators=[MinLengthValidator(3)])

    text2 = models.TextField( blank=True, null = True, validators=[MinLengthValidator(3)])
    text2ru = models.TextField( blank=True, null = True, validators=[MinLengthValidator(3)])
    text2eng = models.TextField( blank=True, null = True, validators=[MinLengthValidator(3)])
    text2turk = models.TextField( blank=True, null = True, validators=[MinLengthValidator(3)])

    rasm1 = models.FileField(null=True, blank=True)
    rasm2 = models.FileField(null=True, blank=True)
    menyu = models.ForeignKey(Menyu, on_delete=models.CASCADE)
    url = models.CharField(max_length=40, blank=True, null=True)
    icon = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nom


class Mahsulot(models.Model):
    nom = models.CharField(max_length=60, blank=True, null = True, validators=[MinLengthValidator(3)])
    nomru = models.CharField(max_length=60, blank=True, null = True, validators=[MinLengthValidator(3)])
    nomeng = models.CharField(max_length=60, blank=True, null = True, validators=[MinLengthValidator(3)])
    nomturk = models.CharField(max_length=60, blank=True, null = True, validators=[MinLengthValidator(3)])

    text1 = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    text1ru = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    text1eng = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    text1turk = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])

    rasm = models.FileField(null=True,blank=True)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class HomePage(models.Model):
    title1 = models.CharField(max_length=200, null=True, blank=True)
    title2 = models.CharField(max_length=200, null=True, blank=True)
    title3 = models.CharField(max_length=200, null=True, blank=True)
    titleru1 = models.CharField(max_length=200, null = True, blank=True)
    titleru2 = models.CharField(max_length=200, null = True, blank=True)
    titleru3 = models.CharField(max_length=200, null = True, blank=True)
    titleeng1 = models.CharField(max_length=200, null = True, blank=True)
    titleeng2 = models.CharField(max_length=200, null = True, blank=True)
    titleeng3 = models.CharField(max_length=200, null = True, blank=True)
    titleeturk1 = models.CharField(max_length=200, null = True, blank=True)
    titleeturk2 = models.CharField(max_length=200, null = True, blank=True)
    titleeturk3 = models.CharField(max_length=200, null = True, blank=True)



    rasm1=models.FileField()
    rasm2=models.FileField()
    rasm3=models.FileField()

    text1 = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    text1ru = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    text1eng = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    text1turk = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])

class Ul(models.Model):
    nom = models.CharField(max_length=60, blank=True, null = True, validators=[MinLengthValidator(3)])
    nomru = models.CharField(max_length=60, blank=True, null = True, validators=[MinLengthValidator(3)])
    nomeng = models.CharField(max_length=60, blank=True, null = True, validators=[MinLengthValidator(3)])
    nomturk = models.CharField(max_length=60, blank=True, null = True, validators=[MinLengthValidator(3)])
    submenyu=models.ForeignKey(SubMenyu,on_delete=models.CASCADE,null=True,blank=True)

class List(models.Model):
    text1 = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    text1ru = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    text1eng = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    text1turk = models.TextField(blank=True, null=True, validators=[MinLengthValidator(3)])
    ul=models.ForeignKey(Ul,on_delete=models.CASCADE)


