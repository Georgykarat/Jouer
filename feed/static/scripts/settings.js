$(function(){

  var ChangePassCnt = $('.item__change_pass');
  var ChangePassWindow1 = $('.main__settings_changepass-1cnt');
  var ChangePassWindow2 = $('.main__settings_changepass-2cnt');
  var Field1 = $('#field1');
  var Field2 = $('#field2');
  var Field3 = $('#field3');
  var ChangePassBtn = $('.main__settings_changepass-2cnt_btn');

  $('#main').on('click', function(event){
    var $target = $(event.target);
    if (!$target.closest('.item__change_pass').length && $('.item__change_pass').is(':visible')) {
      ChangePassWindow1.css('display', 'flex');
      ChangePassWindow2.css('display', 'none');
    }
  }); 
  
  ChangePassCnt.on('click', function(){
    ChangePassWindow1.css('display', 'none');
    ChangePassWindow2.css('display', 'flex');
  });

  ChangePassCnt.on('keyup', function(){
    if ((Field1.val() != "") && (Field2.val() != "") && (Field3.val() != "") && (Field2.val() == Field3.val()) && (Field1.val() != Field2.val())) {
      ChangePassBtn.css('background-color', '#26D07C');
      ChangePassBtn.css('color', 'azure');
      ChangePassBtn.css('cursor', 'pointer');
    } else {
      ChangePassBtn.css('background-color', 'rgb(231, 231, 231)');
      ChangePassBtn.css('color', 'grey');
      ChangePassBtn.css('cursor', 'not-allowed');
    }
  });

  ChangePassBtn.on('click', function(){
    if ((Field1.val() != "") && (Field2.val() != "") && (Field3.val() != "") && (Field2.val() == Field3.val()) && (Field1.val() != Field2.val())) {
      ChangePassBtn.text('Подождите...');
      $.ajax({
        type: 'POST',
        url: 'changepassword/',
        data: {
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            oldpass: Field1.val(),
            newpass: Field2.val(),
            newpass2: Field3.val(),
        },
        success: function() {
          ChangePassWindow1.css('display', 'flex');
          ChangePassWindow2.css('display', 'none');
          Field1.val("");
          Field2.val("");
          Field3.val("");
          ChangePassBtn.text('Смените пароль');
        },
        error: function(xhr) {

        }
    });
    }
  })


});