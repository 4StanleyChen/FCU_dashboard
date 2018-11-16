from django.shortcuts import render
#from try1.models import Country, Course
from django.db import connections, DatabaseError
from collections import namedtuple


def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


# Create your views here.
def C_T(request):
    try:
        cursor = connections['test1'].cursor()
        sql = 'course_total_data_v2'
        radio = 2016
        wildcard = "and duration_week is not NULL"
        to_render = {}

        cursor.execute(
            "select * "
            "from course_total_data_v2 "
            "where 課程代碼 = 'C01' ")
        result = namedtuplefetchall(cursor)

        r = None
        if len(result) != 0:
            r = result[-1].註冊人數

        to_render['country'] = r

    except DatabaseError:
        pass

    return render(request, 'try1.html', to_render)



