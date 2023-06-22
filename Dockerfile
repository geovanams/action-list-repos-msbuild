#Imagem de container que executa o código da action
FROM python:3.8-alpine

RUN pip install requests

COPY main.py /main.py

ENTRYPOINT ["python", "/main.py"]