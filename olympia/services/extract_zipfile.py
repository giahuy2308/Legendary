from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

import zipfile
import os

def extract_zip(zip_file):
    zip_temp_path = default_storage.save("temp_upload.zip", ContentFile(zip_file.read()))
    extract_to = os.path.join(settings.MEDIA_ROOT, "Exam")
    os.mkdir(extract_to,exist_ok=True)

    zip_full_path = os.path.join(settings.MEDIA_ROOT, zip_temp_path)

    try:
        with zipfile.ZipFile(zip_full_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
            return zip_ref.namelist()[0]
    except zipfile.BadZipfile:
        return  "error"