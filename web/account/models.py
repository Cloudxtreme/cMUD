from __future__ import unicode_literals

from django.db import models
from evennia.objects.models import ObjectDB


class PlayerChars(models.Model):
    char_name = ObjectDB.CharField(max_length=80, verbose_name='Character Name')
    background = ObjectDB.TextField(verbose_name='Background')
    player_id = ObjectDB.IntegerField(default=1, verbose_name='Player ID')
