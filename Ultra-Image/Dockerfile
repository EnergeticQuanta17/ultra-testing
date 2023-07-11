FROM ultralytics/ultralytics

RUN apt update

RUN apt install git -y

COPY . /app

WORKDIR /app

CMD python3 model.py