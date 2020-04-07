module.exports = {
  lintOnSave: false,
  devServer: {
    proxy: {
      '/socket.io': {
        target: `http://${process.env.VUE_APP_FLASK_HOST}:5000`,
        ws: true,
        changeOrigin: true,
      },
    },
  },
};
