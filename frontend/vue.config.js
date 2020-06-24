process.env.VUE_APP_VERSION = require('./package.json').version
console.log(process.env.VUE_APP_VERSION)
module.exports = {
  lintOnSave: false,
  devServer: {
    stats: {
      colors: true,
      hash: false,
      version: false,
      timings: false,
      assets: false,
      chunks: false,
      modules: false,
      reasons: false,
      children: false,
      source: false,
      errors: false,
      errorDetails: false,
      warnings: false,
      publicPath: false
    },
    proxy: {
      '/socket.io': {
        target: `http://${process.env.VUE_APP_FLASK_HOST}:5000`,
        ws: true,
        changeOrigin: true
      },
    },
  },
  chainWebpack: config => {
    config.module
      .rule("i18n")
      .resourceQuery(/blockType=i18n/)
      .type('javascript/auto')
      .use("i18n")
      .loader("@intlify/vue-i18n-loader")
      .end();
  }
};
