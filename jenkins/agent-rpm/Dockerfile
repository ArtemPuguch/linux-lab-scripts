FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && apt-get install -y \
    rpm \
    rpm2cpio \
    build-essential \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
