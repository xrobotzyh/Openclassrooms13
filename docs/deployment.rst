Deployment
==========

What's you need:
----------------

A GitHub account
A CircleCI account
A DockerHub account
A Render account
A Sentry account

Description of the CircleCi Pipeline Operation
----------------------------------------------

Upon a commit to a branch other than master, the following job is executed:

    Build-and-test: composed of the following run actions:
        Python/install-packages: install necessary packages to run the project
        Run Tests: execution of unit tests using the pytest command

Upon a commit to the master branch, the following jobs are executed:

    build-and-test as described above
    build_and_push_docker_image: composed of the following run actions:

        Build Docker image: creation of a Docker image from the source code via Git
        Push Docker Image: uploading the created image to Docker Hub in two steps: first with the tag corresponding to the CircleCI commit "hash" and then with the "latest" tag

    deploy: composed of the following run action:

        Start container and push to render: launching the application build on Render via Git

Workflow:

The build-and-test job is executed when any modification is made to any branch of the project.

The build_and_push_docker_image deploy jobs are only executed when a modification is made to the master branch.

The build_and_push_docker_image job is executed only when the build-and-test job is successfully executed.

The deploy job is executed only when the build_and_push_docker_image job is successfully executed.

Environment Variables:
----------------------

Creation of environment variables at the project level:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    Variable Name	            Service	            Description
    RENDER_DEPLOY_TEST	        CircleCI	        Render Webhook URL
    XROBOTZYH_DOCKERHUB	        CircleCI	        Docker account username
    XROBOTZYH_PWD_DOCKERHUB	    CircleCI	        Docker account password
    SECRET_KEY                  CircleCI	        Django secret key
    SENTRY_DSN	                CircleCI	        Sentry integration internal token
    SECRET_KEY	                Render	            Django secret key
    SENTRY_DSN                  Render              Sentry integration internal token
    ENV                         Environment ('production' or 'dev')

Application Access:
-------------------

Local:
^^^^^^
For local deployment via source code or Docker image, ensure to provide the following environment variables:

.. code-block:: bash

    SECRET_KEY=your_django_secret_key
    SENTRY_DSN=your_sentry_dsn_key
    ENV=production

Docker:
You can place the above two lines in an env_file at the root of your project to run the Docker image as follows:

.. code-block:: bash

    docker pull <docker_image:tag>
    docker run --env-file=env_file -i -p 8000:8000 <docker_image>

docker_image: access the latest created image using the "latest" tag or choose an earlier image using the corresponding CircleCI commit "hash".