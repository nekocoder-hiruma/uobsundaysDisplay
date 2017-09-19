import os
from time import strftime
import uuid


def upload_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{0}.{1}".format(uuid.uuid4(), ext)
    return os.path.join(strftime('uploads/%Y/%m/%d'), filename)