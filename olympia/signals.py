from django.dispatch import receiver
from django.db import transaction
from django.db.models.signals import post_delete, pre_delete, post_migrate
from .models.base_models import MediaResource, Player
from .models.kd_models import KDRecord, KDControl
from .models.vcnv_models import VCNVRecord, VCNVControl
from .models.tt_models import TTRecord, TTControl
from .models.vd_models import VDRecord, VDControl
from .models.chp_models import CHPControl 
from .services.signal_services import referenced_media, remove_record_media
import os


@receiver(pre_delete, sender=MediaResource)
def delete_media_file(sender, instance, **kwargs):
    if referenced_media(instance):
        media = MediaResource.objects.create(
            content_type = None,
            object_id=0,
            media_type=instance.media_type,
            resource=instance.resource,
        ) 
        for kd in instance.kdrecord_set.all():
            media.kdrecord_set.add(kd)
        for vcnv in instance.vcnvrecord_set.all():
            media.vcnvrecord_set.add(vcnv)
        for tt in instance.ttrecord_set.all():
            media.ttrecord_set.add(tt)
        for vd in instance.vdrecord_set.all():
            media.vdrecord_set.add(vd)
        media.save()

    elif instance.resource:
        file_path = instance.resource.path  
        if os.path.isfile(file_path):       # Tránh lỗi khi file không tồn tại
            os.remove(file_path)

@receiver(post_delete, sender=KDRecord)
def delete_kd_record_media(sender,instance,**kwargs):
    transaction.on_commit(remove_record_media)

@receiver(post_delete, sender=VCNVRecord)
def delete_vcnv_record_media(sender,instance,**kwargs):
    transaction.on_commit(remove_record_media)

@receiver(post_delete, sender=TTRecord)
def delete_tt_record_media(sender,instance,**kwargs):
    transaction.on_commit(remove_record_media)

@receiver(post_delete, sender=VDRecord)
def delete_vd_record_media(sender,instance,**kwargs):
    transaction.on_commit(remove_record_media)

