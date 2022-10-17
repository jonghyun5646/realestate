from django.db import models


# Create your models here.
class Multi(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.FloatField()
    floor = models.IntegerField()
    sigungu = models.CharField(max_length=500)
    m_domain = models.IntegerField()
    s_domain = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    gu = models.CharField(max_length=500)
    dong = models.CharField(max_length=500)
    deposit = models.IntegerField()
    predpr = models.IntegerField()
    rate = models.FloatField()
    risk = models.CharField(max_length=500)

    class Meta:
        db_table = 'multi'
        ordering = ['-id']