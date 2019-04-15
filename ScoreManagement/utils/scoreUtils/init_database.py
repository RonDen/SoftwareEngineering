import os
import re
import math
from random import choice, randint, choices
from app.models import College, Major, AdmClass, Student,\
    Teacher, Course, ClassRoom, MajorPlan, Teaching
from django.db.utils import IntegrityError


class CollegeInit:
    college_names = [
        ['信息科学与技术学院', '信息学院'],
        ['化学工程学院', '化工学院'],
        ['材料科学与工程学院', '材料学院'],
        ['机电工程学院', '机电学院'],
        ['文法学院', '文法学院'],
        ['经济管理学院', '经管学院'],
        ['理学院', '理学院'],
        ['生命科学与技术学院', '生命学院'],
        ['巴黎居里工程师学院', '巴黎居里工程师学院'],
    ]

    def __init__(self):
        for i in self.college_names:
            college = College.objects.create(name=i[0], short_name=i[1])
            try:
                college.save()
            except:
                print("Except happen: " + str(len(College.objects.all())))


class MajorInit:
    major_names = {
        '信息科学与技术学院': [
            ['计算机科学与技术', '计科', 192],
            ['自动化控制', '自控', 192],
            ['测控技术与仪器', '测控', 193],
            ['电子信息工程', '信工', 192],
            ['数字媒体艺术', '数媒', 173],
        ],
        '化学工程学院': [
            ['化学工程与工艺', '化工'],
            ['能源工程', '能源'],
            ['环境工程', '环工'],
        ],
        '材料科学与工程学院': [
            ['高分子材料与技术', '高材'],
            ['材料科学与技术', '材料'],
            ['功能材料', '功材'],
        ],
        '机电工程学院': [
            ['']
        ],
        '文法学院': [
            ['英语']
        ],
        '经济管理学院': [
            []
        ],
        '理学院': [
            []
        ],
        '生命科学与技术学院': [
            []
        ],
        '巴黎居里工程师学院': [
            []
        ]
    }

    def information_init(self):
        college = College.objects.get(name='信息科学与技术学院')
        for m in self.major_names['信息科学与技术学院']:
            try:
                maj = Major.objects.create(in_college=college, mname=m[0], short_name=m[1])
                maj.save()
            except IntegrityError:
                print(len(Major.objects.all()))

    def information_major_plan_init(self):
        years = [2015, 2016, 2017, 2018]
        for year in years:
            for maj in Major.objects.all():
                cls_num=choice([3, 4, 5, 6])
                try:
                    majp = MajorPlan.objects.create(
                        year=year,
                        major=maj,
                        cls_num=cls_num,
                        score_grad=choice([192, 193]),
                        people_num=35*cls_num,
                        stu_years=4
                    )
                    majp.save()
                except IntegrityError:
                    print(len(MajorPlan.objects.all()))

    def information_class_init(self):
        major_plan_set = MajorPlan.objects.all()
        cnt = 1
        for maj in major_plan_set:
            cls_base_name = maj.major.short_name + str(maj.year)[2:]
            for j in range(1, maj.cls_num+1):
                cls_name = cls_base_name + "%02d" % j
                print(cls_name)
                try:
                    cls = AdmClass.objects.create(name=cls_name, major=maj, people_num=maj.people_num)
                    cls.save()
                except IntegrityError:
                    print(len(AdmClass.objects.all()))

    def information_student_init(self):
        last_name = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        first_name = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
        score_gots = {
            2015: 190,
            2016: 180,
            2017: 100,
            2018: 56
        }

        adm_class_set = AdmClass.objects.all()
        cnt = 1
        for cls in adm_class_set:
            for j in range(cls.people_num + 1):
                year = cls.major.year
                prefix = str(year)
                subfix = "%06d" % cnt
                sno = prefix + subfix
                cnt += 1
                name = choice(last_name) + "".join(choice(first_name) for i in range(2))
                print({
                    'name': name,
                    'sno': sno
                })
                # try:
                #     stu = Student.objects.create(
                #         sno=sno,
                #         username=name,
                #         password=sno,
                #         sex=choice([True, False]),
                #         in_cls=cls,
                #         in_year=cls.major.year,
                #         score_got=score_gots[year]
                #     )
                #     stu.save()
                # except IntegrityError:
                #     print(len(Student.objects.all()))


class TeacherInit:
    last_name = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    first_name = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'

    sex = choice([True, False])
    college = College.objects.get(name='信息科学与技术学院')
    in_year = randint(1980, 2018)

    pass



if __name__ == '__main__':
    # college_init = CollegeInit()
    major_init = MajorInit()
    # major_init.information_init()
    # major_init.information_major_plan_init()
    # major_init.information_class_init()
    major_init.information_student_init()
    pass

