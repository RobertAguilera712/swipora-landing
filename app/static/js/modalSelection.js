function initSelection() {

    const modals = document.querySelectorAll("div.modal-selection");
    modals.forEach(modal => {
        const radios = modal.querySelectorAll("input[type=radio]")
        const input = modal.querySelector("input[type=text]")
        const checked = modal.querySelector('input[type="radio"]:checked')
        if (checked) {
            input.value = checked.dataset.label;
        }
        radios.forEach(r => {
            r.addEventListener("change", (e) => {
                input.value = e.target.dataset.label;
            });
        }
        )
    })
}

function initDataTables() {
    document.querySelectorAll("table.modal-table").forEach(t => {
        if ($.fn.DataTable.isDataTable(t)) {
            table.DataTable().destroy();
        }
        $(t).DataTable({
            language: {
                url: '../lang/ES.json'
            }
        });
    })
}

document.addEventListener("DOMContentLoaded", function () {
    initDataTables();
    initSelection();
});

document.body.addEventListener('htmx:afterSwap', function (evt) {
    // Check if the swap target is your table or container
    initSelection();
    initDataTables();
});
