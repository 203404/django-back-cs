from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static

#import Register 
from Register.views import RegistroView

# Serializers define the API representation.
class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    #URL de registro
    re_path(r'^api/v1/create_user', RegistroView.as_view(), name='create_user'),
    re_path(r'^api/', include('Login.urls')),
    re_path(r'^api/v1/load_image/', include('loadImage.urls')),
    re_path(r'^api/v1/primer_componente/', include('primerComponente.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
#(NOT USED, IGNORE)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)