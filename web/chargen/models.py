from __future__ import unicode_literals

from django.db import models


class CharApp(models.Model):
    app_id = models.AutoField(primary_key=True)
    char_name = models.CharField(max_length=80, verbose_name='Character Name')
    date_applied = models.DateTimeField(verbose_name='Date Applied')
    background = models.TextField(verbose_name='Background')
    player_id = models.IntegerField(default=1, verbose_name='Player ID')
    submitted = models.BooleanField(default=False)
