from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from order.views import CreateOrderView, UpdateOrderStatusView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/basket/', include('basket.urls')), #cart
    path('api/v1/account/', include('account.urls')),
    path('ap/v1/orders/',CreateOrderView.as_view()),
    path('api/v1/order/<int:pk>/',
    UpdateOrderStatusView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

