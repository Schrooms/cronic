FROM python:3.7-alpine
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP="cronic/cronic.py"
ENV FLASK_ENV=development

CMD ["flask", "run","--host=0.0.0.0"]
