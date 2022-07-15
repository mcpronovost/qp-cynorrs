const { defineConfig } = require("@vue/cli-service");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const BundleTracker = require("webpack-bundle-tracker");
const ENV = process.env.NODE_ENV

module.exports = defineConfig({

    publicPath: (
        ENV == "production" ?
            "/" :
            "/"
    ),
    outputDir: (
        ENV == "production" ? "bundles/pro" : "bundles/dev"
    ),
    transpileDependencies: true,
    productionSourceMap: false,
    filenameHashing: false,

    devServer: {
        host: "localhost",
        port: "8080",
        hot: false,
        liveReload: false,
        historyApiFallback: true,
        devMiddleware: {
            writeToDisk: true
        }
    },

    configureWebpack: {
        plugins: [
            new CleanWebpackPlugin(),
            new BundleTracker({
                filename: (ENV == "production" ? "webpack-pro.json" : "webpack-dev.json"),
                publicPath: (ENV == "production" ? "/" : "http://localhost:8080/")
            })
        ]
    },

    chainWebpack: config => {
        config.optimization.splitChunks({
            cacheGroups: {
                vendors: {
                    name: "chunk-vendors",
                    test: /[\\/]node_modules[\\/]/,
                    priority: -10,
                    chunks: "initial"
                },
                common: {
                    name: "chunk-common",
                    minChunks: 2,
                    priority: -20,
                    chunks: "initial",
                    reuseExistingChunk: true
                }
            }
        })
    }

})
