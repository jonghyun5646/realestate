from django.db import models


# Create your models here.
class Multi(models.Model):
    id = models.AutoField(primary_key=True)
    addr = models.CharField(max_length=500)
    m_domain = models.IntegerField()
    s_domain = models.IntegerField()
    area = models.FloatField()
    floor = models.IntegerField()
    year = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = 'multi'
        ordering = ['-addr']
