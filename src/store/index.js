import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    connected: false,
    game: {},
    room: '',
    username: '',
    error: '',
    turn: '',
    spymasterReveal: false,
  },
  mutations: {
    SOCKET_CONNECT(state) {
      state.connected = true;
    },
    SOCKET_DISCONNECT(state) {
      state.connected = false;
    },
    SOCKET_MESSAGE(state, message) {
      state.game = message;
      state.turn = message.starting_color;
      state.room = message.game_id;
      state.error = null;
    },
    SOCKET_JOIN_ROOM(state, message) {
      state.error = null;
      state.room = message.room;
    },
    SOCKET_ERROR(state, message) {
      state.error = message.error;
    },
    set_turn(state, team) {
      state.turn = team;
    },
    set_game(state, game) {
      state.game = game;
    },
    set_room(state, room) {
      state.room = room;
    },
    set_username(state, username) {
      state.username = username;
    },
    reset_error(state) {
      state.room = '';
      state.error = '';
    },
    reveal_spymaster(state) {
      state.spymasterReveal = true;
    },
  },
});
