from django.db import models

# Create your models here.

class Openedu:

    class Meta:
        app_label = 'openedudb'
        db_table = 'index_openedu'


class  Resultdb:

    class Meta:
        app_label = 'resultdb'
        db_table = 'index_result'
