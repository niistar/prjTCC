var mongoose = require('mongoose');
//var Quarto = require('./models/quarto.js');
var bcrypt   = require('bcrypt-nodejs');


var userSchema = new mongoose.Schema({
        
//	_id: Number,
        nome : String,
        endereco : String,
        cidade : String,
        estado : String,
        pais : String,
        email : String,
        telefone : String,
        celular : String,
        CPF : String,
        CEP : String,
        RG : String,
        dataNasc : Date,
        //saldo : Number,
        password : String,
        horaInicialTurno: Date,
        horaFinalTurno: Date,
        //turnos : [{type: Number, ref: 'Quarto'}],
        maquinas : [{type: Number, ref: 'Maquina'}]

        
});

userSchema.methods.generateHash = function(password) {
    return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
};

// checking if password is valid
userSchema.methods.validPassword = function(password) {
    return bcrypt.compareSync(password, this.local.password);
};

module.exports = mongoose.model('User', userSchema);