// ALL MAIN SCRIPTS

// FANCYBOX


$(function(){
	$(".fancybox").fancybox({
        padding: 0,

        openEffect : 'elastic',
        openSpeed  : 650,

        closeEffect : 'elastic',
        closeSpeed  : 550,
    });


    var portImgWidth = $('.port-img').innerWidth();
    $('.mask').css("width", portImgWidth);
})

// END OF FANCYBOX

// PANEL CONTROLS


$(document).ready(function() {
	$('.accordion').find('.accordion-toggle').click(function() {
		$(this).next().slideToggle('600');
		$(".accordion-content").not($(this).next()).slideUp('600');
	});
	$('.accordion-toggle').on('click', function() {
		$(this).toggleClass('active').siblings().removeClass('active');
	});
});

// END OF PANEL CONTROLS


// MIXITUP CONTROLLER

$(function(){

	$('button').click(function(){
		$('.projects').mixItUp('filter', 'all');
	});
})



// COOKIES

$(document).ready(function()
{
    $('.alert').hide();

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
})

// SENDING MESSAGE

$(document).on('submit', '#form_message', function(e){
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: 'send',
        data:{
            name: $('.name-msg').val(),
            email: $('.email-msg').val(),
            message: $('.msg-message').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success:function()
        {
            $('.alert').show();
        }
    });
    $('.name').val("");
    $('.email').val("");
    $('.msg-message').val("");
    $('.alert').addClass('wow fadeInDown');
})
