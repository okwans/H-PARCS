TAG:=1
REGISTRY=tms.staging.hi-parking.net:5000
IMAGE_NAME=raidea-api-test

PWD=$(shell pwd)

NAME=$(shell id -un)
NUM=$(shell id -u)

all:
	@echo "Usage: make <build_dbg|run|exec|rm|build_run|test|push>"

build: Dockerfile
	@echo "= build docker images"
	sudo docker build -f Dockerfile --rm -t ${IMAGE_NAME}:${TAG} .

run: rm
	@echo "= launch container"
	sudo docker run -d -it --name ${IMAGE_NAME} -v ${PWD}:/root -v ${PWD}/result:/result ${IMAGE_NAME}:${TAG} bash

exec:
	@echo "= enter to the container"
	sudo docker exec -it ${IMAGE_NAME} bash

rm:
	@echo "= remove old container"
	@sudo docker ps -a | grep ${IMAGE_NAME} > /dev/null; [ $$? -ne 0 ] || \
	  sudo docker rm -f ${IMAGE_NAME}

test: build
	# @CCI
        #cd ~/
	#git clone ssh://github.com/tmspd3/raidea_api_test
	#cd raidea_api_test
	@echo "= test with docker image"
	sudo rm -rf reports
	sudo docker run --rm -it -v ${PWD}:/root -v ${PWD}/result:/result ${IMAGE_NAME}:${TAG} bash bdd_run.sh
	bash upload.sh

push: build
	@echo "= push docker run image"
	sudo docker tag ${REGISTRY}/${IMAGE_NAME}:${TAG} ${REGISTRY}/${IMAGE_NAME}:latest
	sudo docker push ${REGISTRY}/${IMAGE_NAME}:${TAG}
	sudo docker push ${REGISTRY}/${IMAGE_NAME}:latest


