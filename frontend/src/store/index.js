import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'
import router from '../router';

Vue.use(Vuex);
const inFifteenMinutes = new Date(new Date().getTime() + 15 * 60 * 1000);
export default new Vuex.Store({
  plugins: [createPersistedState({
    storage: {
      getItem: key => Cookies.get(key),
      // Please see https://github.com/js-cookie/js-cookie#json, on how to handle JSON.
      setItem: (key, value) => Cookies.set(key, value, {
        expires: inFifteenMinutes
      }),
      removeItem: key => Cookies.remove(key)
    }
  })],
  state: {
    connected: false,
    disconnected: false,
    disconnect_delay: null,

    starting_sid: null,
    current_sid: null,
    test: 0,
    drawer: false,
    rules: {
      required: value => !!value || "Required.",
      id_length: value => (value && value.length === 5) || "Room ID must be 5 characters."
    },
    // game-specific stuff TODO: move into a module
    dictionaries: {},
    game: {},
    room: '',
    username: null,
    error: null,
    turn: '',
    spymasterReveal: false,
    popupHides: 0
  },
  getters: {
    username(state) {
      if (state.username)
        return state.username
      else if (state.starting_sid)
        return `Agent ${state.starting_sid.substr(6, 6)}`
      else
        return "Unknown Agent"
    },
    isSpymaster(state) {
      if (state.game.players) {
        return state.game.players.spymasters.indexOf(state.current_sid) >= 0
      }
      return false;
    },
    words(state) {
      if (state.game.solution) {
        return Object.keys(state.game.solution);
      }
      return [];
    },
    tileCounts(state) {
      if (state.game.solution) {
        const flippedCounts = {};
        const totalCounts = {
          R: 0,
          B: 0,
          G: 0,
          X: 0,
        };
        // compile the counts for each team + assassin
        Object.keys(state.game.solution).forEach((word) => {
          if (state.game.solution[word] !== 'O') {
            flippedCounts[state.game.solution[word]] = flippedCounts[state.game.solution[word]] || 0;
            if (state.game.board[word]) {
              flippedCounts[state.game.board[word]] += 1;
            }
            totalCounts[state.game.solution[word]] = totalCounts[state.game.solution[word]] || 0;
            totalCounts[state.game.solution[word]] += 1;
          }
        });
        return {
          total: totalCounts,
          flipped: flippedCounts,
        };
      }
      return false;
    },
    gameWon(state, getters) {
      if (getters.tileCounts) {
        return getters.tileCounts.flipped.X > 0 ||
          getters.tileCounts.flipped.R === getters.tileCounts.total.R ||
          getters.tileCounts.flipped.B === getters.tileCounts.total.B ||
          getters.tileCounts.flipped.G === getters.tileCounts.total.G;
      }
      return false;
    },
  },
  mutations: {
    set_connected(state, payload) {
      state.connected = payload;
    },
    set_starting_sid(state, payload) {
      state.starting_sid = payload;
    },
    set_current_sid(state, payload) {
      state.current_sid = payload;
    },
    set_drawer(state, payload) {
      state.drawer = payload;
    },
    set_dictionaries(state, payload) {
      state.dictionaries = payload;
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
    set_error(state, payload) {
      state.error = payload
    },
    reset_error(state) {
      state.room = null;
      state.error = null;
    },
    reset_room(state) {
      state.game = {};
      state.spymasterReveal = false;
    },
    incrementPopupHides(state) {
      state.popupHides++
    },
  },
  actions: {
    WS_connect(context) {
      context.commit('set_connected', true);
      // set sids
      if (context.state.starting_sid)
        context.commit("set_starting_sid", Vue.prototype.$socket.id);
      context.commit("set_current_sid", Vue.prototype.$socket.id);

      // clear disconnect timeout and reconnect
      if (context.state.disconnect_delay) clearTimeout(context.state.disconnect_delay);
      context.state.disconnected = false;
    },
    WS_disconnect(context) {
      context.commit('set_connected', false);
      // reset delay timer
      if (context.state.disconnect_delay) clearTimeout(context.state.disconnect_delay);
      context.state.disconnect_delay = setTimeout(() => {
        return (context.state.disconnected = true);
      }, 3000);

    },
    WS_message(context, message) {
      context.commit('reset_error')
      context.commit('set_game', message)
      context.commit('set_turn', message.starting_color)
      context.commit('set_room', message.game_id)
    },
    WS_join_room(context, message) {
      context.commit('reset_error')
      context.commit('set_room', message.room)
    },
    WS_list_dictionaries(context, message) {
      context.commit('set_dictionaries', message.dictionaries)
    },
    WS_error(context, message) {
      context.commit('set_error', message.error)
    },
  }
});
