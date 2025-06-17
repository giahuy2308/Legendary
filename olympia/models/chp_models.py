from django.db import models
from .base_models import *

class CHPControl(models.Model):
    players_joined = models.CharField(max_length=4,default="0,0,0,0")
    player_steal = models.ForeignKey(Player, on_delete=models.RESTRICT , blank=True, null=True)
    show_question = models.BooleanField(default=False)

    def __str__(self):
        return "Phần thi: Câu Hỏi Phụ"
    
class CHPQuestion(AbstractQuestion):    
    pass

class CHPRecord(AbstractRecord):
    player_steal = models.ForeignKey(PlayerRecord, on_delete=models.RESTRICT , blank=True,null=True)
    question = models.ForeignKey(CHPQuestion, on_delete=models.SET_NULL, null=True)