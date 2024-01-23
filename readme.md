user=airflow
pass=airflow


Exec 
```
docker-compose ps 
docker exec -it <NAME> /bin/bash

```
Flower
```
docker-compose --profile flower up -d  
```


Config File
```
docker cp dagger-airflow-scheduler-1:/opt/airflow/airflow.cfg
```

Postgresql
```
psql -Uairflow
```