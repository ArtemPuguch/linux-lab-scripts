FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
