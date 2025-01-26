from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from kafka import KafkaProducer

class KafkaProducerView(APIView):
    def post(self, request):
        # Configurar el productor de Kafka
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        topic = 'example-topic'
        message = request.data.get('message', 'Default Message')
        
        # Enviar mensaje
        producer.send(topic, message.encode('utf-8'))
        producer.close()

        return JsonResponse({'status': 'Message sent', 'message': message})

class KafkaFrontendView(APIView):
    def get(self, request):
        return render(request, 'frontend.html')