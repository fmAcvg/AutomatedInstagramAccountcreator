FROM python:3.9 WORKDIR /instabot

RUN pip install selenium-wire re time



CMD ["python", "insta.py"]