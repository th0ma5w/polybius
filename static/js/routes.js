angular.module('reader', ['opmlServices','feedServices','urlEncoding',])
  .config(function($routeProvider){
        $routeProvider
                .when('/',{controller:mainCtrl, templateUrl:'main.html'})
                .when('/opml/:opmlurl',{controller:opmlCtrl, templateUrl:'opml.html'})
                .when('/feed/:feedurl',{controller:feedCtrl, templateUrl:'feed.html'})
                .when('/refresh/:feedurl',{controller:refreshCtrl, templateUrl:'feed.html'})
                .when('/entries/:feedurl',{controller:entriesCtrl, templateUrl:'feed.html'})
                .otherwise({redirectTo:'/'})
                ;
        })

