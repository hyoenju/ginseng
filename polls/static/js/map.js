var myCenter=new google.maps.LatLng(37.4492463,127.1285137);
var marker;

function initialize(){
	var mapProp = {
		center:myCenter,
		zoom:15,
		mapTypeId:google.maps.MapTypeId.ROADMAP
	};

	var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

	var marker=new google.maps.Marker({
		position:myCenter,
		animation:google.maps.Animation.BOUNCE
	});

	marker.setMap(map);
}

google.maps.event.addDomListener(window, 'load', initialize);
