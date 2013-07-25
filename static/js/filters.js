quote = function(s){
	return encodeURIComponent(s).replace(':','%3A'); }

unquote = function(s){
	return decodeURIComponent(s.replace('%3A',':')); }

angular.module('urlEncoding', []).
  filter('truncate', function() {
    return function(input,size) {
      if (typeof input != "undefined") {
        if (input.length > size){
          input=input.substr(0,size) + "...";
        }
      return input;
      }
    }
  }).
  filter('urlbuild', function() {
    return function(input,path,double_quote) {
      if (double_quote) {
        input = quote(quote(input));
      } else {
        input = quote(input);
      }
      return "#/" + path + "/" + input
  }}).
  filter('feedurl', function() {
    return function(input) {
      return "#/feed/" + quote(quote(input));
    }
  }).
  filter('entriesurl', function() {
    return function(input) {
      return "#/entries/" + quote(quote(input));
    }
  }).
  filter('entriesfeedlinkurl', function() {
    return function(input) {
      return "#/entries/" + quote(input);
    }
  }).
  filter('feedlinkurl', function() {
    return function(input) {
      return "#/entries/" + quote(input);
    }
  }).
  filter('feedrefreshurl', function() {
    return function(input) {
      return "#/refresh/" + quote(input);
    }
  }).
  filter('feedhtmlurl', function() {
    return function(input) {
      return "/feed/html/" + quote(input);
    }
  }).
  filter('opmlfeedhtmlurl', function() {
    return function(input) {
      return "/feed/html/" + quote(quote(input));
    }
  });

