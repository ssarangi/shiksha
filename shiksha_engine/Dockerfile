# We will use Ubuntu for our image
FROM ubuntu:latest

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Updating Ubuntu packages
RUN apt-get update && yes|apt-get upgrade
RUN apt-get install -y emacs

# Adding wget and bzip2
RUN apt-get install -y wget bzip2

# Add sudo
RUN apt-get -y install sudo

# Add user ubuntu with no password, add to sudo group
RUN adduser --disabled-password --gecos '' ubuntu
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
#RUN echo `pwd`
USER ubuntu
WORKDIR /home/ubuntu
RUN chmod a+rwx /home/ubuntu

# Anaconda installing
RUN wget https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh
RUN bash Anaconda3-2018.12-Linux-x86_64.sh -b
RUN rm Anaconda3-2018.12-Linux-x86_64.sh

# Set path to conda
#ENV PATH /root/anaconda3/bin:$PATH
ENV PATH /home/ubuntu/anaconda3/bin:$PATH

# Updating Anaconda packages
RUN conda update conda
RUN conda update anaconda
RUN conda update --all

RUN conda install sympy
RUN conda install -c conda-forge celery
