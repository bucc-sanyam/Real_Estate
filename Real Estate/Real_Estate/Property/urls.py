from django.urls import path
from .views import *

urlpatterns = [
    path('register/', PropertyOperations.as_view(), name='register_property'),
    path('update/<int:pk>', UpdateProperty.as_view(), name='update_property'),
    path('list/', ViewAllProperty.as_view(), name='list_all_property'),
    path('details/<int:pk>', ViewSpecificProperty.as_view(), name='detailed_view_property'),
]
