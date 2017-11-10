# codenames

> Realtime webapp implementation of the classic social word game, Codenames. Based on a project by [sprek](https://github.com/sprek).

## Development

### Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

### Server
1. `pip install -r requirements.txt`
2. `python __init__.py`

## TODO

* Convert original code to return JSON instead of HTML
* Build websocket architecture
    * Create a lobby [deck, size] - this will generate a random seed for others to join with
    * Join the lobby using seed from above
    * Leave the lobby
    * Get cards - probably can be sent with the "on join" event as an initializer
    * This will have to vary based on leader/player
    * Select and validate a card - this will update all players
