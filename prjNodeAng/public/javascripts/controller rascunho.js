angular.module('appzao', [])
  .controller('quartoController', ['$scope', '$http', function ($scope, $http) {
          $scope.adicionarQuarto = function () {
          // $.param função do jQuery para serializar em JSON
              var data = $.param({
              nome: $scope.nome,
              tipo: $scope.tipo,
              desc: $scope.desc,
              preco: $scope.preco,
          });
          var config = { headers : {
          'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
        } }
        

          $http.post('/users/adicionarQuarto', data, config)
          .success(function (data, status, headers, config) { $scope.Resposta = data; }
          .error(function (data, status, header, config)
            {
              $scope.Resposta = "Data: " + data + "<hr />status: " + status }));
            };

            
  }])