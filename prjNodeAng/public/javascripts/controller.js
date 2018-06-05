var app = angular.module('appzao', ['ngRoute', 'ngResource']);
  
app.controller('quartoController', ['$scope', '$http', function ($scope, $http) {
          $scope.adicionarQuarto = function () {
          // $.param função do jQuery para serializar em JSON
          $scope.quartos.nome = "Kevin Ecklenee";
            $http.get('/users/aaa').then(function(response)
            {
              $scope.quartos = response.data;
            });
          }; 
  }])