# - Dockerfile configurations
FROM python:3.11.2-alpine3.16
LABEL DESCRIPTION="user-api" 
COPY requirements.txt /
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
WORKDIR /usr/src/app
COPY . .
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "81" , "--reload"]

# docker image build -t user-api:latest .

# docker container run --rm -it -v ${pwd}:/usr/src/app --env-file .env -p 81:81 --name user-api user-api:latest