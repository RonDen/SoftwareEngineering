import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ScoreManagement.settings'
django.setup()

import pandas as pd
import numpy as np
import openpyxl
from random import randint, choice
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from app.models import Teacher, Course, College


data_frame = pd.read_excel("school_course.xls")

data_frame['课程号'].unique()
data_frame['课程性质'].get(key='公共基础必修')
data_frame.agg
data_frame.aggregate()
data_frame.get(k='课程性质')
data_frame[data_frame['课程性质']=='专业必修']

def init_course():
    cnt = 1
    for cno, cname, college_name, tname in zip(data_frame['课程号'], data_frame['课程名称'], data_frame['开课学院'], data_frame['任课教师']):
        try:
            college = College.objects.get(name=college_name)
        except ObjectDoesNotExist:
            continue
        in_year = randint(1980, 2018)
        tno = str(in_year) + "%06d" % cnt
        title = choice(['教授', '副教授', '副教授', '副教授', '副教授', '讲师', '讲师', '讲师', '讲师', '讲师'])
        # try:
        #     Course.objects.create(
        #         cno=cno,
        #         cname=cname,
        #         college=college
        #     )
        # except IntegrityError:
        #     print(len(Course.objects.all()))

        try:
            Teacher.objects.create(
                tno=tno,
                username=tname,
                password=tno,
                sex=choice([True, False]),
                edu_background=choice(['博士', '博士后']),
                title=title,
                description="学位是：" + title,
                college=college,
                in_year=in_year
            )
            cnt += 1
            print({
                'tno:': tno,
                'password:': tno,
                'username: ': tname,
                'title: ': title,
                'college: ': college,
                'in_year: ': in_year
            })
        except IntegrityError:
            print("Teacher number: %d."%len(Teacher.objects.all()))


if __name__ == '__main__':

    # print(data_frame.head())
    #
    # print(data_frame[['课程号', '课程名称', '学分', '材料科学与工程学院']][:10])
    # init_course()
    pass


