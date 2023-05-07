$(function(){

    var Mail = $('.mail-f');
    var Password = $('.pass-f');
    var ConfPass = $('.pass-f-con');
    var VerCode = $('.code-f');
    var FirstButton = $('.main__form_submit_button');
    var SecondButton = $('.main__form_submit_button2');
    var Body = $('.main__signup_cnt');
    var RegForm1 = $('.main__signup_cnt');
    var RegForm2 = $('.main__signup_cnt2');



    Mail.on('keyup', function(){
        var mail;
        mail = Mail.val();
        if (!Mail.val().includes('@') || (mail == "") || !Mail.val().includes('.'))  {
            Mail.css('border-color','red');
            mail = Mail.val();
        } else {
            Mail.css('border-color','#27cf7f');
            mail = Mail.val();
        }
    });

    Password.on('keyup', function(){
        var pass_code;
        pass_code = $('.pass-f').val();
        if ((!/^[a-z0-9]+$/.test(pass_code) == true) && (!/^[A-Z0-9]+$/.test(pass_code) == true) && ( !/^[A-Za-z]+$/.test(pass_code) == true) && (pass_code.length >= 8) && (pass_code != "")) {
            $('.pass-f').css('border-color','#27cf7f');
        } else {
            $('.pass-f').css('border-color','red');
        }
    });
    Password.on('keydown', function(){
        var pass;
        pass = Password.val();
    });
    
    Password.on('keyup', function(){
        var pass;
        pass = Password.val();
        if ((!/^[a-z0-9]+$/.test(pass) == true) && (pass != "")) {
            $('.tick-one').css('display','inline');
            $('.check-one').css('display','none');
            var tick_one = true;
        } else {
            $('.tick-one').css('display','none');
            $('.check-one').css('display','inline');
            var tick_one = false;
        }
    });
    Password.on('keyup', function(){
        var pass;
        pass = Password.val();
        if (( !/^[A-Z0-9]+$/.test(pass) == true) && (pass != ""))  {
            $('.tick-three').css('display','inline');
            $('.check-three').css('display','none');
            var tick_two = true;
        } else {
            $('.tick-three').css('display','none');
            $('.check-three').css('display','inline');
            var tick_two = false;
        }
    });
    Password.on('keyup', function(){
        var pass;
        pass = Password.val();
        if (( !/^[A-Za-z]+$/.test(pass) == true) && (pass != ""))  {
            $('.tick-two').css('display','inline');
            $('.check-two').css('display','none');
            var tick_three = true;
        } else {
            $('.tick-two').css('display','none');
            $('.check-two').css('display','inline');
            var tick_three = false;
        }	
    });
    Password.on('keyup', function(){
        var pass;
        pass = Password.val();
        if ( pass.length >= 8)  {
            $('.tick-four').css('display','inline');
            $('.check-four').css('display','none');
            var tick_four = true;
        } else {
            $('.tick-four').css('display','none');
            $('.check-four').css('display','inline');
            var tick_four = false;
        }	
    });
    ConfPass.on('keyup',function(){
        let pass_code = Password.val();
        let confirmpass_code = ConfPass.val();
        if (pass_code == confirmpass_code && confirmpass_code != "") {
            ConfPass.css('border-color','#27cf7f');
        } else {
            ConfPass.css('border-color','red');
        }
    });
    Body.on('click', function(){
        if (Mail.val() != "" && Password.val() != "" && ConfPass.val() != "" && Password.val() == ConfPass.val() && $('.mail-f').val().indexOf('@') != -1 && (!/^[a-z0-9]+$/.test(pass) == true) && ( !/^[A-Z0-9]+$/.test(pass) == true) && ( !/^[A-Za-z]+$/.test(pass) == true) && ( pass.length >= 8) && ($('input[type="checkbox"]').prop("checked") == true)) {
            FirstButton.css('background-color', '#27cf7f');
        } else {
            FirstButton.css('background-color', 'grey');
        }
    });
    Body.on('keyup', function(){
        if (Mail.val() != "" && Password.val() != "" && ConfPass.val() != "" && Password.val() == ConfPass.val() && $('.mail-f').val().indexOf('@') != -1 && (!/^[a-z0-9]+$/.test(pass) == true) && ( !/^[A-Z0-9]+$/.test(pass) == true) && ( !/^[A-Za-z]+$/.test(pass) == true) && ( pass.length >= 8) && ($('input[type="checkbox"]').prop("checked") == true)) {
            FirstButton.css('background-color', '#27cf7f');
            FirstButton.css('cursor', 'pointer');
        } else {
            FirstButton.css('background-color', 'grey');
            FirstButton.css('cursor', 'not-allowed');
        }
    });
    FirstButton.on('click', function(){
        pass = Password.val();
        ourmail = Mail.val();
        if (Mail.val() != "" && Password.val() != "" && ConfPass.val() != "" && Password.val() == ConfPass.val() && $('.mail-f').val().indexOf('@') != -1 && (!/^[a-z0-9]+$/.test(pass) == true) && ( !/^[A-Z0-9]+$/.test(pass) == true) && ( !/^[A-Za-z]+$/.test(pass) == true) && ( pass.length >= 8) && ($('input[type="checkbox"]').prop("checked") == true)) {
            FirstButton.text('Please wait...')
            $.ajax({
                type: 'POST',
                url: 'generatepass/',
                data: {
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    mail: ourmail,
                },
                success: function() {
                    RegForm1.css('display', 'none');
                    RegForm2.css('display', 'flex');
                }
            });
        } else if (($('input[type="checkbox"]').prop("checked") != true)) {
            $('.you-agree-terms-policy__text').css('color', 'red');
        } else if (!Mail.val().includes('@') || (mail == "") || !Mail.val().includes('.')) {
            Mail.css('border-color','red');
        } else if (Password.val() == "") {
            Password.css('border-color','red');
        } else if (Password.val() != ConfPass.val()) {
            ConfPass.css('border-color','red');
        }
    });
    SecondButton.on('click', function(){
        code = VerCode.val();
        if (code != "") {
            SecondButton.text('Please wait...')
            $.ajax({
                type: 'POST',
                url: 'verify/',
                data: {
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    code: code,
                    mail: ourmail,
                    password: pass,
                },
                success: function() {
                    // RegForm1.css('display', 'none');
                    // RegForm2.css('display', 'flex');
                }
            });
        }
    });
});