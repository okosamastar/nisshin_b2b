let mix = require('laravel-mix');
const path = require('path');
const del = require('del');

require('laravel-mix-svg-vue');

let resourcesPath = 'resources'
let staticPath = 'static'

mix.setPublicPath(staticPath)
mix.setResourceRoot('../')

// if you don't need browser-sync feature you can remove this lines
mix.browserSync(
    {
        // https://www.browsersync.io/docs/options/#option-proxy
        files: [
            "templates/**/*.*",
            "./*.py",
            "resources/**/*.*"
        ],
        proxy: {
            target: '0.0.0.0:8000',
            proxyReq: [
                function (proxyReq, req) {
                    // Assign proxy "host" header same as current request at Browsersync server
                    proxyReq.setHeader('Host', req.headers.host)
                }
            ]
        },
    }
)

del(staticPath);

mix.copyDirectory(`${resourcesPath}/images/`, `${staticPath}/images/`);

mix.js(`${resourcesPath}/js/index.js`, `${staticPath}/js/`)
    .vue({
        extractStyles: true,
        globalStyles: false
    })
    .postCss(`${resourcesPath}/css/style.css`, `${staticPath}/css/`, [
        require('postcss-import'),
        require('postcss-color-function'),
        require('postcss-simple-vars'),
        require('postcss-calc'),
        require('postcss-nested'),
        require('tailwindcss'),
        // require('postcss-inline-svg'),
        require('postcss-svgo'),
        require('postcss-sorting'),
    ])
    .svgVue({
        svgPath: 'resources/svg',
        extract: false,
        svgoSettings: [
            {removeTitle: true},
            {removeViewBox: false},
            {removeDimensions: true},
        ]
    })
    .options({
        fileLoaderDirs: {
            images: 'images',
            fonts: 'fonts'
        }
    })
    .styles([
        `${staticPath}/js/index.css`,
        `${staticPath}/css/style.css`
    ], `${staticPath}/css/app.css`)
    .styles([
        `${resourcesPath}/css/common_header.css`,
        `${resourcesPath}/css/global.css`,
        `${resourcesPath}/css/index_style.css`
    ], `${staticPath}/css/legacy.css`)

// .options({
//   processCssUrls: false,
// })


mix.webpackConfig({
    // externals: {
    //     "jquery": "jQuery"
    // }
});

if (mix.inProduction()) {
    // mix.versionHash();
    mix.version()
} else {
    mix.sourceMaps();
}
