FROM python:3.6.5
RUN pip install --upgrade pip
COPY . /api
WORKDIR /api
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["run.py"]