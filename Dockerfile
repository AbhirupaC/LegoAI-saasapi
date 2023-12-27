FROM python:3.10

WORKDIR /opt/
EXPOSE 5000
#RUN groupadd -r appgrp && useradd -r -g appgrp appuser && chown appuser:appgrp -R /opt/
#USER appuser
COPY ./app app
COPY ./core core
COPY ./data data
COPY ./testapp testapp
COPY ./certs certs
COPY run.py tests.py requirements.txt  init.sh ./

CMD ["/bin/bash", "init.sh"]
