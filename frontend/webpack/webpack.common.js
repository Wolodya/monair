const path = require("path");
const VueLoaderPlugin = require("vue-loader/lib/plugin")
var BundleTracker  = require("webpack-bundle-tracker");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: {
        app: "./frontend/src/main.js"
    },
    output: {
        path: path.resolve("./frontend/dist/bundles/"),
        filename: "[name]-[hash:8].js"
    },
    module:{
        rules: [
            {
                test: /\.vue$/,
                loader: "vue-loader",
            },
            {
                test: /\.js$/,
                loader: "babel-loader",
                exclude: /node_modules/,
            },
            {
                test: /\.(sa|sc|c)ss$/,
                use: [ MiniCssExtractPlugin.loader, "css-loader", "sass-loader",]
            },

        ]
    },
    plugins: [
        new VueLoaderPlugin(),
        new BundleTracker({filename: "./webpack-stats.json"}),
        new MiniCssExtractPlugin({
            filename: "[name].css",
        }),
    ],
    optimization: {
        splitChunks: {
          cacheGroups: {
            styles: {
              name: "styles",
              test: /\.(sa|sc|c)ss$/,
              chunks: "all",
              enforce: true
            }
          }
        }
      },
}