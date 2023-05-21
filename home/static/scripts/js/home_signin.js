$(function(){

    var Form1 = $('#main__signin1');
    var Form2 = $('#main__signin2');
    var Form3 = $('#main__signin3');
    var Form4 = $('#main__signin4');
    var MailField = $('#id_mail').val();
    var MailFiledRecovery = $('.main__email-recovermail');
    var CodeField = $('.main__code-approve');
    var PassField1 = $('.main__new-pass');
    var PassField2 = $('.main__new-pass2');
    var ResetPassBtn = $('.forgot-pass');
    var ResetPassBtn2 = $('.main__resetpass-btn');
    var ResetPassBtn3 = $('.main__code-approve-btn')
    var ResetPassBtn4 = $('.main__setnewpass-btn')


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
                    Form2.css('display', 'none');
                    Form3.css('display', 'flex');
                }
            });
        }
    });

    CodeField.on('keyup', function(){
        var approve_code = CodeField.val();
        if (approve_code.length != 6)  {
            CodeField.css('border-color','red');
            approve_code = CodeField.val();
            ResetPassBtn3.css('background-color', '#c5c5c5');
            ResetPassBtn3.css('cursor', 'not-allowed');
        } else {
            CodeField.css('border-color','#27cf7f');
            approve_code = CodeField.val();
            ResetPassBtn3.css('background-color', '#27cf7f');
            ResetPassBtn3.css('cursor', 'pointer');
        }
    });


    ResetPassBtn3.on('click', function(){
        if (approve_code.length != 6) {
            CodeField.css('border-color','red');
            approve_code = CodeField.val();
            ResetPassBtn3.css('background-color', '#c5c5c5');
            ResetPassBtn3.css('cursor', 'not-allowed');
        } else {
            ResetPassBtn3.text('Проверка кода...');
            approve_code = CodeField.val();
            $.ajax({
                type: 'POST',
                url: '/login/checkcode/',
                data: {
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    approve_code: approve_code,
                    mail: mail,
                },
                success: function(response) {
                    var requestcode = response.encrypted_code;
                }
            });
        }
    });

    PassField1.on('keyup', function(){
        var new_pass_code;
        new_pass_code = PassField1.val();
        if ((!/^[a-z0-9]+$/.test(new_pass_code) == true) && (!/^[A-Z0-9]+$/.test(new_pass_code) == true) && ( !/^[A-Za-z]+$/.test(new_pass_code) == true) && (new_pass_code.length >= 8) && (new_pass_code != "")) {
            PassField1.css('border-color','#27cf7f');
        } else {
            PassField1.css('border-color','red');
        }
    });

    PassField2.on('keyup', function(){
        var new_pass_code2;
        new_pass_code2 = PassField2.val();
        if ((!/^[a-z0-9]+$/.test(new_pass_code2) == true) && (!/^[A-Z0-9]+$/.test(new_pass_code2) == true) && ( !/^[A-Za-z]+$/.test(new_pass_code2) == true) && (new_pass_code2.length >= 8) && (new_pass_code2 != "") && (new_pass_code2 == new_pass_code)) {
            PassField2.css('border-color','#27cf7f');
        } else {
            PassField2.css('border-color','red');
        }
    });


    ResetPassBtn4.on('click', function(){
        if ((!/^[a-z0-9]+$/.test(new_pass_code2) == true) && (!/^[A-Z0-9]+$/.test(new_pass_code2) == true) && ( !/^[A-Za-z]+$/.test(new_pass_code2) == true) && (new_pass_code2.length >= 8) && (new_pass_code2 != "") && (new_pass_code2 == new_pass_code)) {
            ResetPassBtn4.text('Смена пароля...');
            new_password = PassField1.val();
            $.ajax({
                type: 'POST',
                url: '/login/setnewpassword/',
                data: {
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    mail: mail,
                    requestcode: requestcode,
                    new_password: new_password,
                },
                success: function() {
                    window.location.href = '/login/'
                }
            });
        } else {
            PassField1.css('border-color','red');
            PassField2.css('border-color','red');
        }
    });


});