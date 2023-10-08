# HOW TO DEPLOY THE APP LOCALLY
In order to run the bew application locally, go ahead and perform the following steps:

1. Create a .env file in the project's main folder with the following two lines (substitute the actual values of the environment variables in place of the <>)
    * MONGO_URI = <mongo-db-uri>
    * OPENAI_API_KEY = <openai-api-key>
4. Execute the back-end server by running:
    * uvicorn app:app --reload

You can now check out and test the back-end server API documentation by visiting http://127.0.0.1:8000/docs.

# HOW TO DEPLOY THE APP REMOTELY ON HEROKU
* LOCAL DOCKER OPERATIONS
    * docker build -t open-science-cafe/app:1.0 .
    * docker run -d --name open-science-cafe -env PORT=80 -p 80:80 open-science-cafe/app:1.0

* HEROKU DOCKER OPERATIONS
    * heroku login
    * heroku container:login
    * heroku container:push web -a <app-name>
    * heroku container:release web -a <app-name>
