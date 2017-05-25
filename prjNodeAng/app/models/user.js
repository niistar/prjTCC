var mongoose = require('mongoose');
var Quarto = require('./quarto.js');
var bcrypt   = require('bcrypt-nodejs');


var userSchema = new mongoose.Schema({
        
	//_id: Number,
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
        saldo : Number,
        password : String,
        quartosCadastrados : [{type: String, ref: 'Quarto'}],
        quartos : [{type: String, ref: 'Quarto'}]
});

userSchema.methods.generateHash = function(password) {
    return bcrypt.hashSync(password, bcrypt.genSaltSync(8), null);
};

// checking if password is valid
userSchema.methods.validPassword = function(password) {
    return bcrypt.compareSync(password, this.password);
};

module.exports = mongoose.model('User', userSchema);