from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from accounts.views import LoginView, RegisterView, GuestRegisterView
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from carts.views import cart_detail_api_view
from .views import home_page, about_page, contact_page
from billing.views import payment_method_view, payment_method_createview
from marketing.views import MarketingPreferenceUpdateView, MailchimpWebhookView

from carts.views import cart_home

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^accounts/$', RedirectView.as_view(url='/account')),
    url(r'^account/', include("accounts.urls")),
    url(r'^accounts/', include("accounts.passwords.urls")),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^register/guest/$', GuestRegisterView.as_view(), name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
    url(r'^cart/$', cart_home, name='cart'),
    url(r'^billing/payment-method/$', payment_method_view, name='billing-payment-method'),
    url(r'^billing/payment-method/create/$', payment_method_createview, name='billing-payment-method-endpoint'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^cart/', include("carts.urls")),
    url(r'^orders/', include("orders.urls")),
    url(r'^products/', include("products.urls")),
    url(r'^search/', include("search.urls")),
    url(r'^settings/$', RedirectView.as_view(url='/account')),
    url(r'^settings/email/', MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    url(r'^webhooks/mailchimp/', MailchimpWebhookView.as_view(), name='webhooks-mailchimp'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
