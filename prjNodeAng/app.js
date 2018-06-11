
// set up ======================================================================
// get all the tools we need
var express  = require('express');
var app      = express();
var port     = process.env.PORT || 1337;
var mongoose = require('mongoose');
var passport = require('passport');
var flash    = require('connect-flash');

var morgan       = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser   = require('body-parser');
var session      = require('express-session');

var configDB = require('./config/db.js');

//var mongoose = require('mongoose');
var User            = require('./app/models/user');
var Maquina          = require('./app/models/maquina');
var users           = require('./app/routes/users.js');

// configuration ===============================================================
mongoose.connect(configDB.url); // connect to our database

require('./config/passport')(passport); // pass passport for configuration
app.use(express.static(__dirname + '/public'));
app.use(express.static(__dirname + '/views'));
app.use('/node_modules', express.static(__dirname + '/node_modules'));
app.use('/bower_components', express.static(__dirname + '/bower_components'));

// set up our express application
app.use(morgan('dev')); // log every request to the console
app.use(cookieParser()); // read cookies (needed for auth)
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json()); // get information from html forms

app.set('view engine', 'ejs'); // set up ejs for templating

// required for passport
app.use(session({ secret: 'ilovescotchscotchyscotchscotch', resave : true, saveUninitialized : true })); // session secret
app.use(passport.initialize());
app.use(passport.session()); // persistent login sessions
app.use(flash()); // use connect-flash for flash messages stored in session

// routes ======================================================================
require('./app/routes/routes.js')(app, passport); // load our routes and pass in our app and fully configured passport
//app.use('/users', users);
// launch ======================================================================
app.listen(port);
console.log('The magic happens on port ' + port);
/*
User.findOne({nome:'joao'})
        .populate({path : 'quartos',
        populate: {path: 'reservante', model: User}})
        .exec(function(err, user){
            if(err){
                console.log(err);
            }
            else{
            console.log(user);
            
            }
            
        });*/
/*
        User.findOne({nome:'joao'})
        .populate('quartos')
        .exec(function(err, user){
            if(err){
                console.log(err);
            }
            else{
            console.log(user);
            }
            
        });
*/

module.exports = app;