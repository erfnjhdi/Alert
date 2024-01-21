let map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'),
    {
        center: {lat: 45.5019 , lng: -73.561668},
        zoom: 12,
    });
    /*const location = document.getElementById('button');
    location.textContent = 'Go to My Location';
    location.classList.add("map-button");
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(location);
    location.addEventListener('click', () => {
        if (navigator.geolocation){
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const pos = {
                        lat: position.coords.latitude,
                        lng: position.coords.longtitude,
                    };
                    map.setCenter(pos);
                    const marker = new google.maps.Marker({
                        position: pos,
                        map: map
                    });
                    map.setZoom(17);
                }
            )
        }
    })*/
    document.getElementById('NextBtn').addEventListener('click', function() {
        // Get the location input value
        const locationInputValue = document.getElementById('locationInput').value;
    
        // Use Geocoding API to get the coordinates for the entered location
        const geocoder = new google.maps.Geocoder();
        geocoder.geocode({ address: locationInputValue }, function(results, status) {
          if (status === 'OK' && results.length > 0) {
            const location = results[0].geometry.location;
    
            // Set a marker and zoom in on the entered location
            map.setCenter(location);
            map.setZoom(15);
    
            const marker = new google.maps.Marker({
              position: location,
              map: map,
              title: 'Crime Location'
            });
            window.location.href = 'next.html';
          } else {
            alert('Location not found. Please enter a valid location.');
          }
        });
      });
}
/*function spot (){
    map = new google.maps.Map(document.getElementById('map'),
    {
        center: {lat: 45.5019 , lng: -73.561668},
        zoom: 12,
    });
}*/
window.initMap = initMap;