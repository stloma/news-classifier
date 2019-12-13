### Build image

`docker build . -t cs6220/news_classifier`

### Run your container

`docker run -d -p 8080:8080 --name news_classifier cs6220/news_classifier:latest`

### Access your service

Using a browser, navigate to `localhost:8080/ui` to access the swagger interface of your service.

### Stop your container

Once you're done, you can stop your container by running `docker stop CONTAINER_ID`. To retrieve the container_id, reference the output of `docker ps`.
