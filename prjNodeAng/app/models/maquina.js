var mongoose = require('mongoose');
var User = require('./user.js');
var bcrypt   = require('bcrypt-nodejs');


var maquinaSchema = new mongoose.Schema({
        
        //_id: Number,
        nomeMaquina: String,
        capacidadeHoras: Number,
        tipoMaquina: String,
        modeloMaquina: String,
        observacoesMaquina: String,
        statusMaquina: String,
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
        data_inicio: Date,
        data_fim: Date,


        // dono : [{ type: String, ref: 'User' }] ,
        usuariosMaquina : [{ type: String, ref: 'User' }] ,
        
});

module.exports = mongoose.model('Maquina', maquinaSchema);