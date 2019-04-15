from django.db import models
from django.contrib.auth.models import User


# 学院
class College(models.Model):
    # 学院名
    name = models.CharField(unique=True, max_length=128)
    # 学院简称
    short_name = models.CharField(unique=True, max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'college'


# 专业
class Major(models.Model):
    # 专业名称，唯一，如：计算机科学与技术， 化学工程与工艺
    mname = models.CharField(unique=True, max_length=128)
    # 专业简称，如：计算机科学与技术--计科， 化学工程与工业--化工
    short_name = models.CharField(unique=True, max_length=10)

    # 所属学院，外键
    in_college = models.ForeignKey(to=College, on_delete=models.CASCADE)

    def __str__(self):
        return self.mname

    class Meta:
        db_table = 'major'


# 专业信息
class MajorPlan(models.Model):
    # 学年，该专业下的那个年级的学生
    year = models.IntegerField()
    # 专业名称，对应了需要的专业
    major = models.ForeignKey(to=Major, on_delete=models.CASCADE)
    # 专业计划班级数
    cls_num = models.IntegerField()
    # 专业计划人数
    people_num = models.IntegerField()
    # 毕业最低学分
    score_grad = models.IntegerField()
    # 学制：毕业需要学习的年数, 4
    stu_years = models.IntegerField()

    def __str__(self):
        return str(self.year) + '-' + str(self.major)

    class Meta:
        db_table = 'major_plan'
        unique_together = (
            'year', 'major'
        )


# 行政班
class AdmClass(models.Model):
    # 行政班名，如：计科1605
    name = models.CharField(max_length=10, unique=True)
    # 行政班所属专业，由 major.short_name + in_year + 编号（自增）构成
    # 例如：计科1605， 化工1606
    major = models.ForeignKey(to=MajorPlan, on_delete=models.CASCADE)
    people_num = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'adm_class'


# 学生
class Student(User):
    # 学号，必须10位，例如：2016011186
    sno = models.CharField(max_length=10, primary_key=True)
    # 学生姓名
    # username = models.CharField()
    # 登录所需密码
    # password = models.CharField()
    # 学生性别
    sex = models.BooleanField(default=True)
    # 目前已修学分
    score_got = models.IntegerField()
    # 所在的行政班级，外键
    in_cls = models.ForeignKey(to=AdmClass, on_delete=models.CASCADE)

    # 入学年份，用int表示即可
    in_year = models.IntegerField()

    def __str__(self):
        return self.sno

    class Meta:
        db_table = 'student'


# 教师
class Teacher(User):
    # 教师工号
    tno = models.CharField(max_length=10, primary_key=True)
    # username = models.CharField()
    # password = models.CharField()
    sex = models.BooleanField(default=True)

    # 教师所属学院
    college = models.ForeignKey(to=College, on_delete=models.CASCADE)
    # 教师入职的年份
    in_year = models.IntegerField()
    # 学历，在个人信息中显示。如：博士，博士后...
    edu_background = models.CharField(null=True, max_length=128)
    # 在校职位，如：教授，副教授，讲师等
    title = models.CharField(default='讲师', max_length=128)
    # 教师个人简介，可空
    description = models.TextField(null=True)

    def __str__(self):
        return self.tno

    class Meta:
        db_table = 'teacher'


# 课程信息
class Course(models.Model):
    # 课程编号，长度必须为9位，如：MAT13004C
    # 3位英文+5位数字+一位英文
    cno = models.CharField(max_length=9, primary_key=True)
    # 课程名称，需要与编号对应
    cname = models.CharField(max_length=128)
    # 开课学院，需要从学院中选取对应的老师来上课
    college = models.ForeignKey(to=College, on_delete=models.CASCADE)

    def __str__(self):
        return self.cno

    class Meta:
        db_table = 'course'


# 专业对应课程信息
class MajorCourses(models.Model):
    # 课程编号
    cno = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    # cname = cno.cname
    # 对应到的专业计划信息
    # 注意，这里都是外键，需要传入的是对象引用
    mno = models.ForeignKey(to=MajorPlan, on_delete=models.CASCADE)

    # 该门课程在该专业对应的性质，选修 or 必修，默认必修
    cproper = models.BooleanField(default=True)
    # 该门课程在该专业对应的学分
    score = models.IntegerField()
    # 该门课程在该专业对应的学时
    chour = models.IntegerField()

    # 学期, 默认表示上学期
    semester = models.BooleanField(default=True)

    def __str__(self):
        return str(self.cno) + '-' + str(self.mno)

    class Meta:
        # 设置数据库中表的显示名称
        db_table = 'major_courses'
        # 设置数据联合主键，为全码
        unique_together = (
            'cno', 'mno'
        )


# 教室
class ClassRoom(models.Model):
    # 教室编号，如：A302， B阶202
    crno = models.CharField(primary_key=True, max_length=128)
    # 教室类型，阶教180人，中等教室120人，小教室50人
    # 教室类型需要和教室编号对应
    crtype = models.CharField(null=False, max_length=10)

    # 教室能够容纳的学生数目，需要与类型对应
    contain_num = models.IntegerField()

    def __str__(self):
        return self.self.crno

    class Meta:
        db_table = 'class_room'


# 教师授课
class Teaching(models.Model):
    # 教授课程的教师工号
    tno = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    # 教授课程的教师名称，为了显示方便，可以冗余
    # tname = tno.username
    # 这门课对应所在的专业培养计划
    mcno = models.ForeignKey(to=MajorCourses, on_delete=models.CASCADE)
    # 教师给的本课程的平时分权重，如：0.3, 0.2 ...
    weight = models.FloatField()

    def __str__(self):
        return self.tno

    class Meta:
        db_table = 'teaching_table'
        unique_together = (
            'tno', 'mcno'
        )


# TODO::完成候选课表和选课后表
# 候选课表
class CourseForSelect(models.Model):

    class Meta:
        db_table = 'course_for_select'
    pass


# 选课后表
class CourseSelected(models.Model):
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    mcno = models.ForeignKey(to=MajorCourses, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        db_table = 'course_selected'
    pass


class CourseScore(models.Model):
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    cno = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    tno = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    tcls_name = models.CharField(max_length=128)
    score_proper = models.CharField(max_length=128)
    cscore = models.IntegerField()
    score = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return "-".join(self.sno, self.cno, self.score)

    class Meta:
        db_table = 'course_score'
        unique_together = (
            'sno',
            'cno'
        )



