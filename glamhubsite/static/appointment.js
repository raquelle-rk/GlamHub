var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();

today = dd + '/' + mm + '/' + yyyy;

function setDatePicker (disabledDates) {
    $("#id_appointment_date").datetimepicker({
        format: 'd/m/Y',
        formatDate: 'd/m/Y',
        timepicker:false,
        minDate: today,
        disabledDates: disabledDates
    });
}
