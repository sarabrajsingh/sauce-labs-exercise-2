ARG PYTHON_VERSION="3.7-slim"

# base image
FROM python:${PYTHON_VERSION}

# dump logs to stream instead of buffer (better for loggers like stackdriver)
ENV PYTHONUNBUFFERED=1

# copy requirements.txt and use pip to install
COPY ./requirements.txt ./
COPY ./main.py ./

# install requirements
RUN pip3 install -U Flask

# Expose Flask Port
EXPOSE 5000/tcp

# create runtime user for security (non-root runtime)
RUN useradd -u 1000 -m web-user
USER web-user
ENTRYPOINT ["python", "main.py"]