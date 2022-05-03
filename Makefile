all:	mkdir up

# mkdir:
# 		echo "Create folders"
# 		mkdir -p ~/data/db
# 		mkdir -p ~/data/wp
# 		mkdir -p ~/data/ad
# 		mkdir -p ~/data/rd

up:
		docker-compose -f ./srcs/docker-compose.yml up --build

stop:
		docker stop $$(docker ps -aq)

rm:
		docker rm -f $$(docker ps -aq)
		docker volume rm mysql
		docker volume rm wordpress
		docker volume rm adminer
		docker volume rm redis
		rm -fr ~/data

rmi:
		docker rmi -f $$(docker images -q)

clean:	stop rm

fclean:	clean rmi

.PHONY:	all mkdir up stop rm rmi