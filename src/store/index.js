import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    connect: false,
    game: {},
    room: '',
    username: '',
  },
  mutations: {
    SOCKET_CONNECT(state) {
      console.log('conntec');
      state.connect = true;
    },
    SOCKET_MESSAGE(state, message) {
      state.game = message;
      state.room = message.game_id;
    },
    SOCKET_JOIN_ROOM(state, message) {
      state.room = message.room;
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
  },
});
