# djangoKafkaFastApi
sending messages from django to Kafka and subcribing FastApi to read them
we have a Django app which sends messages to a topic in kafka, also there is a fastApi subscribed to the topic and reading the message
#1 To install Kafka, zookeeper is necessary, docker compose is needed to enable and install kafka and zookeeper
docker-compose -f docker-compose-kafka.yml up -d   #takes some time to install kafka and zookeeper images
docker-compose -f docker-compose-kafka.yml down # stop containers
to make it work is important to have this in docker compose settings: 
 KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
KAFKA_AUTO_CREATE_TOPICS_ENABLE: "false"

pip install kafka

docker ps  # check kfka container
docker exec -it <kafka_container_id> bash
docker exec -it containerid bash
docker ps --filter "id=containerid" --format "{{.Image}}"   # ver la imagen que tiene el contenedor
docker-compose -f docker-compose-kafka.yml down   stop containers
docker logs containerid

# comandos en Kafka
kafka-console-consumer --bootstrap-server kafka:9092 --topic example-topic --from-beginning   # consultar todos los comandos
# crear un topico:
kafka-topics --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic example-topic
# listar topicos:
kafka-topics --list --bootstrap-server kafka:9092
# enviar un mensaje
kafka-console-producer --bootstrap-server localhost:9092 --topic example-topic



docker-compose-kafka.yml

#2 Django App:

django-admin startproject frontapp1
 cd .\frontapp1\|
 python manage.py startapp kafkaproducer
add the app to settings.py INSTALLED_APPS 
python manage.py runserver # run and check kafka is receiving messages

 django-admin subcommands
check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

create urls.py in kafkaproducer
in urls.py from the root folder add the route to the urls.py in kafkaproducer 
path('api/', include('kafkaproducer.urls')),

to add front end to  django after created as DRF
create a folder called templates inside kafkaproducer 


# Fast APi
 pip install confluent-kafka fastapi uvicorn
 create the folders and main.py file
 # run locally
uvicorn consumer.main:app --host 0.0.0.0 --port 8000 --reload
using asynccontextmanager and lifespan