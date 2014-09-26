/**
 * Created by Travis on 9/25/14.
 */
$(document).ready( function(){
    $('.ownerBtn').on('click', function(){
        $('.ownerAbout').toggle();
    });
    $('.renterBtn').on('click', function(){
        $('.renterAbout').toggle();

    });
});