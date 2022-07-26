FROM python:3.10

WORKDIR /bot

COPY requirements.txt /bot/

RUN pip3 install -U -r requirements.txt

COPY . /bot

CMD python3 -m bot
