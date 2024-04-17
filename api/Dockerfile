FROM python:3.10

WORKDIR /ehusports_api

RUN pip install --upgrade pip

COPY requirements.txt /ehusports_api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /ehusports_api/requirements.txt

COPY ./app /ehusports_api/app
COPY ./images /ehusports_api/images

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

