document.addEventListener("DOMContentLoaded", function () {
    console.log("Initializing map...");

    // Initialize the map
    var map = L.map('map').setView([51.0447, -114.0719], 12); // Calgary default location

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    console.log("Map initialized successfully!");


    // Function to add bus markers
    function showBusMarkers() {
        console.log("Adding static bus locations...");
        busLocations.forEach(bus => {
            var marker = L.marker([bus.latitude, bus.longitude])
                .bindPopup(`<b>${bus.vehicle_id}</b><br>Lat: ${bus.latitude}<br>Lon: ${bus.longitude}`)
                .addTo(map);
        });
    }

    // Add bus markers immediately when page loads
    showBusMarkers();

    // Refresh button (not fetching data, just reloading static buses)
    var refreshButton = document.getElementById("refresh-btn");
    if (refreshButton) {
        refreshButton.addEventListener("click", function () {
            console.log("Refreshing bus locations...");
            showBusMarkers();
        });
    } else {
        console.error("Refresh button not found!");
    }
});
