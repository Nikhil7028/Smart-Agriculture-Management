const NEWS_URL = "/api/news/";

document.addEventListener("DOMContentLoaded", function () {
    fetch(NEWS_URL)
        .then(response => response.json())
        .then(data => {
            console.log("Fetched News Data:", data); // ✅ Log the full API response here

            if (!data.articles || data.articles.length === 0) {
                throw new Error("No articles found. Check API key or query.");
            }

            const newsList = document.getElementById("news-list");
            newsList.innerHTML = "";

            data.articles.slice(0, 5).forEach(article => {
                const li = document.createElement("li");
                const a = document.createElement("a");
                a.href = article.url;
                a.target = "_blank";
                a.textContent = article.title;
                li.appendChild(a);
                newsList.appendChild(li);
            });
        })
        .catch(error => {
            console.error("Error fetching news:", error);
            document.getElementById("news-list").innerHTML = "<li>Failed to load news. Try again later.</li>";
        });
});
