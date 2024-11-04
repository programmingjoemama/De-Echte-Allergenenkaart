const filterButtons = document.querySelectorAll(".btn-filter");
const selectedAllergens = new Set();  // Set om de geselecteerde allergenen bij te houden

filterButtons.forEach(button => {
    button.addEventListener("click", function() {
        const allergen = this.getAttribute("data-filter");

        // Toggle de actieve staat van de allergenen
        if (this.classList.contains("active")) {
            selectedAllergens.delete(allergen);
            this.classList.remove("active");
        } else {
            selectedAllergens.add(allergen);
            this.classList.add("active");
        }

        // Update de gerechten op basis van geselecteerde allergenen
        filterSelection();
    });
});

function filterSelection() {
    const gerechten = document.querySelectorAll(".filterDiv");

    gerechten.forEach(gerecht => {
        let hideGerecht = false;  // Variabele om te bepalen of het gerecht moet worden verborgen
        let showAlert = false;    // Variabele om te bepalen of de alert-knop moet worden getoond

        selectedAllergens.forEach(allergen => {
            const allergenClass = allergen;        // Bijv. 'Ei'
            const allergenAlertClass = `${allergen}-alert`;  // Bijv. 'Ei-alert'

            // Als het gerecht de allergenen bevat zonder alert, moet het worden verborgen
            if (gerecht.classList.contains(allergenClass) && !gerecht.classList.contains(allergenAlertClass)) {
                hideGerecht = true;
            }

            // Als er een allergeen met '-alert' is, toon de alert-knop
            if (gerecht.classList.contains(allergenAlertClass)) {
                showAlert = true;
            }
        });

        // Als het gerecht verborgen moet worden, verberg het
        if (hideGerecht) {
            gerecht.style.display = "none";
        } else {
            gerecht.style.display = "flex";
        }

        // Toon of verberg de alert-knop
        if (showAlert && !hideGerecht) {
            showAlertButton(gerecht);
        } else {
            hideAlertButton(gerecht);
        }
    });
}

function showAlertButton(gerecht) {
    const alertBtn = gerecht.querySelector(".alert-btn");
    if (alertBtn) {
        alertBtn.style.display = "inline-block";  // Zorg ervoor dat de alert-knop zichtbaar is
    }
}

function hideAlertButton(gerecht) {
    const alertBtn = gerecht.querySelector(".alert-btn");
    if (alertBtn) {
        alertBtn.style.display = "none";  // Verberg de alert-knop
    }
}


// Selecteer de overlay en de knop
const alertOverlay = document.getElementById("alertOverlay");
const alertButton = document.querySelector(".alert-btn");

// Voeg een klikgebeurtenis toe aan de knop om de alert te tonen
alertButton.addEventListener("click", function() {
    alertOverlay.classList.add("show");
});

// Voeg een klikgebeurtenis toe aan de overlay om het venster te verbergen
alertOverlay.addEventListener("click", function() {
    alertOverlay.classList.remove("show");
});