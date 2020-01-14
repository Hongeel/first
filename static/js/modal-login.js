$(function(){
    var formAjaxSubmit = function(form, modal) {
        $(form).submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function (xhr, ajaxOptions, thrownError) {
                    if ( $(xhr).find('.has-error').length > 0 ) {
                        $(modal).find('.modal-body').html(xhr);
                        formAjaxSubmit(form, modal);
                    } else {
                        $(modal).modal('toggle');
                        window.location.href = '/cookbook/';
                    }
                },
                error: function (xhr, ajaxOptions, thrownError) {
                // handle response errors here
                }
            });
        });
    }
    $('#login-button').click(function() {
        $('#modal-login-body').load('../../../login/', function () {
            $('#modal-login').modal('toggle');
            formAjaxSubmit('#modal-login-body form', '#modal-login');
        });
    })
  })