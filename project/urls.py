from django.contrib import admin
from django.urls import path, include
from sneakers import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('sneakers/<int:id>/', views.categor_elements, name='categor_elements'),
    path('detal/<int:id>/', views.detail_news, name='detail_news'),
    path('sneakers/', views.main, name='main'),
    path('workspace/', include('workspace.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

