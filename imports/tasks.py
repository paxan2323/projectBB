# Create your tasks here

from celery import shared_task
from .importrers.imp import ImporterXML
from .models import Config

@shared_task
def import_data(config_id):
    config = Config.objects.get(id=config_id)
    importer = ImporterXML(config)
    importer.import_data()