FROM node:12-stretch
# install MFE certs
# build the container
RUN npm install -g @vue/cli

WORKDIR /app
COPY ./package*.json ./
RUN npm install
RUN npm rebuild node-sass
COPY . .
ENV VUE_APP_FLASK_HOST flask
ENV HOST 0.0.0.0
EXPOSE 8080
CMD ["npm", "run", "serve"]
