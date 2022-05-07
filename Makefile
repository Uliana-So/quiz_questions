all:	up

up:
	docker-compose --env-file ./srcs/.env -f ./srcs/docker-compose.yml up --build -d

down:
	docker-compose -f ./srcs/docker-compose.yml down

stop:
	docker-compose -f ./srcs/docker-compose.yml stop

rm:
	docker-compose -f ./srcs/docker-compose.yml rm -s -v -f
	docker volume rm srcs_postgresql

clean:	rm

fclean:	stop clean

.PHONY:	all up down stop rm
