from django.db import models
from .base_models import *
# Create your models here.

class KDControl(models.Model):
    current_player = models.ForeignKey(Player, related_name="kd_current_player", on_delete=models.RESTRICT , blank=True, null=True)
    player_steal = models.ForeignKey(Player, related_name="kd_player_steal", on_delete=models.RESTRICT , blank=True, null=True)
    show_question = models.BooleanField(default=False)

    def __str__(self):
        return "Phần thi: Khởi Động"
    

class KDQuestion(AbstractQuestion):
    pass

class KDRecord(AbstractRecord):
    player = models.ForeignKey(PlayerRecord,related_name="kd_player_record", on_delete=models.RESTRICT , blank=True,null=True)
    player_steal = models.ForeignKey(PlayerRecord, related_name="kd_steal_record", on_delete=models.RESTRICT , blank=True, null=True)
    question = models.ForeignKey(KDQuestion, on_delete=models.SET_NULL, null=True)
    