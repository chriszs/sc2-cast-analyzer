FROM python:3.7

RUN apt-get update && apt-get install -y --no-install-recommends \
		ffmpeg \
		tesseract-ocr \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pipenv

# nodejs nodejs-npm

# -- Install Application into container:
RUN set -ex && mkdir /app

WORKDIR /app

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pipenv install 
#--deploy --system

COPY . /app

CMD pipenv run python main.py
