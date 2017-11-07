from django.conf.urls import url,include
from organizations.views import OrgList,UserAskFormView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView,UserFavView,TeacherListView,TeacherDetailView
from django.conf.urls.static import static
from jiaoyu.settings import MEDIA_ROOT,MEDIA_URL

urlpatterns = [
    url(r'^org_list/$',OrgList.as_view(),name="org_list"),
    url(r'^user_ask/$',UserAskFormView.as_view(),name='user_ask'),
    url(r'^org_home/(?P<org_id>.*)/$',OrgHomeView.as_view(),name='org_home'),
    url(r'^org_course/(?P<org_id>.*)/$',OrgCourseView.as_view(),name='org_course'),
    url(r'^org_desc/(?P<org_id>.*)/$',OrgDescView.as_view(),name='org_desc'),
    url(r'^org_teacher/(?P<org_id>.*)/$', OrgTeacherView.as_view(), name='org_teacher'),
    url(r'^add_fav/$',UserFavView.as_view(),name='add_fav'),
    url(r'^teacher_list/$',TeacherListView.as_view(),name='teacher_list'),
    url(r'^teacher_detail/(?P<teacher_id>.*)/$',TeacherDetailView.as_view(),name='teacher_detail'),
]+static(MEDIA_URL,document_root=MEDIA_ROOT)
