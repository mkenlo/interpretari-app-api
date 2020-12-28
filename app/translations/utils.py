import os
import re
import datetime
import zipfile
from django.conf import settings 

UPLOAD_PATH = settings.MEDIA_ROOT
UPLOAD_URL= settings.MEDIA_URL

def export_translation_per_language(source_lang, target_lang):
    archive_name = "_".join([str(datetime.date.today()),"export", source_lang, target_lang, "archive.zip"])
    archive_path = os.path.join(UPLOAD_PATH, archive_name)
    prefix = re.compile(source_lang.lower()+"_"+target_lang.lower())
    zipf = zipfile.ZipFile(archive_path, 'w')
    count = 0
    for root, dirs, files in os.walk(UPLOAD_PATH):
        for file in files:
            if prefix.match(file):
                filepath = os.path.join(root,file)
                zipf.write(filepath, os.path.basename(filepath))
                count+=1
    zipf.close()

    if count==0:
        os.remove(archive_path)
        return {"detail": "No files found"}

    return {"uri": UPLOAD_URL+archive_name, "audiofiles":count}
    

