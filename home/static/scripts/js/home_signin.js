$(function(){

    var Form1 = $('#main__signin1');
    var Form2 = $('#main__signin2');
    var Form3 = $('#main__signin3');
    var MailField = $('#id_mail').val();
    var MailFiledRecovery = $('.main__email-recovermail');
    var ResetPassBtn = $('.forgot-pass');
    var ResetPassBtn2 = $('.main__resetpass-btn');
    var ResetPassBtn3 = $('.main__code-approve-btn')


    ResetPassBtn.on('click', function(){
        if (MailField != false) {
            MailFiledRecovery.val(MailField)
        }
        Form1.css('display', 'none');
        Form2.css('display', 'flex');
    });


    MailFiledRecovery.on('keyup', function(){
        var mail = MailFiledRecovery.val();
        if (!mail.includes('@') || (mail == "") || !mail.includes('.'))  {
            MailFiledRecovery.css('border-color','red');
            mail = MailFiledRecovery.val();
            ResetPassBtn2.css('background-color', '#c5c5c5');
            ResetPassBtn2.css('cursor', 'not-allowed');
        } else {
            MailFiledRecovery.css('border-color','#27cf7f');
            mail = MailFiledRecovery.val();
            ResetPassBtn2.css('background-color', '#27cf7f');
            ResetPassBtn2.css('cursor', 'pointer');
        }
    });


    ResetPassBtn2.on('click', function(){
        if (!mail.includes('@') || (mail == "") || !mail.includes('.')) {
            MailFiledRecovery.css('border-color','red');
            mail = MailFiledRecovery.val();
            ResetPassBtn2.css('background-color', '#c5c5c5');
            ResetPassBtn2.css('cursor', 'not-allowed');
        } else {
            ResetPassBtn2.text('Генерация кода...');
            mail = MailFiledRecovery.val();
            $.ajax({
                type: 'POST',
                url: 'changepass/',
                data: {
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    mail: mail,
                },
                success: function() {
                    // window.location.href = '/feed/'
                    // RegForm1.css('display', 'none');
                    // RegForm2.css('display', 'flex');
                }
            });
        }
    });
    
});