// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('starter', ['ionic'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if(window.cordova && window.cordova.plugins.Keyboard) {
      // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
      // for form inputs)
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);

      // Don't remove this line unless you know what you are doing. It stops the viewport
      // from snapping when text inputs are focused. Ionic handles this internally for
      // a much nicer keyboard experience.
      cordova.plugins.Keyboard.disableScroll(true);
    }
    if(window.StatusBar) {
      StatusBar.styleDefault();
    }
  });
})


.controller('RadioCtrl', ['$scope', 'RadioService', 'MPCService', function($scope, RadioService, MPCService) {

  $scope.channels = [];

  RadioService.getChannels().success(function(channels){
    $scope.channels = channels;
  })

  $scope.changeChannel = function (channelUrl){
    MPCService.controlRadio({"channel" : channelUrl}).success(function(response){
      console.log(response);
    })
  }

  $scope.changeVolume = function (volumeChange){
    MPCService.controlRadio({"volume" : volumeChange}).success(function(response){
      console.log(response);
    })
  }

  $scope.turnOffRadio = function (){
    MPCService.controlRadio({off : "off"}).success(function(response){
      console.log(response);
    })
  }

}])

.service('RadioService', ['$http',  function($http) {
	return {
		getChannels: function(){
			return $http.get("db/channels.json");
		}
	}
}])


.service('MPCService', ['$http',  function($http) {
	return {
		controlRadio: function(data){
			return $http.post("mpc.php", data);
		}
	}
}])