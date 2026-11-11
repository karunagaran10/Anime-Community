
// DOM CONTENT LOADED

document.addEventListener("DOMContentLoaded", function () {

    // MOBILE MENU

    const mobileIcon = document.getElementById("myMenu");
    const menus = document.getElementById("myMenus");

    if (mobileIcon && menus) {

        const menuIcon = mobileIcon.querySelector("i");

        const setMenuOpen = function (isOpen) {
            menus.classList.toggle("active", isOpen);
            mobileIcon.setAttribute("aria-expanded", String(isOpen));
            if (isOpen) {
                menuIcon.classList.remove("bi-list");
                menuIcon.classList.add("bi-x-lg");
            } else {
                menuIcon.classList.remove("bi-x-lg");
                menuIcon.classList.add("bi-list");
            }
        };

        mobileIcon.addEventListener("click", function () {
            setMenuOpen(mobileIcon.getAttribute("aria-expanded") !== "true");
        });

        menus.addEventListener("click", function (event) {
            if (event.target.closest("a")) {
                setMenuOpen(false);
            }
        });

        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape" && mobileIcon.getAttribute("aria-expanded") === "true") {
                setMenuOpen(false);
                mobileIcon.focus();
            }
        });

    }


    // MOBILE DROPDOWN

    const serviceLink = document.getElementById("serviceLink");
    const submenu = document.querySelector(".submenu");

    if (serviceLink && submenu) {

        serviceLink.addEventListener("click", function (event) {

            if (window.innerWidth <= 768) {

                event.preventDefault();

                submenu.classList.toggle("active");

            }

        });

    }


});
