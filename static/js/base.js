document.addEventListener("DOMContentLoaded", function() {
    var logoutForm = document.getElementById("logout-form");
    if (logoutForm) {
        logoutForm.addEventListener("submit", function(event) {
            var confirmed = confirm("Are you sure you want to log out?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    }
});