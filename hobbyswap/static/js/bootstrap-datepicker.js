$(document).ready(function () {

    $('.BtnFirst').on('click', function () {
        $('.firstPart').toggle('slow');
        $('.secondPart').toggle('slow');

    });
    $('.BtnLast').on('click', function () {

        $('.secondPart').toggle('slow');

        $('.lastPart').toggle('slow');
    });


});