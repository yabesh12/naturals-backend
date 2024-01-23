FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update
RUN groupadd -r deepuser && useradd -r -g deepuser deepuser
WORKDIR /app
COPY ./requirements.txt /app/
RUN apt -y install gcc
RUN apt install -y libmagic-dev
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8009
RUN chmod +x entry.sh
ENTRYPOINT ["/app/entry.sh"]
