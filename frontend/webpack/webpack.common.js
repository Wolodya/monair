const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')
var BundleTracker  = require('webpack-bundle-tracker');

module.exports = {
    entry: {
        app: './frontend/src/main.js'
    },
    output: {
        path: path.resolve('./frontend/dist/bundles/'),
        filename: '[name]-[hash:8].js'
    },
    module:{
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.css$/,
                use: [
                  'vue-style-loader',
                  'css-loader'
                ]
            }            
        ]
    },
    plugins: [
        new VueLoaderPlugin(),
        new BundleTracker({filename: './webpack-stats.json'})

    ]
}