var mongoose = require('mongoose');
var User = require('./user.js');
var bcrypt   = require('bcrypt-nodejs');


var escalaSchema = new mongoose.Schema({
        
        //_id: Number,
        nomeTarefa: String,
        horasTarefa: Number,
        order : Number,
        forcedOrder: Number,
        nextTask: Number
        // titulo : String,
        // rua : String,
        // numero : Number,
        // cidade : String,
        // estado : String,
        // desc : String,
        // preco : Number,
        // total_aval : Number,
        // numero_aval : Number,
        // media_aval : Number,
        // reservado : Boolean,



        // dono : [{ type: String, ref: 'User' }] ,
       // usuariosMaquina : [{ type: String, ref: 'User' }] ,
        
});

module.exports = mongoose.model('Escala', escalaSchema);