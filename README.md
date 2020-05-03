# Codenames

> Realtime browser-based implementation of the classic social word game, Codenames, designed to be played on multiple devices, or using a shared screen and mobile phones.

[Try it out!](https://codewords.tv)

## Blog Series

To read more about how this project came to fruition and how to build an app using the same technologies, follow the links below!

* __Part 1__ - [Introduction and Planning](https://medium.com/hackervalleystudio/weekend-project-part-1-creating-a-real-time-web-based-application-using-flask-vue-and-socket-b71c73f37df7)
* __Part 2__ - [Enabling Websockets in Flask using Flask-SocketIO](https://medium.com/hackervalleystudio/weekend-project-part-2-turning-flask-into-a-real-time-websocket-server-using-flask-socketio-ab6b45f1d896)
* __Part 3__ - [Scaffolding a Vue App with vue-cli and Managing State with Vuex](https://medium.com/hackervalleystudio/weekend-project-part-3-centralizing-state-management-with-vuex-5f4387ebc144)
* __Part 4__ - [Integrating Websockets into a Real-Time Vue App with Socket.io and Vuex](https://medium.com/hackervalleystudio/weekend-project-part-4-integrating-websockets-into-a-real-time-vue-app-with-socket-io-and-vuex-e358e04f477c)

<p>
  <img src="screenshots/player-full.png" alt="Large Player View">
</p>
<p>
  <img src="screenshots/player-mobile.png" alt="Player - mobile" width="49%">
  <img src="screenshots/spymaster-mobile.png" alt="Spymaster - mobile" width="49%">
</p>

## Rules

Rules for codenames can be found [here](https://en.wikipedia.org/wiki/Codenames_(board_game)#Rules).

## Development

The app uses flask as its back-end and webpack as a front-end dev server.

### Prerequesites

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Run in Development

```bash
./run.sh development
# or run the docker-compose command manually
docker-compose -f docker-compose.yml -f docker-compose.development.yml up --build
# navigate to localhost:8080 in browser
```

## Production

```bash
./run.sh production
```
