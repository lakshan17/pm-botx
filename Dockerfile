FROM python:3.10.5

WORKDIR /bot
COPY . /bot
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "bot"]
