// Function to close the sidebar
function closeSidebar() {
    document.querySelector(".sidebar").classList.remove("open");
}

// Event listener for the hamburger icon
document.querySelector(".hamburger").addEventListener("click", function () {
    document.querySelector(".sidebar").classList.toggle("open");
});

// Event listener for the close button
document.querySelector(".close-btn").addEventListener("click", function () {
    closeSidebar();
});
