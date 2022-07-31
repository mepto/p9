const path = require('path')
const MiniCSSExtractPlugin = require('mini-css-extract-plugin')
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
const ProgressBarPlugin = require('progress-bar-webpack-plugin')
const { WebpackManifestPlugin } = require('webpack-manifest-plugin');


const DJANGO_STATIC_URL = '/static/'

module.exports = (env, argv) => {
  const devMode = !argv || argv.mode !== 'production'
  const resolve = path.resolve.bind(path, __dirname)

  return {
    stats: 'errors-warnings',
    entry: {
      'main': resolve('components', 'main.js'),
    },

    resolve: {
      extensions: ['.js'],
    },

    output: {
      path: resolve('dist/assets'),
      filename: `[name]-[chunkhash:8]'}.js`,
      chunkFilename: '[name]-[chunkhash:8].js'
    },

    devtool: !devMode ? 'source-map' : 'eval-cheap-module-source-map',

    devServer: {
      devMiddleware: {
        writeToDisk: true,
      },
      proxy: {
        '/': {
          target: 'http://localhost:8000',
          changeOrigin: true,
        },
      },
    },

    module: {
      rules: [
        {
          test: /\.js$/,
          include: [resolve('node_modules'), resolve('components')],
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env'],
            },
          },
        },
        {
          test: /\.css$/,
          use: [
            MiniCSSExtractPlugin.loader,
            { loader: 'css-loader', options: { sourceMap: devMode } },
            { loader: 'postcss-loader', options: { sourceMap: devMode } }
          ],
          include: [resolve('node_modules'), resolve('components')]
        },
        {
          test: /(\.scss$)|(\.sass$)/,
          use: [
            MiniCSSExtractPlugin.loader,
            { loader: 'css-loader', options: { sourceMap: devMode } },
            { loader: 'postcss-loader', options: { sourceMap: devMode } },
            { loader: 'sass-loader', options: { sourceMap: devMode } }
          ],
          include: [resolve('node_modules'), resolve('components')]
        },
        {
          test: /\.(eot|otf|woff|woff2|ttf)(\?v=[0-9.]+)?$/,
          loader: 'file-loader',
          options: {
            name: 'fonts/[name].[hash].[ext]',
            publicPath: DJANGO_STATIC_URL
          },
          include: [resolve('node_modules'), resolve('components')]
        },
        {
          test: /\.(png|svg|jpg)(\?v=[0-9.]+)?$/,
          loader: 'file-loader',
          options: {
            name: 'images/[name].[hash].[ext]',
            publicPath: DJANGO_STATIC_URL,
            esModule: false
          },
          include: [resolve('node_modules'), resolve('components')]
        }
      ]
    },

    plugins: [
      new ProgressBarPlugin(),
      new CleanWebpackPlugin(),
      new MiniCSSExtractPlugin({
        filename: '[name].[chunkhash:8].css',
        chunkFilename: '[id].[chunkhash:8].css'
      }),
      new WebpackManifestPlugin({publicPath: ''}),
    ],

    optimization: {
      minimizer: [
        `...`,
        new CssMinimizerPlugin(),
      ],
    },
  }
}
