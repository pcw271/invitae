from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from invitae import views

router = routers.DefaultRouter()
router.register('variants', views.VariantsViewSet)

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^api/', include(router.urls)),
	url('^invitae/', views.index, name='index'),
    url('', views.index, name='index')
]
