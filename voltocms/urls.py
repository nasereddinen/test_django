from django.urls import path 
import voltocms.views as views
app_name = "company"

urlpatterns = [
    path('create_company/', views.CreateCompanyView.as_view(), name="create_company"),
    path('company_account/<int:compte_id>/', views.CompanyAccountView.as_view(), name="company_account"),
    path('get_company_with_siret/<str:siret>/', views.GetCompanyWithSiretView.as_view(), name="get_company_with_siret"),
    path('add_energy_counter/', views.AddCounterView.as_view(), name="add_energy_counter"),
    path('energy_company_counter/<int:company_id>/', views.GetEnergyCounterWithCompanyView.as_view(), name="get_energy_counter"),
    path('energy_account_counter/<int:account_id>/', views.GetEnergyCounterWithAccountView.as_view(), name="get_energy_couter_with_account"),
    path('add_contract/', views.CalculateEnergyConsumptionView.as_view(), name="add_contract"),
]