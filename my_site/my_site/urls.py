
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("api.urls"),
    path('user/', include("practic_ap.urls"))     )

]
