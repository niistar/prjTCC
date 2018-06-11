var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var User = require('../models/user.js');
//var Quarto = require('../models/quarto.js');

/* GET users listing. */

/*router.get('/aaa', function(req, res, next) {
  
  User.find({}, function(err, user){
    if(err){
     // return res.send();
    }
    res.render('adicionarQuarto.ejs');
    console.log("sadasd");
  });

 // res.send('respond with a resource');

  
});*/

router.get('/aaab', function(req, res, next) {
  
  Quarto.find({}, function(err, user){
    if(err){
     return res.send();
    }
    else
    res.json(user);
    //res.render('adicionarQuarto.ejs',{data:user});
//    console.log(user);
  });

router.post('/aaa', function(req, res, next) {
  var quarto1 = new Quarto(req.body);
  console.log("ahrfuwuhfuw" + quarto1)
  console.log(req.user + "ru289yr2w98ry8wfr");

});

  
});

function isLoggedIn(req, res, next) {

    // if user is authenticated in the session, carry on 
    if (req.isAuthenticated())
        return next();

    // if they aren't redirect them to the home page
    res.redirect('/');
}

module.exports = router;
