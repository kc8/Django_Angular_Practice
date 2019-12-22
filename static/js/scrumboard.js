(function() {
    'use strict';
    angular.module('scrumboard.demo', ['ngRoute']) // important as we tell the module that route is a dependency in depdency list
        .controller('ScrumboardController', ['$scope', '$http', 'Login', ScrumboardController]);

    function ScrumboardController($scope, $http, Login) {
        $scope.add = function(list, title) {
            let card = {
                list: list.id,
                title: title
            }
            $http.post('scrumboard/cards/', card)
                .then(function(response) {
                    list.cards.push(response.data);
                },
                    function() {
                    alert('Cloud not create card');
                    });
            list.cards.push(card);
        };

        Login.redirectIfNotLoggedIn();
        $scope.data = [];
        $scope.logout = Login.logout;
        $scope.sortBy='title';
        $scope.reverse=false;
        $scope.showFilters=false;

        $http.get('/scrumboard/lists/').then(function(response) {
            $scope.data = response.data;
        });
    }
}());