FROM node:12-stretch
# build the container
RUN npm install -g @vue/cli

WORKDIR /app
COPY ./package*.json ./
RUN npm install --production --no-progress
RUN npm rebuild node-sass
COPY . .
ENV VUE_APP_FLASK_HOST backend
ENV HOST 0.0.0.0
EXPOSE 8080
CMD ["npm", "run", "serve"]
