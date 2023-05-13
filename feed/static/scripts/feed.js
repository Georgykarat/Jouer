$(function(){

    var TopPane = $('.header__center-cnt');
    var ProfileButton = $('.header__bg_profile-picture');

    TopPane.mouseenter(function() {
        ProfileButton.animate({
          left: '0px'
        }, 400);
    }).mouseleave(function() {
        ProfileButton.animate({
          left: '50px'
        }, 400);
    });


});