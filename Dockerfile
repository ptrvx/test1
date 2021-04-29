FROM python:3

COPY test.py .

CMD [ "python", "test.py"]
