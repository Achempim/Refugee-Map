// Initialize the map
const map = L.map('map').setView([20, 0], 2); // Centered on Africa

// Load and display tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

// Load the CSV data using D3
d3.csv("Year-to-date.csv").then(function(data) {
    data.forEach(function(d) {
        // Parse the data and create markers
        const lat = +d.Latitude;
        const lon = +d.Longitude;
        const admitted = +d['Total Admitted'];

        // Create a marker for each country
        const marker = L.marker([lat, lon]).addTo(map)
            .bindPopup(`<b>${d.Country}</b><br>Total Admitted: ${admitted}`);
    });
}).catch(function(error) {
    console.error('Error loading the CSV file:', error);
});