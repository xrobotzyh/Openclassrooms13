#use official python image from docker hub
FROM python:3.9.13
#set working directory
WORKDIR /openclassrooms13
#copy requirements
COPY requirements.txt .
#install necessary packages
RUN pip install -r requirements.txt
COPY . .
# import environment variables from circleci
ARG SECRET_KEY
ARG SECRET_DSN
ENV SECRET_KEY=${SECRET_KEY}
ENV SECRET_DSN=${SECRET_DSN}
# initial the database
RUN python manage.py migrate
# expose port 80000
EXPOSE 8000
# run the python project
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]