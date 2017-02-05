window.onload = function() {
  // add Bootstrap classes to form elements
  $('form p input').addClass('form-control')
  $('form p textarea').addClass('form-control')
  $('form p label').addClass('form-control-label')

  $('.helptext').addClass('text-muted form-text small')

  // add Bootstrap classes to form error messages
  $('.errorlist').addClass('has-danger')
  $('.errorlist li').addClass('form-control-feedback')

  // add Bootstrap classes to form elements with errors
  $('.errorlist + p').addClass('has-danger')
  $('.errorlist + p input').addClass('form-control-danger')
}
