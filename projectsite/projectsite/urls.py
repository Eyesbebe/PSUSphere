from studentorg.views import HomePageview, OrganizationList
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'), 
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
]