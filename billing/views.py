from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.utils.http import is_safe_url

import stripe

stripe.api_key = "sk_test_yT2kdPo6H6R4ux82MsyrkPEG"
STRIPE_PUB_KEY = 'pk_test_Bz1MpNExcRPDzRW8oJPkdZUc'


def payment_method_view(request):
    #next_url =
    # if request.user.is_authenticated():
    #     billing_profile = request.user.billingprofile
    #     my_customer_id = billing_profile.customer_id

    # billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    # if not billing_profile:
    #     return redirect("/cart")
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})

def payment_method_createview(request):
    if request.method == "POST" and request.is_ajax():
        print(request.POST)
        return JsonResponse({"message":"Done"})
    return HttpResponse("error", status=401)