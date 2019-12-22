(function() {
    'usestrict';

    angular
        .module('scrumboard.demo')
        .controller('LoginController',
            ['$scope', '$http', '$location', 'Login', LoginController]);

    function LoginController($scope, $http, $location, Login) {
        $scope.login = function() {
            $http.post('/auth_api/login/', $scope.user)
                .then(function () {
                    $location.url ('/');
                },
                function() {
                    $scope.login_error="Invalid username or password combination";
                });
        }
        if (Login.isLoggedIn()) {
            $location.url('/');
        }
    }
})();