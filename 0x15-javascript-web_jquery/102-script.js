$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const langCode = $('input#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function (data) {
      $('div#hello').html(data.hello);
    });
  });
});
