ARG BUILD_FROM
FROM $BUILD_FROM

RUN pip3 install --no-cache-dir --disable-pip-version-check paho-mqtt~=1.6.1 requests~=2.28.1

WORKDIR /data

COPY . ./

RUN ls

RUN chmod a+x /data/run.sh

CMD [ "/app/run.sh" ]