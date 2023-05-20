$(function(){

    var Form1 = $('#main__signin1');
    var Form2 = $('#main__signin2');
    var MailField = $('#id_mail').val();
    var MailFiledRecovery = $('.main__email-recovermail');
    var ResetPassBtn = $('.forgot-pass');


    ResetPassBtn.on('click', function(){
        if (MailField != false) {
            MailFiledRecovery.val(MailField)
        }
        Form1.css('display', 'none');
        Form2.css('display', 'flex');
    });
    
});