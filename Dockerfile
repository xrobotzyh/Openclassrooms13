#use official python image from docker hub
FROM cimg/python:3.9.13
#set working directory
WORKDIR /openclassrooms13
#copy files
COPY  . /openclassrooms13/
#install necessary packages
RUN pip install -r requirements.txt
# import environment variables from circleci
COPY run.sh /openclassrooms13/docker/run.sh
RUN chmod +x /openclassrooms13/docker/run.sh
ENV PORT=8000
# initial the database
# run the python project
#RUN chmod +x docker/run.sh
CMD ["./run.sh"]