export default {
  state: {
    room: null,
    error: null,
    game: {},
    turn: null,
    isSpymaster: false,
  },
  getters: {
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
    }
  },
  mutations: {

  },
  actions: {

  }
}
