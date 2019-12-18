 $('.item .title').click(function () {
        $(this).next().toggleClass('hidden').parent().siblings().children('.body').addClass('hidden');

    });

    (function () {
        $('.item .body .active').parent().toggleClass('hidden');
    })();