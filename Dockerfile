FROM ubuntu

# Install dependencies
RUN apt-get update
RUN sudo apt-get install -y ruby-full
RUN gem install jekyll

# Move into project dir
WORKDIR /jekyll-project

# Compile Jekyll
CMD jekyll build

