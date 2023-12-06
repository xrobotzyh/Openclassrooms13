#use official python image from docker hub
FROM cimg/python:3.9.13
#set working directory
WORKDIR /openclassrooms13
#copy files
COPY  . /openclassrooms13/
#install necessary packages
RUN pip install -r requirements.txt
#RUN python manage.py migrate
# import environment variables from circleci
ENV PORT=8000
# initial the database
# run the python project


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]