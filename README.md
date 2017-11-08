# Codenames
Realtime webapp implementation of the classic social word game, Codenames.

Original project by [sprek](https://github.com/sprek).

## Development

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
