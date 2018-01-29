# [START docker]

# The Google App Engine python runtime is Debian Jessie with Python installed
# and various os-level packages to allow installation of popular Python
# libraries. The source is on github at:
# https://github.com/GoogleCloudPlatform/python-docker
FROM gcr.io/google_appengine/python

# Create a virtualenv for the application dependencies.
# # If you want to use Python 3, add the -p python3.4 flag.
RUN virtualenv /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install -r /app/requirements.txt
ADD . /app

COPY start.sh /start.sh

EXPOSE 80 8000


CMD gunicorn -b :$PORT config.wsgi
CMD ["/start.sh"]

# [END docker]
