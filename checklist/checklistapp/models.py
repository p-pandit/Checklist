from django.db import models

class common_checklist(models.Model):

    Delar_Name=models.CharField(max_length=200)
    var1=models.CharField(max_length=200)
    var2 = models.CharField(max_length=200)
    var3 = models.CharField(max_length=200)
    var4 = models.CharField(max_length=200)
    var5 = models.CharField(max_length=200)
    var6 = models.CharField(max_length=200)
    var7 = models.CharField(max_length=200)
    var8 = models.CharField(max_length=200)
    var9 = models.CharField(max_length=200)
    var10 = models.CharField(max_length=200)
    var11 = models.CharField(max_length=200)
    var12 = models.CharField(max_length=200)
    var13 = models.CharField(max_length=200)
    var14 = models.CharField(max_length=200)
    var15 = models.CharField(max_length=200)
    date = models.DateField()
    datetime = models.DateTimeField()

    class Meta:
        abstract=True

class s21(common_checklist):
    pass


