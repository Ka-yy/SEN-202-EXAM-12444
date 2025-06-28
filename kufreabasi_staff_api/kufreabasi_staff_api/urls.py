from django.contrib import admin
from django.urls import path


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

app_name = 'staff_management'

# Optional: Using DRF Router for some endpoints
# router = DefaultRouter()
# router.register(r'addresses', views.AddressViewSet)
urlpatterns = [
    # Address endpoints
    path('addresses/', views.AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', views.AddressDetailView.as_view(), name='address-detail'),
    path('addresses/search/', views.AddressSearchView.as_view(), name='address-search'),
    
    # Manager endpoints
    path('managers/', views.ManagerListCreateView.as_view(), name='manager-list-create'),
    path('managers/<int:pk>/', views.ManagerDetailView.as_view(), name='manager-detail'),
    path('managers/<int:pk>/addresses/', views.ManagerAddressView.as_view(), name='manager-addresses'),
    path('managers/<int:manager_id>/addresses/<int:address_id>/', views.ManagerAddressDetailView.as_view(), name='manager-address-detail'),
    
    # Intern endpoints
    path('interns/', views.InternListCreateView.as_view(), name='intern-list-create'),
    path('interns/<int:pk>/', views.InternDetailView.as_view(), name='intern-detail'),
    path('interns/<int:pk>/addresses/', views.InternAddressView.as_view(), name='intern-addresses'),
    path('interns/<int:intern_id>/addresses/<int:address_id>/', views.InternAddressDetailView.as_view(), name='intern-address-detail'),
    
    # Polymorphism demonstration endpoints
    path('staff/roles/', views.staff_roles_view, name='staff-roles'),
    path('staff/summary/', views.staff_summary_view, name='staff-summary'),
    path('staff/with-addresses/', views.staff_with_addresses_view, name='staff-with-addresses'),
    
    # Filtering and search endpoints
    path('managers/by-department/', views.ManagersByDepartmentView.as_view(), name='managers-by-department'),
    path('interns/by-mentor/', views.InternsByMentorView.as_view(), name='interns-by-mentor'),
    path('staff/by-location/', views.StaffByLocationView.as_view(), name='staff-by-location'),

]
    