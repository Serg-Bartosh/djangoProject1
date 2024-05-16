document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("searchButton").addEventListener("click", function () {
        let input = document.getElementById('searchInput').value;
        window.location.href = "search/" + encodeURIComponent(input);
    });
});
