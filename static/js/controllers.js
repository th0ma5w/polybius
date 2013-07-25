var mainCtrl = function($scope) {}

var opmlCtrl = function($scope, $routeParams, Opml) {
                $scope.opml = Opml.get({opmlurl: $routeParams.opmlurl},function(opml){
                });
                $scope.opmlurl=$routeParams.opmlurl;
        };

var feedCtrl = function($scope, $routeParams, Feed) {
                $scope.feed = Feed.get({feedurl: $routeParams.feedurl},function(feed){
                });
                $scope.feedurl=$routeParams.feedurl;
        };

var refreshCtrl = function($scope, $routeParams, FeedRefresh) {
                $scope.feed = FeedRefresh.get({feedurl: $routeParams.feedurl},function(feed){
                });
                $scope.feedurl=$routeParams.feedurl;
        };

var entriesCtrl = function($scope, $routeParams, FeedEntries) {
                $scope.feed = FeedEntries.get({feedurl: $routeParams.feedurl},function(feed){
                });
                $scope.feedurl=$routeParams.feedurl;
        };

