$('.parent-control').click(function () {
    $(this).toggleClass('fa-caret-right');
    $(this).parent().parent().nextUntil('.parent').toggleClass('hidden');
});