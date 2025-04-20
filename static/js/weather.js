// b17f25127cdbd86a6ea89d46f1a240f9

const apiKey = "4dc6e972cf0dfbf8ff347e337e133e4c";
console.log('hi');

function fetchWeather() {
    console.log('hi');
    const city = document.getElementById("cityInput").value;
    if (city === "") {
        alert("Please enter a city name!");
        return;
    }

    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;


    // fetch(url)
    //     .then(response => response.json())
    //     .then(data => {
    //         // console.log(data);
    //         const iconCode = data.weather[0].icon;

    //         document.getElementById("cityName").innerText = data.name;
    //         document.getElementById("weatherDesc").innerText = data.weather[0].description;
    //         document.getElementById("temperature").innerText = `${data.main.temp}°C`;
    //         document.getElementById("humidity").innerText = data.main.humidity;
    //         document.getElementById("windSpeed").innerText = data.wind.speed;
    //         document.getElementById("rain").innerText = data.rain ? data.rain["1h"] : "No Rain";

    //         const sunriseTime = new Date(data.sys.sunrise * 1000).toLocaleTimeString();
    //         const sunsetTime = new Date(data.sys.sunset * 1000).toLocaleTimeString();
    //         document.getElementById("sunrise").innerText = sunriseTime;
    //         document.getElementById("sunset").innerText = sunsetTime;

    //         document.getElementById("imges").innerHTML = '<img src="https://openweathermap.org/img/wn/${iconCode}@2x.png" alt="${data.weather[0].description}"> ';

    //         suggestFarmingTips(data);
    //     })
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const iconCode = data.weather[0].icon;

            document.getElementById("cityName").innerText = data.name;
            document.getElementById("weatherDesc").innerText = data.weather[0].description;
            document.getElementById("temperature").innerText = `${data.main.temp}°C`;
            document.getElementById("humidity").innerText = `${data.main.humidity}%`;
            document.getElementById("windSpeed").innerText = `${data.wind.speed} m/s`;
            document.getElementById("rain").innerText = data.rain ? `${data.rain["1h"]} mm` : "No Rain";

            const sunriseTime = new Date(data.sys.sunrise * 1000).toLocaleTimeString();
            const sunsetTime = new Date(data.sys.sunset * 1000).toLocaleTimeString();
            document.getElementById("sunrise").innerText = sunriseTime;
            document.getElementById("sunset").innerText = sunsetTime;

            // Fixing icon display using proper template literals
            document.getElementById("imges").innerHTML = `
        <img src="/static/img/icons/${data.weather[0].description}.png" 
             alt="" height="90px" width="90px"
             title="${data.weather[0].description}">
      `;

            suggestFarmingTips(data);
        })
        .catch(() => alert("City not found!"));
}

function suggestFarmingTips(data) {
    const temp = data.main.temp;
    const rain = data.rain ? data.rain["1h"] : 0;
    const humidity = data.main.humidity;
    let suggestion = "Weather is stable for general farming activities.";

    if (temp > 35) {
        suggestion = "High temperature! Irrigate crops more frequently.";
    } else if (temp < 15) {
        suggestion = "Cold weather detected! Protect sensitive crops.";
    } else if (rain > 5) {
        suggestion = "Heavy rainfall! Drain excess water from fields.";
    } else if (humidity > 80) {
        suggestion = "High humidity! Risk of fungal infections in crops.";
    }

    document.getElementById("suggestions").innerText = suggestion;
}
