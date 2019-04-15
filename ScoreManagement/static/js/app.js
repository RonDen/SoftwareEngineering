$(function () {

    $('.prev-slide').on('click', function() {
       $('#slide-show').carousel('prev');
    });

    $('.next-slide').on('click', function() {
        $('#slide-show').carousel('next');
    });

    $(document).on('keydown', function (e) {
       console.log(e.which);
       switch (e.which) {
           case 37:
               $('#slide-show').carousel('prev');
               break;
           case 39:
               $('#slide-show').carousel('next');
               break;
       }
    });

    var play = false;
    $('.play-and-stop').click(function () {
        if (!play) {
            $('#slide-show').carousel('cycle');
            $(this).children('span').removeClass('glyphicon-play').addClass('glyphicon-pause');
        } else{
            $('#slide-show').carousel('pause');
            $(this).children('span').removeClass('glyphicon-pause').addClass('glyphicon-play');
        }
        play = !play;
    });
});