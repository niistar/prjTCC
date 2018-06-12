var mongoose = require('mongoose');
var User = require('../models/user.js');
var Maquina = require('../models/maquina.js');
var Tarefa = require ('../models/tarefa.js');

// app/routes.js
module.exports = function(app, passport) {

    app.get('/adicionarMaquina', isLoggedIn, function(req, res, next) {
        res.render('adicionarMaquina.ejs',{

        user:req.user});
    });

    app.get('/escalonar', isLoggedIn, function(req, res, next) {
        res.render('escalonar.ejs',{

        user:req.user});
    });

    app.get('/users/adicionarMaquina', isLoggedIn, function(req, res, next) {
        
        Maquina.find({}, function(err, user){
        if(err){
            return res.send();
        }
        else
        res.json(user);
        });
    });

    app.post('/users/adicionarMaquina', isLoggedIn, function(req, res, next) {
        var maquina1 = new Maquina(req.body);

        maquina1.save(function(err){
            if(err) return console.error(err);
        });
        
        

    });

    app.post('/users/deletarMaquina', isLoggedIn, function(req, res, next) {
        var maquina1 = new Maquina(req.body);

        Maquina.findOneAndRemove({'modeloMaquina': maquina1.modeloMaquina}, function(err, user){
            if(err){
                return res.send();
            }
            });
    });  

    app.get('/adicionarTarefa', isLoggedIn, function(req, res, next) {
        res.render('adicionarTarefa.ejs',{

        user:req.user});
        
    });

    app.get('/users/adicionarTarefa', isLoggedIn, function(req, res, next) {
        Tarefa.find({}, function(err, user){
            if(err){
                return res.send();
            }
            else
            res.json(user);
            });
    });

    app.post('/users/adicionarTarefa/', isLoggedIn, function(req, res, next) {
        var tarefa1 = new Tarefa(req.body);

        tarefa1.save(function(err){
            if(err) return console.error(err);
        });
    });    

    app.post('/users/deletarTarefa', isLoggedIn, function(req, res, next) {

        Tarefa.findOneAndRemove({'nomeTarefa': req.body.nomeTarefa}, function(err, user){
            if(err){
                return res.send();
            }
            });
        
    });  

    app.get('/completarCadastro', isLoggedIn, function(req, res, next){
        res.render('completarCadastro.ejs',
        {
            user : req.user
        });
    });

    app.post('/users/completarCadastro', isLoggedIn, function(req, res, next){
        var user1 = new User(req.body);
        var idzao = req.user._id;

        User.findById(idzao, function(err, user2){
            user2.nome = req.body.nome;
            user2.sobrenome = req.body.sobrenome;
            user2.rua = req.body.rua;
            user2.numero = req.body.numero;
            user2.cidade = req.body.cidade;
            user2.cep = req.body.cep;
            user2.estado = req.body.estado;
            user2.pais = req.body.pais;
            user2.cpf = req.body.cpf;
            user2.rg = req.body.rg;
            user2.telefone = req.body.telefone;
            user2.celular = req.body.celular;
            user2.dataNasc = req.body.dataNasc;
            
            user2.save(function(err, usernovo1){
            });
        });
    });
    
    app.get('/users/completarCadastro', isLoggedIn, function(req, res, next){
        User.findById(req.user._id, function(err, user){
            if(err){
                return res.send();
            }
            else
            res.json(user);
        });
    });


    // =====================================
    // HOME PAGE (with login links) ========
    // =====================================
    app.get('/', function(req, res) {
        res.render('index.ejs'); // load the index.ejs file
    });

    // =====================================
    // LOGIN ===============================
    // =====================================
    // show the login form
    app.get('/login', function(req, res) {

        // render the page and pass in any flash data if it exists
        res.render('login.ejs', { message: req.flash('loginMessage') }); 
    });

    // process the login form
    app.post('/login', passport.authenticate('local-login', {
        successRedirect : '/profile', // redirect to the secure profile section
        failureRedirect : '/login', // redirect back to the signup page if there is an error
        failureFlash : true // allow flash messages
    }));

    // =====================================
    // SIGNUP ==============================
    // =====================================
    // show the signup form
    app.get('/signup', function(req, res) {

        // render the page and pass in any flash data if it exists
        res.render('signup.ejs', { message: req.flash('signupMessage') });
    });

    // process the signup form
    // app.post('/signup', do all our passport stuff here);
    app.post('/signup', passport.authenticate('local-signup', {
        successRedirect : '/profile', // redirect to the secure profile section
        failureRedirect : '/signup', // redirect back to the signup page if there is an error
        failureFlash : true // allow flash messages
    }));

    // =====================================
    // PROFILE SECTION =====================
    // =====================================
    // we will want this protected so you have to be logged in to visit
    // we will use route middleware to verify this (the isLoggedIn function)
    app.get('/profile', isLoggedIn, function(req, res) {

        res.render('profile.ejs', {
            //quarto : quarto1;
            
            user : req.user,
        //    quartos : req.quartos1.quartos[0] // get the user out of session and pass to template
        });
    });

    // =====================================
    // LOGOUT ==============================
    // =====================================
    app.get('/logout', function(req, res) {
        req.logout();
        res.redirect('/');
    });
};

// route middleware to make sure a user is logged in
function isLoggedIn(req, res, next) {

    // if user is authenticated in the session, carry on 
    if (req.isAuthenticated())
        return next();

    // if they aren't redirect them to the home page
    res.redirect('/');
}