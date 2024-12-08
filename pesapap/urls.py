from django.urls import path
from pesapap.views import StkCallbackView, PaymentView, DefaultHomeView,ViewMpesaPayments, ViewMpesaRequests,payvia_webapp

urlpatterns = [
    path('stk-callback/', StkCallbackView.as_view()),
    path('pay', PaymentView.as_view()),
    path('payments', ViewMpesaPayments.as_view()),
    path('requests', ViewMpesaRequests.as_view()),
    path('webapp', payvia_webapp),
    path('', DefaultHomeView.as_view()),
]

