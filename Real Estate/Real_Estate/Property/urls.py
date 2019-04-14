from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterProperty.as_view(), name='register_property'),
    path('update/', UpdateProperty.as_view(), name='update_property'),
    path('update/<int:pk>', UpdatePropertyForm.as_view(), name='update_property_form'),
    path('list/', ViewAllProperty.as_view(), name='list_all_property'),
    path('details/<int:pk>', ViewSpecificProperty.as_view(), name='detailed_view_property'),
    path('delete/<int:pk>', DeleteProperty.as_view(), name='delete_property'),
    path('delete/', DeletePropertyList.as_view(), name='delete_property_list'),
    path('access/', access),
    path('query/<int:id>', handlequery, name="handle_query")
]
