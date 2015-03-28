FROM ubuntu

# Install dependencies
RUN apt-get update
RUN sudo apt-get install -y ruby-full build-essential
RUN gem install jekyll therubyracer

# Move into project dir
WORKDIR /jekyll-project

# Compile Jekyll
CMD jekyll build

