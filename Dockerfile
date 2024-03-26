FROM python:latest

COPY . /paymentsystem

WORKDIR /paymentsystem
RUN pip install -r req.txt

CMD ["uvicorn", "main:app", "--reload", "--host=2.0.0.5"]