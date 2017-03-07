FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install globus_sdk
RUN pip install ftplib

# Bundle app source
COPY /src/globus_connect.py /src/globus_connect.py
COPY /src/PetrelScanner.py /src/PetrelScanner.py

CMD ["python", "/src/PetrelScanner.py"]