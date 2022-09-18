FROM python

ARG ENVIRONMENT="qa"

ENV ENVIRONMENT=${ENVIRONMENT}

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "__init__.py"]