FROM alpine:3.8
RUN apk update && apk add bash
RUN apt-get install python3 && apt-get install pip3
RUN pip3 install boto3
RUN npm install -g yo generator-bitbucket-pipe
RUN yo bitbucket-pipe
CMD python --version

ENTRYPOINT [""]