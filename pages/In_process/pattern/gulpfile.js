const gulp = require('gulp');
const postcss = require('gulp-postcss');
const cleanCSS = require('gulp-clean-css');
const autoprefixer = require('autoprefixer');
const browserSync = require('browser-sync').create();
const gulpIf = require('gulp-if');
const sourcemaps = require('gulp-sourcemaps');
const rename = require('gulp-rename');
const del = require('del');
const gutil = require('gulp-util');
const pug = require('gulp-pug');
const customizeBootstrap = require('gulp-customize-bootstrap');
const sass = require('gulp-sass');

const isDevelopment = process.env.NODE_ENV !== 'production';



gulp.task('views', function buildHTML() {
    return gulp.src('./src/index.pug')
        .pipe(pug())
        .on('error', function(error) {
            gutil.log(gutil.colors.red('Error: ' + error.message));
            this.emit('end');
        })
        .pipe(gulp.dest('./dist'));
});

gulp.task('sass', function () {
  return gulp.src('./src/app.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./dist/css'));
});


gulp.task('prefix', () =>
    gulp.src('src/app.css')
        .pipe(guloIf(!isDevelopment, postcss([
            autoprefixer({
                browsers: ['> 5%', 'ff > 14']
            })
        ])))
        .pipe(gulpIf(isDevelopment, sourcemaps.write()))
        .pipe(gulpIf(!isDevelopment, cleanCSS()))
        .pipe(rename('style.css'))
        .pipe(gulp.dest('./dist/css'))
);

gulp.task('compile', ['sass', 'prefix']);

gulp.task('compileBootstrap', function() {
  return gulp.src('node_modules/bootstrap/scss/bootstrap.scss')
    .pipe(customizeBootstrap('styles/scss/*.scss'))
    .pipe(sass())
    .pipe(gulp.dest('styles/'));
});

gulp.task('copy:fonts', function () {
    return gulp.src([
        './node_modules/font-awesome/fonts/**/*.*'
    ])
        .pipe(gulp.dest('./dist/fonts'));
});

gulp.task('copy:images', function () {
    return gulp.src('./src/**/*.{png,jpg,jpeg,gif,svg}')
        .pipe(rename(function (path) {
            path.dirname = '';
        }))
        .pipe(gulp.dest('./dist/images'));
});

gulp.task('watch', function () {
  gulp.watch('./src/**/*.scss', gulp.series('sass'));
  gulp.watch('./src/**/*.pug', gulp.series('views'));
});


gulp.task('serve', function () {
    browserSync.init({
        server: './dist',
        port: 8080
    });

    browserSync.watch('./dist/**/*.*').on('change', browserSync.reload);
});

gulp.task('clean', function () {
    return del('./dist')
});

gulp.task('build', gulp.series(
    'clean',
    gulp.parallel(
        'views',
        'compile',
        'copy:fonts',
        'copy:images'
    )));

gulp.task('default', gulp.series(
    'build',
    gulp.parallel(
        'watch',
        'serve'
    )));
