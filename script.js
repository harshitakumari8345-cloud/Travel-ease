document.addEventListener("DOMContentLoaded", function () {
    const plannerForm = document.querySelector(".planner-form");

    if (plannerForm) {
        plannerForm.addEventListener("submit", function (event) {
            const days = Number(document.getElementById("days").value);
            const people = Number(document.getElementById("people").value);

            if (!Number.isInteger(days) || days < 1 || days > 30) {
                event.preventDefault();
                alert("Please enter trip duration between 1 and 30 days.");
                return;
            }

            if (!Number.isInteger(people) || people < 1 || people > 20) {
                event.preventDefault();
                alert("Please enter between 1 and 20 travellers.");
                return;
            }
        });
    }
});