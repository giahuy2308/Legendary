from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

global QUESTION_DATA_TYPE_CHOICES
QUESTION_DATA_TYPE_CHOICES = [
        ("Image", "I"),
        ("Audio", "A"),
        ("Video", "V"),
        ("Text", "T"),
]

class Player(models.Model):
    display_name = models.CharField(max_length=255,default="")
    current_score = models.PositiveIntegerField(default=0)
    is_connected = models.BooleanField(default=False)
    auth_id = models.CharField(max_length=10, default="")

    class Meta:
        get_latest_by = "auth_id"

    def __str__(self):
        return f"{self.auth_id} | {self.display_name}"

class Exam(models.Model):
    title = models.CharField(max_length=255,default="")
    scheduled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'title'
    
    def __str__(self):
        return self.title

class ExamRecord(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,default="")
    current_record = models.BooleanField(default=True)
    played_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = ["exam","played_at"]

    def __str__(self):
        return self.title

    # Uncomplete/ ReWrite in signals 
    def save(self,*args,**kwargs):
        self.title = f'"{self.exam.title}" record @ {self.played_at}' 
        return super().save(*args,**kwargs)
    
class PlayerRecord(models.Model):
    no = models.PositiveIntegerField(default=0)
    record = models.ForeignKey(ExamRecord, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255,default="")
    score = models.PositiveIntegerField(default=0)

    def created():
        pass

    def __str__(self):
        return f"{self.no} | {self.display_name}" 

# Tự động xoá file media lưu trong resources khi xoá hoặc update media instance
class MediaResource(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    question = GenericForeignKey('content_type', 'object_id')
    
    media_type = models.CharField(max_length=10, choices=QUESTION_DATA_TYPE_CHOICES, default="Image")

    def get_upload_path(instance, filename):
        return f'{instance.media_type}/{filename}'
    
    resource = models.FileField(upload_to=get_upload_path)

    class Meta:
        get_latest_by = ["question","media_type"]

    def __str__(self):
        return f"{self.question.exam} | {self.resource}"

class AbstractQuestion(models.Model):
    question_no = models.PositiveBigIntegerField(default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer = models.TextField(blank=True,null=True)
    question_data_type = models.CharField(max_length=10,choices=QUESTION_DATA_TYPE_CHOICES, default="Text")
    question_value = models.PositiveIntegerField(default=10)
    target_player_no = models.PositiveIntegerField(default=1)
    media = GenericRelation(MediaResource)

    class Meta:
        abstract = True
        get_latest_by = ["exam","-target_player_no","-question_no"]
    
    def __str__(self):
        return f"{self.target_player_no} | {self.question_no} | {self.question_text} | {self.question_data_type} | {self.exam}"
    


class AbstractRecord(models.Model):
    record = models.ForeignKey(ExamRecord, on_delete=models.CASCADE)
    question_no = models.PositiveIntegerField(default=0)
    question_data_type = models.CharField(max_length=10, choices=QUESTION_DATA_TYPE_CHOICES, default="Text")
    is_correct = models.BooleanField(default=False)
    question_value = models.PositiveIntegerField(default=10)
    question_text = models.TextField()
    answer_text = models.TextField()
    media = GenericRelation(MediaResource)

    class Meta:
        abstract = True
        get_latest_by = ["exam","record","question","question_no"]

    def save(self, *args, **kwargs):
        self.question_no = self.question.question_no
        self.question_text = self.question.question_text
        self.question_value = self.question.question_value
        self.question_data_type = self.question.question_data_type
        self.answer_text = self.question.answer
        
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.record} | {self.question_no} | {self.question_text}"