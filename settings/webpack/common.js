'use strict';

const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCSSExtractPlugin = require('mini-css-extract-plugin');
const BundleTracker = require('webpack4-bundle-tracker');
const helpers = require('./helpers');
const isDev = process.env.NODE_ENV === 'development';

const webpackConfig = {
  entry: {
    polyfill: '@babel/polyfill',
    main: helpers.root('static', 'js', 'packs', 'main'),
  },
  resolve: {
    extensions: ['.js', '.vue'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
      '@': helpers.root('static', 'js'),
      '~': helpers.root('static', 'css'),
    }
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        include: [helpers.root('static', 'js')]
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        include: [helpers.root('static', 'js')]
      },
      {
        test: /\.css$/,
        use: [
          isDev ? 'vue-style-loader' : MiniCSSExtractPlugin.loader,
          {loader: 'css-loader', options: {sourceMap: isDev}},
        ]
      },
      {
        test: /\.scss$/,
        use: [
          isDev ? 'vue-style-loader' : MiniCSSExtractPlugin.loader,
          {loader: 'css-loader', options: {sourceMap: isDev}},
          {loader: 'sass-loader', options: {sourceMap: isDev}}
        ]
      },
      {
        test: /\.sass$/,
        use: [
          isDev ? 'vue-style-loader' : MiniCSSExtractPlugin.loader,
          {loader: 'css-loader', options: {sourceMap: isDev}},
          {loader: 'sass-loader', options: {sourceMap: isDev}}
        ]
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
    new BundleTracker({
      filename: './static/webpack-stats.json',
      logTime: true
    }),
  ]
};

module.exports = webpackConfig;
