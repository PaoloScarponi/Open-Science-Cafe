# base image definition
FROM python:3.10.11-bullseye@sha256:b48e216f7c4adcf24fecd7016f3b8ead76866a19571819f67f47c1ccaf899717

# group and user creation
RUN addgroup --system app && adduser --system --group app

# user switch
USER app

# work directory definition
WORKDIR /home/app

# requirements file copy and dependency installation
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# required file copy
COPY ./modules ./modules
COPY app.py app.py

# container execution command
CMD python -m uvicorn app:app --host 0.0.0.0 --port $PORT
