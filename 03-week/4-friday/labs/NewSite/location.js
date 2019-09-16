var mymap = L.map('mapid').setView([29.7516754, -95.357813], 15);
var marker = L.marker([29.7516754, -95.357813]).addTo(mymap);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	id: 'mapbox.streets',
	accessToken: 'pk.eyJ1IjoiZGdyOG5pbmphIiwiYSI6ImNrMG1rZzc4dzE4M3kzbHFkOG1oMmJxbDEifQ.Hhadn5czac5nMEuj6gC_Lg'
}).addTo(mymap);