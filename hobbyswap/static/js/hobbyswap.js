/**
 * Created by Travis on 9/25/14.
 */
$(document).ready(function () {
    $('.ownerBtn').on('click', function () {
        $('.ownerAbout').toggle();
    });
    $('.renterBtn').on('click', function () {
        $('.renterAbout').toggle();

    });

    $('.searchBTN').on('click', function () {
        var searched = $('.hobbySearchInput').val();

        var searchdata = JSON.stringify(searched);
        console.log(searchdata);
        console.log(searched);

        $.ajax({
            url: '/search/',
            type: 'POST',
            dataType: 'json',
            data: searchdata,
            success: function (response) {

                  $.each(response,function(index,item) {
                      console.log(item.fields);
                      console.log(response);


                  });



//                $('.searchResults').html('<div class="col-md-4"><div class="thumbnail"> <div class="class1 text-center"><p>{{ listing.category }}</p><div class="image">'+
//                '<img class="profile" src="{{ listing.image.url }}" alt="Profile picture" height="75"' +
//                'width="75"></div ><div class="details"><p><a href="{% url "view_listing" '+response.pk %}" class="class-name">{{ listing }}</a></p><p class="postBy"> Posted by: {{ listing.post_user }}</p>'+
//                </div><div class= "cost" ><p><a href="{% url 'view_listing' listing.id %}"class="cost-button"><strong>${{ listing.price }}</strong>per day</a></p></div ></div></div>')
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});