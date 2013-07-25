angular.module('opmlServices',['ngResource'])
  .factory('Opml', function($resource){
        return $resource('/memopml/:opmlurl', {}, {
                query: {method: 'GET', params: {opmlurl: ''}, isArray: false}
        });
});

angular.module('feedServices',['ngResource'])
  .factory('Feed', function($resource){
        return $resource('/memfeed/:feedurl', {}, {
                query: {method: 'GET', params: {feedurl: ''}, isArray: false}
        });
})
  .factory('FeedRefresh', function($resource){
        return $resource('/memrefresh/:feedurl', {}, {
                query: {method: 'GET', params: {feedurl: ''}, isArray: false}
        });
})
  .factory('FeedEntries', function($resource){
        return $resource('/entries/:feedurl', {}, {
                query: {method: 'GET', params: {feedurl: ''}, isArray: false}
        });
});

