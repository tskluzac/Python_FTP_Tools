FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY hello-world.py /src/hello-world.py

EXPOSE  8000
CMD ["python", "/src/hello-world.py", "-p 8000"]
