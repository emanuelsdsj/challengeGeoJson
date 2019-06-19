from django.urls import path
from .views import PartnersView, PartnersDetailsView, PartnersClosestView, gitJsonView, gitJsonDetailsView, gitJsonClosest
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
	# Database data
    path('partners/', PartnersView.as_view(), name="allPartners"),
    path('partners/<int:pk>/', PartnersDetailsView.as_view(), name="details"),
    path('partners/closest/<str:lat>/<str:lon>/', PartnersClosestView.as_view(), name="closestCoord"),
    # GitHub Json Test
    path('gitjson/', gitJsonView.as_view(), name="allPartnersJSON"),
    path('gitjson/<int:num>/', gitJsonDetailsView.as_view(), name="detailsJSON"),
    path('gitjson/closest/<str:lat>/<str:lon>/', gitJsonClosest.as_view(), name="closestCoordJSON"),
}
urlpatterns = format_suffix_patterns(urlpatterns)