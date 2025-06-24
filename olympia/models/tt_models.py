from django.db import models
from .base_models import *

class TTControl(models.Model):
    show_question = models.BooleanField(default=False)
    show_result = models.BooleanField(default=False)

    def __str__(self):
        return "Phần thi: Tăng Tốc"
    
class TTQuestion(AbstractQuestion):
    pass    

class TTRecord(AbstractRecord):
    player_answers = models.JSONField(null=True)
    question = models.ForeignKey(TTQuestion, on_delete=models.SET_NULL, null=True)


