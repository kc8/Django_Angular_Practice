from django.conf.urls import url
#from django.views.generic import TemplateView
#from .api import ListApi, CardApi #replaced with ListViewSet and CardViewSet functionality


#code for the router:
from .api import ListViewSet, CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter() #creates mappings for a general API
router.register(r'lists', ListViewSet) #creates views for these views.
router.register(r'cards', CardViewSet)

urlpatterns = router.urls #tells the urlpatterns to use the router from above


# code from original list view(). Repalced with router functionality above
#urlpatterns = [
#    url(r'^lists$', ListApi.as_view()),
#    url(r'^cards$', CardApi.as_view()),
#    url(r'^home', TemplateView.as_view(template_name="scrumboard/home.html")),
#]

#r = raw string. $ matches anything at the end
# the seconds arguemnt is a view class.
# url needs a function as an argument
# don't forget tht imports
# the second argument is a class with a function which will provide the view.
#Must import the API fields (from the api.py)
# make sure to add the projcet to he app url.py