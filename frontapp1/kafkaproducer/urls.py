from django.urls import path
from .views import KafkaProducerView, KafkaFrontendView

urlpatterns = [
    path('produce/', KafkaProducerView.as_view(), name='kafka-produce'),
    path('frontend/', KafkaFrontendView.as_view(), name='kafka-frontend'),
]