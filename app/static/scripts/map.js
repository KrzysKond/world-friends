



document.addEventListener('DOMContentLoaded', function() {
    let map = L.map('map').setView([20, 0], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);



    let currentYear = new Date().getFullYear()
    fetch('/friends-locations/')
        .then(response => response.json())
        .then(data => {
            data.forEach(person => {
            const photoHtml = person.photo
                ? `
                    <img src="${person.photo}" alt="${person.name}'s photo" style="width:100px;height:auto;"/>
                   `
                : '';



            const popupContent = `
                <a href="/person/${person.id}/" style="text-decoration: none; color: inherit; display: block;">
                    <strong>${person.name}</strong><br>
                    Origin: ${person.origin}<br>
                    Age: ${new Date().getFullYear() - person.born}<br><br>
                    ${photoHtml}
                </a>`;




            // Add a marker for each friend
            L.marker([parseFloat(person.latitude), parseFloat(person.longitude)])
                .addTo(map)
                .bindPopup(popupContent);
            });
         })
        .catch(error => {
            console.error('Error fetching friend locations:', error);
        });



    let form = document.querySelector('form');


    let latitudeInput = form.querySelector('input[name="latitude"]');
    if (!latitudeInput) {
        latitudeInput = document.createElement('input');
        latitudeInput.setAttribute('name', 'latitude');
        latitudeInput.setAttribute('id', 'latitude');
        form.appendChild(latitudeInput);
    }

    let longitudeInput = form.querySelector('input[name="longitude"]');
    if (!longitudeInput) {
        longitudeInput = document.createElement('input');
        longitudeInput.setAttribute('name', 'longitude');
        longitudeInput.setAttribute('id', 'longitude');
        form.appendChild(longitudeInput);
    }

    let currentMarker = null

    map.on('dblclick', function(e) {
        let latitude = e.latlng.lat;
        let longitude = e.latlng.lng;

        if(currentMarker){
            map.removeLayer(currentMarker);
        }

        currentMarker = L.marker([latitude, longitude]).addTo(map);
        currentMarker.bindPopup('Point selected at ' + latitude.toFixed(4) + ', ' + longitude.toFixed(4)).openPopup();

        // Update the hidden inputs
        latitudeInput.value = latitude.toFixed(6);
        longitudeInput.value = longitude.toFixed(6);
    });
});
