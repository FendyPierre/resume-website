mapboxgl.accessToken = 'pk.eyJ1IjoiZmVuZHlwaWVycmUiLCJhIjoiY2w2Nzl0bXJ6MDFiMjNxbW4yeWZnOGk5ayJ9.fVpRwtH84Wvc6Zz0kle4Rw';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v10',
	center: [-97.517054, 35.472989], // starting position
    zoom: 11 // starting zoom
});
		
// create the popup
var popup = new mapboxgl.Popup({ offset: 40 }).setText(
    '756 Livingston Street, Brooklyn, NY 11201'
);

// create DOM element for the marker
var el = document.createElement('div');
el.id = 'marker';
 
// create the marker
new mapboxgl.Marker(el)
    .setLngLat([-73.9751,40.7289])
    .setPopup(popup) // sets a popup on this marker
    .addTo(map);

// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl(), 'bottom-right');