// scripts.js
function toggleDetails(systemName) {
    const details = document.getElementById(`details-${systemName}`);
    if (details.style.display === "none") {
        details.style.display = "block";
    } else {
        details.style.display = "none";
    }
}
