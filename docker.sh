#!/bin/bash

if [ "$1" == 'build' ]; then
	docker build --no-cache -t jekyll-build .
elif [ "$1" == 'run' ]; then
	docker run -it --rm -v `pwd`/shanereustle/:/jekyll-project jekyll-build
else
	echo 'Usage: ./docker.sh [build|run]'
fi

