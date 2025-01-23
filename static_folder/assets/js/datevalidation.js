$(window).on('load', function() {
  // Initialize all datetimepickers with common settings
  const commonSettings = {
      format: 'h:i A',
      step: 15,
      datepicker: false,
  };

  // Apply datetimepicker to all inputs
  $('#datetimepickernew, #datetimepickernew1, #datetimepickernew2, #datetimepickernew3, #datetimepickernew4').datetimepicker(commonSettings);

  // Add datetimepicker to time-specific classes
  $('.timeON, .timeOU, .timeMC, .timeLL, .timeTF').datetimepicker({
      ...commonSettings,
      onClose: function() {
          $('#errorMsgs').modal('hide');
          return true;
      },
      validateOnBlur: false,
  });

  // Additional datepicker configuration if needed
  $('#datepicker').datetimepicker({
      i18n: {
          en: {
              months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
              dayOfWeek: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
          },
      },
      timepicker: false,
      value: "today",
      format: "d-m-Y",
      closeOnDateSelect: true,
      minDate: 0,
      weeks: false,
  });
});

// Repeat for other date pickers if needed...
