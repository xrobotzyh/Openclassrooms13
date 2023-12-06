#use official python image from docker hub
FROM cimg/python:3.9.13
#set working directory
WORKDIR /openclassrooms13
#copy files
COPY  . /openclassrooms13/
#install necessary packages
RUN pip install -r requirements.txt
# import environment variables from circleci
ENV PORT=8000
# initial the database
# run the python project
#RUN chmod +x docker/run.sh
CMD ["sh", "-c", "chmod +x docker/run.sh && docker/run.sh"]