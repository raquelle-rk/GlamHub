$(function() {
    $('#datepicker').datepicker({
      onSelect: function(dateText) {
   $('#datepicker2').datepicker("setDate", $(this).datepicker("getDate"));
      }
    });
  });

  $(function() {
    $("#datepicker2").datepicker();
  });