window.onload = function() {
  $('form p input').addClass('form-control')
  $('form p textarea').addClass('form-control')

  $('.helptext').addClass('text-muted form-text')

  var errList = $('.errorlist')
  errList.addClass('has-danger')
  $('li', errList).addClass('form-control-feedback')
  $('.errorlist + p').addClass('has-danger')
  $('.errorlist + p input').addClass('form-control-danger')
}
