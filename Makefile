all:	up

up:
		docker-compose --env-file ./srcs/.env -f ./srcs/docker-compose.yml up --build

stop:
		docker stop $$(docker ps -aq)

rm:
		docker rm -f $$(docker ps -aq)
		docker volume rm srcs_postgresql

rmi:
		docker rmi -f $$(docker images -q)

clean:	rm rmi

fclean:	stop clean

.PHONY:	all mkdir up stop rm rmi