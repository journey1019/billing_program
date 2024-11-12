"""
URL configuration for billing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import AggregatedDataAPIView, GenerateBillingData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('billing.api.urls')), # API URL 추가

    path('table/', include('table.urls')),
    path('polls/', include('polls.urls')), # include: URL 패턴을 포함할 때 항상 사용
    path("cdr/", include("cdr.urls")),
    path("nr/", include("networkreport.urls")),
    path("account/", include("account.urls")),
    path("device/", include("device.urls")),
    path("pplan/", include("pplan.urls")),

    path('api/aggregated-data/', AggregatedDataAPIView.as_view(), name='aggregated-data'),
    path('billing/generate/', GenerateBillingData, name='generate_billing_data'),
]
