from fastapi import FastAPI
from confluent_kafka import Consumer, KafkaException
from contextlib import asynccontextmanager
import asyncio

# Configuración de Kafka
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'example-group',
    'auto.offset.reset': 'earliest',
}
consumer = Consumer(consumer_config)
consumer.subscribe(['example-topic'])

@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_event_loop()

    async def consume():
        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaException._PARTITION_EOF:
                        continue
                    else:
                        print(f"Error: {msg.error()}")
                else:
                    print(f"Received message: {msg.value().decode('utf-8')}")
        except asyncio.CancelledError:
            print("Kafka consumer task was cancelled.")
        finally:
            consumer.close()

    task = loop.create_task(consume())
    try:
        yield  # Aquí se inicializa la aplicación
    finally:
        task.cancel()  # Cancela la tarea al cerrar la aplicación
        await task  # Espera a que la tarea se complete

# Instancia de FastAPI con ciclo de vida personalizado
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"status": "Kafka consumer is running"}