from django.urls import path
from refinitiv import views

urlpatterns = [
    path('api/corps/database', views.AllCompanyDataBase.as_view(), name='show-company-database'),
    path('api/corps/csv', views.AllCompanyCSV.as_view(), name='show-company-csv'),
    path('api/corps/esgscore/<str:ticker>/database', views.GetCompanyByTickerDataBase.as_view(), name='ticker-company-database'),
    path('api/corps/esgscore/<str:ticker>/csv', views.GetCompanyByTickerCSV.as_view(), name='ticker-company-csv'),
]