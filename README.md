# codenames

> Realtime webapp implementation of the classic social word game, Codenames. Based on a project by [sprek](https://github.com/sprek).

<p>
  <img src="screenshots/player-full.png" alt="Large Player View">
  <img src="screenshots/player-mobile.png" alt="Player - mobile" width="49%">
  <img src="screenshots/spymaster-mobile.png" alt="Spymaster - mobile" width="49%">
</p>

## Rules
Rules for codenames can be found [here](https://en.wikipedia.org/wiki/Codenames_(board_game)#Rules).

## Development
The app uses flask as its back-end and webpack as a front-end dev server.

### Flask Server
```bash
# optional: use a virtualenv
virtualenv venv
source venv/bin/activate

# install python dependencies
pip install -r requirements.txt

# run the flask server
npm run flask
```

### Webpack
```bash
# install dependencies
npm install

# run webpack dev server with hot reload at localhost:8080
npm run dev
```

## Production
### Build
``` bash
# install dependencies
npm install
pip install -r requirements.txt

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# start the flask server
npm run flask
```

## TODO

* Show which team goes first
* Add a turn timer/turn tracker
* Build for production
* Streamline install and build