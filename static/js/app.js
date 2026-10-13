(function () {
    "use strict";

    function initNavbar() {
        const menuButton = document.getElementById("cnMenuBtn");
        const navLinks = document.getElementById("cnNavLinks");

        if (!menuButton || !navLinks) return;

        function closeMenu() {
            navLinks.classList.remove("cn-open");
            menuButton.setAttribute("aria-expanded", "false");
            menuButton.setAttribute("aria-label", "باز کردن منو");
            menuButton.textContent = "☰";
        }

        menuButton.addEventListener("click", function () {
            const isOpen = navLinks.classList.toggle("cn-open");

            menuButton.setAttribute(
                "aria-expanded",
                String(isOpen)
            );

            menuButton.setAttribute(
                "aria-label",
                isOpen ? "بستن منو" : "باز کردن منو"
            );

            menuButton.textContent = isOpen ? "×" : "☰";
        });

        navLinks.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", closeMenu);
        });

        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape") {
                closeMenu();
            }
        });

        window.addEventListener("resize", function () {
            if (window.innerWidth > 900) {
                closeMenu();
            }
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initNavbar);
    } else {
        initNavbar();
    }
})();
<script>
document.querySelectorAll(".toast-message").forEach(function (toast) {
    setTimeout(function () {
        toast.classList.add("hiding");

        setTimeout(function () {
            toast.remove();
        }, 350);
    }, 3500);
});
</script>
<script>
document.querySelectorAll(".cn-toast").forEach(function (toast) {
    setTimeout(function () {
        if (!toast.isConnected) return;

        toast.classList.add("hiding");

        setTimeout(function () {
            toast.remove();
        }, 350);
    }, 3500);
});
</script>