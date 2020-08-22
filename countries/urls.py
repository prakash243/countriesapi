from django.contrib import admin
from django.urls import path, include
from countries import views
from countries.views import TaskViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todo', TaskViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    path('countries/', views.countries_list, name="countries_list"),
    path('countries/<int:pk>', views.countries_detail, name="countries_detail"),
    path('api/', include(router.urls)),
    path('', include(router.urls)),
]
