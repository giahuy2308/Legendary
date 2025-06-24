from django.db import models
from .base_models import *

class VDControl(models.Model):
    current_player = models.ForeignKey(Player,on_delete=models.RESTRICT , blank=True, null=True)
    show_picker = models.BooleanField(default=False)
    picked_questions = models.CharField(max_length=6, default="0,0,0,0,0,0")
    nshv_active = models.BooleanField(default=False)
    nshv_turned_on = models.BooleanField(default=False)
    show_question = models.BooleanField(default=False)

    def __str__(self):
        return "Phần thi: Về đích"
    
class VDQuestion(AbstractQuestion):
    pass

class VDRecord(AbstractRecord):
    player = models.ForeignKey(PlayerRecord, related_name="vd_player_record", on_delete=models.RESTRICT ,null=True)
    player_steal = models.ForeignKey(PlayerRecord, related_name="vd_steal_record", on_delete=models.RESTRICT,blank = True, null=True)
    question = models.ForeignKey(VDQuestion, on_delete=models.SET_NULL, null=True)
    picked_question = models.CharField(max_length=6, default="0,0,0,0,0,0")
    nshv = models.CharField(max_length=3,default="0,0,0")
