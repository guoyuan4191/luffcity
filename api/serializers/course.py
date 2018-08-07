from rest_framework import serializers
from api import models

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)
    level_name = serializers.CharField(source='get_level_display')

# 上课代码练习
# class CourseModelSerializer(serializers.ModelSerializer):
#     level_name = serializers.CharField(source='get_level_display')
#     # OneToOneField序列化反向查询按表名.属性可以取到一对一表中的字段值
#     hours = serializers.CharField(source='coursedetail.hours')
#     course_slogan = serializers.CharField(source='coursedetail.course_slogan')
#     recommend_courses = serializers.SerializerMethodField()
#
#     class Meta:
#         model = models.Course
#         fields = ['id','name','level_name','hours','course_slogan','recommend_courses']
#
#     # 多对多表不能直接表名.属性取值
#     def get_recommend_courses(self,row):
#         recommend_list = row.coursedetail.recommend_courses.all()
#         return [{'id':item.id,'name':item.name} for item in recommend_list]

# class DegreeCourseModelSerializer(serializers.ModelSerializer):
#     teachers = serializers.SerializerMethodField()
#     scholarship_list = serializers.SerializerMethodField()
#
#
#     class Meta():
#         model = models.DegreeCourse
#         fields = ['id','name','teachers','scholarship_list']
#
#     # a.查看所有学位课并打印学位课名称以及授课老师
#     def get_teachers(self,row):
#         teacher_list = []
#         for teacher in row.teachers.all():
#             teacher_list.append(teacher)
#         return [{'id':teacher.id,'name':teacher.name} for teacher in teacher_list]
#
#     # b.查看所有学位课并打印学位课名称以及学位课的奖学金
#     def get_scholarship_list(self,row):
#         scholarship_list = row.scholarship_set.all()
#         return [{'value':scholarship.value,'time_percent':scholarship.time_percent} for scholarship in scholarship_list]

# a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourseModelTeacherSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()
    class Meta():
        model = models.DegreeCourse
        fields = ['id','name','teachers']

    def get_teachers(self,row):
        teacher_list = []
        for teacher in row.teachers.all():
            teacher_list.append(teacher)
        return [{'id':teacher.id,'name':teacher.name} for teacher in teacher_list]


# b.查看所有学位课并打印学位课名称以及学位课的奖学金
class DegreeCourseScholarshipModelSerializer(serializers.ModelSerializer):
    scholarship_list = serializers.SerializerMethodField()

    class Meta():
        model = models.DegreeCourse
        fields = ['name','scholarship_list']

    def get_scholarship_list(self,row):
        scholarship_list = row.scholarship_set.all()
        return [{'value':scholarship.value,'time_percent':scholarship.time_percent} for scholarship in scholarship_list]


# c.展示所有的专题课
class  CoursesAllViewModelSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Course
        fields = ['id','name']

# d. 查看id=1的学位课对应的所有模块名称
class DegreeCourseDetailModelSerializer(serializers.ModelSerializer):
    course_list = serializers.SerializerMethodField()

    class Meta():
        model = models.DegreeCourse
        fields = ['id', 'course_list']
    def get_course_list(self,row):
        course_list = row.course_set.all()
        return [{'name': course.name} for course in course_list]


# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class CourseModelSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='get_level_display')
    why_study = serializers.CharField(source='coursedetail.why_study')
    what_to_study_brief = serializers.CharField(source='coursedetail.what_to_study_brief')
    recommend_courses = serializers.SerializerMethodField()
    ask_list = serializers.SerializerMethodField()
    courseoutline_list = serializers.SerializerMethodField()
    coursechapter_list = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['id','name','level_name','why_study','what_to_study_brief','recommend_courses','ask_list','courseoutline_list','coursechapter_list']

    def get_recommend_courses(self,row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [{'id':item.id,'name':item.name} for item in recommend_list]

    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    def get_ask_list(self,row):
        ask_list = row.asked_question.all()
        return [{'question':ask.question,'answer':ask.answer} for ask in ask_list]

    # g.获取id = 1的专题课，并打印该课程相关的课程大纲
    def get_courseoutline_list(self,row):
        courseoutline_list = row. coursedetail.courseoutline_set.all()
        return [{'title': courseoutline.title, 'content': courseoutline.content} for courseoutline in courseoutline_list]

    # h.获取id = 1的专题课，并打印该课程相关的所有章节
    def get_coursechapter_list(self,row):
        coursechapter_list = row.coursechapters.all()
        return [{'name':chapter.name,'chapter':chapter.chapter,'summary':chapter.summary,'pub_date':chapter.pub_date} for chapter in coursechapter_list]