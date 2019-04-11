import os
import re
import math
from random import choice, randint, choices
from app.models import College, Major, AdmClass, Student,\
    Teacher, Course, ClassRoom, MajorPlan, Teaching


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

major_names = {
    '信息科学与技术学院': [
        ['计算机科学与技术', '计科'],
        ['自动化控制', '自控'],
        ['', '测控'],
        ['通信工程', '信工'],
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


def create_college():
    for i in college_names:
        print(i)
        college = College.objects.create(name=i[0], short_name=i[1])
        print(college)
        college.save()


def create_major():
    pass


def create_admin_class():
    pass


def create_student():
    pass


if __name__ == '__main__':
    create_college()
