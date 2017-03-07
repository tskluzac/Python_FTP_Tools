FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install globus_sdk

# Bundle app source
COPY /src/globus_connect.py /src/globus_connect.py

CMD ["python", "/src/globus_connect.py"]