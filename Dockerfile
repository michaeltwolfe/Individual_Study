FROM python:3.7
COPY . project
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "app.py"]
