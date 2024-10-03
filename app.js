// Fetch data from your API endpoint
async function fetchData() {
    const response = await fetch('/api/data');
    return await response.json();
}

// Create charts
async function createCharts() {
    const data = await fetchData();
    
    const timestamps = data.map(item => item.timestamp);
    const temperatures = data.map(item => item.temperature);
    const humidities = data.map(item => item.humidity);

    new Chart(document.getElementById('temperatureChart'), {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Temperature (°C)',
                data: temperatures,
                borderColor: 'rgb(255, 99, 132)',
                tension: 0.1
            }]
        }
    });

    new Chart(document.getElementById('humidityChart'), {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Humidity (%)',
                data: humidities,
                borderColor: 'rgb(54, 162, 235)',
                tension: 0.1
            }]
        }
    });
}

createCharts();
