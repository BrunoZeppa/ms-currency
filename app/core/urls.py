from django.urls import path
from . import views

urlpatterns = [
    path('v1/currencies/', views.CurrenciesView.as_view()),#GET, POST
    path('v1/currencies/<str:name>/', views.CurrenciesView.as_view()),#GET
    path('v1/currencies/check/<str:base>/<str:quote>/', views.Check_exchange_rateView.as_view()), #GET
    path('v1/exchange/', views.Change_currencyView.as_view()),#POST
    path('v1/track_fee/', views.TrackFeeView.as_view()),#GET
    path('v1/setup/', views.SetupView.as_view()),#POST
]