FROM ubuntu

# Install dependencies
RUN apt-get update
RUN sudo apt-get install -y ruby-full build-essential python-pip
RUN gem install jekyll therubyracer
RUN pip install virtualenv

# Move into project dir
WORKDIR /jekyll-project

# Start VirtualEnv so pygments can run properly (doesnt support python 3)
RUN virtualenv -p /usr/bin/python2.7 venv
RUN source venv/bin/activate

# Compile Jekyll
CMD jekyll build

