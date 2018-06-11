var mongoose = require('mongoose');
var Maquina = require('./maquina.js');
var bcrypt   = require('bcrypt-nodejs');


var userSchema = new mongoose.Schema({
        
	//_id: Number,
        nome : String,
        sobrenome : String,
        rua : String,
        numero : Number,
        cidade : String,
        estado : String,
        pais : String,
        email : String,
        telefone : Number,
        celular : Number,
        cpf : Number,
        cep : Number,
        rg : Number,
        dataNasc : Date,
        saldo : Number,
        password : String,
        quartosCadastrados : [{type: String, ref: 'Quarto'}],
        quartos : [{type: String, ref: 'Quarto'}],
        total_aval : Number,
        numero_aval : Number,
        media_aval : Number
});

userSchema.methods.generateHash = function(password) {
    return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
};

// checking if password is valid
userSchema.methods.validPassword = function(password) {
    return bcrypt.compareSync(password, this.password);
};

module.exports = mongoose.model('User', userSchema);