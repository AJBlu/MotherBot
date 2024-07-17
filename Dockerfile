FROM python:3.12

ADD main.py .
ADD responses.py .
ADD .env .

RUN pip install discord.py
RUN pip install python-dotenv

CMD ["python", "./main.py"]