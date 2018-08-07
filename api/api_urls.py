from django.conf.urls import url
from api.views import course

urlpatterns = [
    # url(r'degree_courses/$',course.DegreeCourseView.as_view()),
    # a.查看所有学位课并打印学位课名称以及授课老师
    url(r'degree_courses_teacher/$',course.DegreeCourseTeacherView.as_view()),
    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    url(r'degree_courses_scholarship/$', course.DegreeCourseScholarshipView.as_view()),
    # c.展示所有的专题课
    url(r'courses_all/$', course.CoursesAllView.as_view()),
    # id=1的学位课详情
    url(r'degree_courses/(?P<pk>\d+)/$',course.DegreeCourseDetail.as_view()),
    url(r'courses/$', course.CoursesView.as_view()),
    # id=1的专题课详情
    url(r'courses/(?P<pk>\d+)/$',course.CourseDetailView.as_view()),

]