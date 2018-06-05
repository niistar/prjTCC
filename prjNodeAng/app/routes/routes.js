var mongoose = require('mongoose');
var User = require('../models/user.js');
var Quarto = require('../models/quarto.js');

// app/routes.js
module.exports = function(app, passport) {

    app.get('/adicionarQuarto', isLoggedIn, function(req, res, next) {
        res.render('adicionarQuarto.ejs',{

        user:req.user});
    });

    app.get('/users/adicionarQuarto', isLoggedIn, function(req, res, next) {
        Quarto.find({dono : req.user._id}, function(err, user){
        if(err){
            return res.send();
        }
        else
        res.json(user);
        });
    });

    app.post('/users/adicionarQuarto', isLoggedIn, function(req, res, next) {
        var quarto1 = new Quarto(req.body);

        User.findByIdAndUpdate(req.user._id, 
        {$push : {"quartosCadastrados" : quarto1._id}},
        {safe: true, upsert: true},function(err, quarto1){
            console.log(err);
        });

        quarto1.dono = req.user._id;
        quarto1.reservado = false;
        quarto1.save(function(err){
            if(err) return console.error(err);
        });
        
        

    });

    app.get('/adicionarReserva', isLoggedIn, function(req, res, next) {
        res.render('adicionarReserva.ejs',{

        user:req.user});
        
    });

    app.get('/users/adicionarReserva', isLoggedIn, function(req, res, next) {
  
        Quarto.find({dono:{'$ne':req.user._id}, reservado:false}, function(err, user){
        if(err){
            return res.send();
        }
        else
        res.json(user);
        });
    });

    app.post('/users/adicionarReserva/', isLoggedIn, function(req, res, next) {
        var idzao = req.body._id;
        console.log(req.body);
        Quarto.findById(idzao, function(err, quarto1){
            quarto1.reservado = true;
            quarto1.reservante = req.user._id;
            quarto1.data_inicio = req.body.data_inicio;
            quarto1.data_fim = req.body.data_fim;
            
            quarto1.save(function(err, novoQuarto){
                if(err) return handleError(err);
                res.send(novoQuarto);
                console.log(novoQuarto);
            });

        });
        User.findByIdAndUpdate(req.user._id, 
        {$push : {"quartos" : idzao}},
        {safe: true, upsert: true},function(err, quarto1){
            console.log(err);
        });
        User.findById(req.user._id, function(err, user2){
            user2.saldo = user2.saldo - req.body.preco;
            user2.save(function(err, novoUser){
            });
        });
        Quarto.findById(idzao, function(err, quarto9){
        User.findById(quarto9.dono, function(err, user3){
            user3.saldo = user3.saldo + req.body.preco;
            user3.save(function(err, novoUser2){
            });
        });
        });
    });    

    app.get('/encerrarReserva', isLoggedIn, function(req, res, next){
        res.render('encerrarReserva.ejs',
        {
            user : req.user
        });
    });
    
    app.get('/users/encerrarReserva', isLoggedIn, function(req, res, next)
    {
        Quarto.find({reservante : req.user._id}, function(err, user){
        if(err){
            return res.send();
        }
        else
        res.json(user);
        });
    }
    );

    app.post('/users/encerrarReserva', isLoggedIn, function(req, res, next)
    {
        idzao = req.body._id;
        var nota = req.body.nota;
        console.log(nota);
        Quarto.findById(idzao, function(err, quarto9){
            quarto9.reservado = false;
            quarto9.data_fim = undefined;
            quarto9.data_inicio = undefined;
            
            quarto9.save(function(err, novoQuarto1){
            });
        });
        Quarto.findByIdAndUpdate(idzao, 
        {$pull : {"reservante" : req.user._id}},
        {safe: true, upsert: true},function(err, quarto1){
            console.log(err);
        });

        User.findByIdAndUpdate(req.user._id, 
        {$pull : {"quartos" : idzao}},
        {safe: true, upsert: true},function(err, quarto1){
            console.log(err);
        });
    }
    );

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
            user2.saldo = req.body.saldo;
            
            user2.save(function(err, usernovo1){
            });
        });
    });
    
    app.get('/users/profile', isLoggedIn, function(req, res, next){
        Quarto.find({reservante : req.user._id}, function(err, user){
        if(err){
            return res.send();
        }
        else
        res.json(user);
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