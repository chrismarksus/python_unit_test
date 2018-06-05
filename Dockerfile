FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install python3 python3-pip -y && \
    pip3 install --no-cache-dir --upgrade pip && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/cache* /tmp/* /var/tmp/* /var/lib/apt/lists/* && \
    cd /usr/bin && \
    ln -s pydoc3 pydoc && \
    ln -s python3 python && \
    ln -s python3-config python-config && \
    cd /

WORKDIR /python_unit_test

ADD requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ADD ./ ./
