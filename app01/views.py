from django.shortcuts import render,HttpResponse
from api import models

# Create your views here.
def index(request):
    # a.查看所有学位课并打印学位课名称以及授课老师
    # degreeCourse_list = models.DegreeCourse.objects.all().values('name','teachers__name')
    # print(degreeCourse_list)

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    # degreeCourse_list = models.DegreeCourse.objects.all().values('name','scholarship__value')
    # print(degreeCourse_list)

    # c.展示所有的专题课
    # ret = models.Course.objects.filter(degree_course__isnull=True)
    # print(ret)

    # d.查看id = 1的学位课对应的所有模块名称
    # ret = models.DegreeCourse.objects.filter(id=1).values('course__name')
    # print(ret)

    # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    # ret = models.Course.objects.filter(id=1,degree_course__isnull=True).values('name','coursedetail__why_study','coursedetail__what_to_study_brief')
    # print(ret)
    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    # obj = models.Course.objects.filter(id=1,degree_course__isnull=True).first()
    # question_list = models.OftenAskedQuestion.objects.filter(content_type__model='course')
    # print(question_list)

    # g.获取id = 1的专题课，并打印该课程相关的课程大纲
    # ret = models.Course.objects.filter(id=1,degree_course__isnull=True).values('name','coursedetail__courseoutline__title')
    # print(ret)
    # h.获取id = 1的专题课，并打印该课程相关的所有章节
    ret = models.Course.objects.filter(id=1,degree_course__isnull=True).values('name','coursechapters__name')
    print(ret)
    # i.获取id = 1的专题课，并打印该课程相关的所有课时









    return HttpResponse('查询成功')


