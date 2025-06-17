from django.db import models
from .base_models import * 

global QUESTION_TYPE_CHOICES
QUESTION_TYPE_CHOICES = [
        ("HN","HN"),
        ("TT","TT"),
        ("CNV","CNV")
]

class VCNVControl(models.Model):
    show_question = models.BooleanField(default=False)
    show_result = models.BooleanField(default=False)
    disabled_players = models.CharField(max_length=10, default="0,0,0,0")
    players_answer_cnv = models.CharField(max_length=10,default="0,0,0,0")

    def __str__(self):
        return "Phần thi: Vượt Chướng Ngại Vật"

class VCNVQuestion(AbstractQuestion):
    picture_opened = models.BooleanField(default=False)
    question_shown = models.BooleanField(default=False)
    question_type = models.CharField(max_length=10,choices=QUESTION_TYPE_CHOICES,default="HN")


class VCNVRecord(AbstractRecord):
    player_answer = models.JSONField()
    question = models.ForeignKey(VCNVQuestion, on_delete=models.SET_NULL, null=True)
    question_type = models.CharField(max_length=10,choices=QUESTION_TYPE_CHOICES, default="HN")


