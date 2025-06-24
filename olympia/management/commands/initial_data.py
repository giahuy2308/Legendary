from django.core.management.base import BaseCommand
from olympia.models.base_models import Player
from olympia.models.kd_models import KDControl
from olympia.models.vcnv_models import VCNVControl
from olympia.models.tt_models import TTControl
from olympia.models.vd_models import VDControl
from olympia.models.chp_models import CHPControl
import os 
from dotenv import load_dotenv #

load_dotenv()

class Command(BaseCommand):
    help = "Tạo dữ liệu mặc định ban đầu (chỉ chạy 1 lần sau khi tạo DB)"

    def handle(self, *args, **kwargs):

        if not Player.objects.exists():
            
            auth_id=os.getenv("player_auth_id").split(',')
            for no in range(1,5):
                player = Player.objects.create(
                    display_name="",
                    current_score=0,
                    is_connected=False,
                    auth_id=auth_id[no-1]
                )
                player.save()

            models = [KDControl,VCNVControl,TTControl,VDControl,CHPControl]
            
            for Model in models:
                control = Model.objects.create()
                control.save()

            self.stdout.write(self.style.SUCCESS("✔ Dữ liệu mặc định đã được tạo"))
        else:
            self.stdout.write(self.style.WARNING("⚠ Dữ liệu đã tồn tại. Bỏ qua."))
            