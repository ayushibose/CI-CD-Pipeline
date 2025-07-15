FROM python:3.13.4
WORKDIR /main
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]