(function() {
    'use strict'

    angular.module('scrumboard.demo') //Comment for testing
        .directive('scrumboardCard', CardDirective);

    function CardDirective() {
        return {
            templateUrl: '/static/scrumboard/card.html',
            restrict: 'E',
            controller: ['$scope', '$http', function ($scope, $http) {
                let url = '/scrumboard/cards/' + $scope.card.id + '/';
                $scope.update = function () {
                    $http.put(
                        url,
                        $scope.card
                    );
                };
                $scope.modelOptions = {
                    debounce: 500
                };
            }]
        };
    }
})();