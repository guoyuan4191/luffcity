from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
from rest_framework.response import Response
from api.serializers.course import CourseSerializer,CourseModelSerializer,DegreeCourseScholarshipModelSerializer,DegreeCourseModelTeacherSerializer,CoursesAllViewModelSerializer,DegreeCourseDetailModelSerializer
from api import models
from api.utils.response import BaseResponse
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class CoursesView(APIView):
    def get(self,request,*args,**kwargs):
        '''
        获取所有专题课信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # ret = {'code':1000,'data':None,'error':None}
        # 将字典封装成一个类，用ret.属性名去调用，简化代码
        ret = BaseResponse()
        try:
            queryset = models.Course.objects.all()
            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)
            # 分页之后的结果序列化
            # ser = CourseSerializer(course_list,many=True)
            ser  = CourseModelSerializer(course_list,many=True)
            # ret['data'] = ser.data
            ret.data = ser.data

        except Exception as e:
            # ret['code'] = 500
            ret.code = 500
            # ret['error'] = '获取数据失败'
            ret.error = '获取数据失败'

        return Response(ret.dict)

# 上课代码练习
# class CourseDetailView(APIView):
#     def get(self,request,pk,*args,**kwargs):
#         ret = BaseResponse()
#         try:
#             course = models.Course.objects.filter(id=pk).first()
#             # ser = CourseSerializer(course)
#             ser = CourseModelSerializer(course)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = '获取数据失败'
#         return Response(ret.dict)

# class DegreeCourseView(APIView):
#     def get(self,request,*args,**kwargs):
#         ret = BaseResponse()
#         try:
#             degree_queryset = models.DegreeCourse.objects.all().order_by('id')
#             # print(queryset)
#             page = PageNumberPagination()
#             degree_list = page.paginate_queryset(degree_queryset, request, self)
#
#             ser = DegreeCourseModelSerializer(degree_list,many=True)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = '获取数据失败'
#
#         return Response(ret.dict)

# a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourseTeacherView(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            degree_queryset = models.DegreeCourse.objects.all().order_by('id')
            # print(queryset)
            page = PageNumberPagination()
            degree_list = page.paginate_queryset(degree_queryset, request, self)
            ser = DegreeCourseModelTeacherSerializer(degree_list,many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)

# b.查看所有学位课并打印学位课名称以及学位课的奖学金
class DegreeCourseScholarshipView(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            degree_queryset = models.DegreeCourse.objects.all().order_by('id')
            # print(queryset)
            page = PageNumberPagination()
            degree_list = page.paginate_queryset(degree_queryset, request, self)

            ser = DegreeCourseScholarshipModelSerializer(degree_list,many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)

# c.展示所有的专题课
class CoursesAllView(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            queryset = models.Course.objects.filter(degree_course__isnull=True).order_by('id')
            print(queryset)
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)
            ser = CoursesAllViewModelSerializer(course_list,many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)


# d. 查看id=1的学位课对应的所有模块名称
class DegreeCourseDetail(APIView):
    def get(self, request,pk, *args, **kwargs):
        ret = BaseResponse()
        try:
            queryset = models.DegreeCourse.objects.filter(id=pk)
            print(queryset)
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)
            ser = DegreeCourseDetailModelSerializer(course_list, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)

# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class CourseDetailView(APIView):
    def get(self,request,pk,*args,**kwargs):
        ret = BaseResponse()
        try:
            course = models.Course.objects.filter(id=pk).first()
            ser = CourseModelSerializer(course)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)

