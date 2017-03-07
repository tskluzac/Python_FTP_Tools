FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY /src/hello-world.py /src/hello-world.py

CMD ["python", "/src/hello-world.py"]
