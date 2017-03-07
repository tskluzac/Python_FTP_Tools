FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY hello-world.py /src/src/hello-world.py

CMD ["python", "/src/src/hello-world.py"]
