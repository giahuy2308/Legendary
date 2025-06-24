
from django.forms.models import model_to_dict
from django.db.models import Q
from dotenv import load_dotenv #
import os #

load_dotenv()

def add_media_to_record(record,question):
    for media in question.media.all():
        record.media.add(media)
    record.save()

def get_no_from_auth_id(auth_id):
    for no, _auth_id in enumerate(os.getenv("player_auth_id").split(",")):
        if auth_id == _auth_id:
            return no+1
        
def record_player(record):
    from ..models.base_models import Player,PlayerRecord

    current_player = Player.objects.all()
    players_recorded=[]

    for player in current_player:
        player_recorded = PlayerRecord.objects.create(
            no=get_no_from_auth_id(player.auth_id),
            record=record,
            display_name=player.display_name,
            score=player.current_score
        )
        player_recorded.save()
        players_recorded.append(player_recorded)

    return players_recorded

def create_empty_record_question(RecordModel, record, questions, players_recorded,**kwargs):
    for question in questions:
        
        question_dict = model_to_dict(question)

        record_question = RecordModel.objects.create(
            record=record,
            question=question,
        )

        if question_dict["target_player_no"] != 0:

            get_player= lambda pl: pl.no == question_dict["target_player_no"]
            
            player = list(filter(get_player, players_recorded))[0]
            setattr(record_question ,"player", player)
            question_dict["target_player_no"] = -1
        question_dict["id"] = -1
        question_dict["exam"] = -1

        add_media_to_record(record_question, question)
        
        record_dict = {**question_dict,**kwargs}

        for field,value in record_dict.items():
            if value != -1:
                setattr(record_question, field, value)

        record_question.save()



def  create_empty_record(exam,**kwargs):
    from ..models.base_models import ExamRecord
    from ..models.kd_models import KDRecord, KDQuestion
    from ..models.vcnv_models import VCNVRecord, VCNVQuestion
    from ..models.tt_models import TTRecord, TTQuestion
    from ..models.vd_models import VDRecord, VDQuestion
    from ..models.chp_models import CHPRecord, CHPQuestion

    record = ExamRecord.objects.create(
        exam=exam,
        title="_",
        current_record=True
    )
    setattr(record, "title", f'"{exam.title} record @ {record.played_at}')
    record.save()

    kd = KDQuestion.objects.all()
    vcnv = VCNVQuestion.objects.all()
    tt = TTQuestion.objects.all()
    vd = VDQuestion.objects.all()
    chp = CHPQuestion.objects.all()

    players_recorded = record_player(record)

    create_empty_record_question(KDRecord, record, kd, players_recorded, player_steal=None)
    create_empty_record_question(VCNVRecord, record, vcnv, players_recorded, picture_opened=-1, question_shown=-1, player_answer={"":""})
    create_empty_record_question(TTRecord, record, tt, players_recorded, player_answer={"":""})
    create_empty_record_question(VDRecord, record, vd, players_recorded, player_steal=None, picked_question="0,0,0,0,0,0", nshv='0,0,0')
    create_empty_record_question(CHPRecord, record, chp, players_recorded, player_steal=None)

def referenced_media(instance):
    is_referenced = instance.kdrecord_set.exists() | instance.vcnvrecord_set.exists() | instance.ttrecord_set.exists() | instance.vdrecord_set.exists()
    return is_referenced

def remove_record_media():
    from ..models.base_models import MediaResource
    orphan_medias = MediaResource.objects.all()
    for media in orphan_medias:
        if not referenced_media(media): 
            media.delete()