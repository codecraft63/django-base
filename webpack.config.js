const path = require("path");
const autoprefixer = require('autoprefixer');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

const resolve = path.resolve.bind(path, __dirname);

module.exports = (env, argv) => {
  const devMode = argv.mode !== 'production';

  let extractCssPlugin;
  let fileLoaderPath;
  let output;

  if (!devMode) {
    const baseStaticPath = process.env.STATIC_URL || '/static/';
    const publicPath = url.resolve(baseStaticPath, 'assets/');
    output = {
      path: resolve('{{ project_name }}/static/assets/'),
      filename: "[name].[chunkhash].js",
      chuckFilename: '[name].[chunkhash].js',
      publicPath: publicPath
    };
    fileLoaderPath = 'file-loader?name=[name].[hash].[ext]';
    extractCssPlugin = new MiniCssExtractPlugin({
      filename: '[name].[chunkhash].css',
      chuckFilename: '[id].[chunkhash].css',
    })
  } else {
    output = {
      path: resolve('{{ project_name }}/static/assets/'),
      filename: '[name].js',
      chuckFilename: '[name].js',
      publicPath: '/static/assets/'
    };
    fileLoaderPath = 'file-loader?name=[name].[ext]';
    extractCssPlugin = new MiniCssExtractPlugin({
      filename: '[name].css',
      chuckFilename: '[name].css'
    });
  }
  ;

  return {
    context: __dirname,

    entry: {
      main: './{{ project_name }}/static/js/main/index'
    },

    output: output,

    module: {
      rules: [
        {
          test: /\.js$/,
          loader: 'babel-loader',
          exclude: file => (
            /node_modules/.test(file) &&
            !/\.vue\.js/.test(file)
          )
        },
        {test: /\.vue$/, loader: 'babel-loader'}, // to transform VUE into JS
        {
          test: /\.scss$/,
          use: [
            MiniCssExtractPlugin.loader,
            'vue-style-loader',
            {
              loader: 'css-loader',
              options: {sourceMap: true}
            },
            {
              loader: "postcss-loader",
              options: {
                sourceMap: true,
                plugins: [autoprefixer]
              }
            },
            {
              loader: 'sass-loader',
              options: {sourceMap: true}
            }
          ]
        },
        {
          test: /\.(eot|oft|png|svg|jpg|ttf|woff|woff2)(\?v=[0-9.]+)?%/,
          loader: fileLoaderPath,
          include: [
            resolve('node_modules'),
            resolve('{{ project_name }}/static/fonts'),
            resolve('{{ project_name }}/static/images')
          ]
        }
      ],
    },

    optimization: {
      removeAvailableModules: false,
      removeEmptyChunks: false,
      splitChunks: false
    },

    plugins: [
      new VueLoaderPlugin(),
      new BundleTracker({filename: './static/webpack-stats.json'}),
      new webpack.ProvidePlugin({
        $: 'jquery',
        JQuery: 'jquery',
        Vue: 'vue/dist/vue.esm'
      })
    ],

    resolve: {
      alias: {
        Vue: resolve('node_modules/vue/dist/vue.esm.js')
      },
      extensions: ['.vue', '.js', '.jsx']
    },

    devtool: "sourceMap"
  };
};