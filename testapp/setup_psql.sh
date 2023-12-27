docker rm -f legoai_psql
docker run -d \
	--name legoai_psql \
	-p5432:5432 \
    -e POSTGRES_PASSWORD=pwd \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /tmp/legoai_psql_data:/var/lib/postgresql/data \
	postgres

docker exec -it legoai_psql psql -Upostgres -c 'create database legoai_apiservice'