
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
# Create your views here.
from hobby import settings
from hobbyswap.forms import EmailUserCreationForm, PostItemForm, ReviewForm
from hobbyswap.models import Item, Review


def contact(request):
    return render(request, 'landings/contact.html')


def careers(request):
    return render(request, 'landings/careers.html')


def home(request):
    return render(request, 'landings/home.html')


def error(request):
    return render(request, 'landings/error.html')


def about(request):
    return render(request, 'about.html')


def category(request):
    listings = Item.objects.all()
    data = {'listings': listings}
    return render(request, 'loops/category.html', data)



def reviews(request):
    reviews = Review.objects.all()
    data = {'reviews': reviews}
    return render(request, 'loops/reviews.html', data)


def listing(request):
    listings = Item.objects.all()
    data = {'listings': listings}
    return render(request, 'loops/listings.html', data)


def view_user(request, user_id):
    user_view = User.objects.get(id=user_id)
    data = {'user': user_view}
    return render(request, 'loops/view_user.html', data)


def view_listing(request, item_id):
    item = Item.objects.get(id=item_id)
    data = {"item": item}
    return render(request, "loops/view_listing.html", data)

@login_required
def user(request):
    if not request.user.is_authenticated():
        return redirect("login")
    return render(request, 'landings/user.html', {
        'request': request
    })

@login_required
def thanks(request):
    return render(request, 'landings/thanks.html', {})

@login_required
def profile(request):
    if not request.user.is_authenticated():
        return redirect("login")
    return render(request, 'landings/user.html', {
        'request': request
    })

@login_required
def edit_profile(request, user_id):
    profile_user = User.objects.get(id=user_id)
    if request.user == profile_user:
        if request.method == 'POST':
            form = EmailUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("profile")
        else:
            form = EmailUserCreationForm()
        return render(request, "registration/register.html", {
        'form': form, "user": profile_user})

    else:
        return redirect("home")
# initial={"username": user, 'first_name': user, 'last_name': user, "email": user })


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)

        if form.is_valid():
            reg_user = form.save()

            text_content = 'Thank you for signing up for our website, {}'.format(reg_user.username)

            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our ' \
                           'site</div>'.format(reg_user.first_name, reg_user.last_name)

            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [reg_user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("home")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def post_item(request):
    if request.method == "POST":
        form = PostItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.cleaned_data['item']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            deposit = form.cleaned_data['deposit']
            description = form.cleaned_data['description']
            condition = form.cleaned_data['condition']
            beg_availability = form.cleaned_data['beg_availability']
            end_availability = form.cleaned_data['end_availability']
            image = form.cleaned_data['image']
            post_user = request.user
            items = Item.objects.create(item=item, price=price, deposit=deposit, description=description,
                                        condition=condition, beg_availability=beg_availability,
                                        end_availability=end_availability, post_user=post_user,
                                        image=image, category=category)
            text_content = 'Thank you for posting a {} for rent on HobbySwap'.format(items.item)
            html_content = '<h2> Please make sure all the information you provided is correct<h2><p> Description ' \
                           '{}</p><p>Availability {} to {}</p><p>Condition {}</p>'.format(items.description,
                                                                                          items.beg_availability,
                                                                                          items.end_availability,
                                                                                          items.condition)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [items.post_user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("thanks")
    else:
        form = PostItemForm()

    items = Item.objects.all()
    data = {"form": form, "items": items}
    return render(request, "forms/post.html", data)

@login_required
def edit_post(request, item_id):
    item = Item.objects.get(id=item_id)
    if item.post_user == request.user:
        if request.method == "POST":
            form = PostItemForm(request.POST, request.FILES)
            if form.is_valid():
                item.item = form.cleaned_data['item']
                item.category = form.cleaned_data['category']
                item.price = form.cleaned_data['price']
                item.deposit = form.cleaned_data['deposit']
                item.description = form.cleaned_data['description']
                item.condition = form.cleaned_data['condition']
                item.beg_availability = form.cleaned_data['beg_availability']
                item.end_availability = form.cleaned_data['end_availability']
                item.image = form.cleaned_data['image']
                item.save()
                return redirect("/view_listing/{}".format(item_id))
        else:
            form = PostItemForm(initial={'item': item, 'category': item, 'price': item.price, 'condition': item, 'deposit':
                                         item.deposit, 'description': item, 'end_availability': item.end_availability,
                                         'beg_availability': item.beg_availability, 'image': item.image })
        data = {"form": form, "item": item}
        return render(request, "forms/edit_post.html", data)
    else:
        return redirect("error")

@login_required
def review(request):
    reviews = Review.objects.all()
    data = {'reviews': reviews}
    return render(request, 'loops/reviews.html', data)

@login_required
def view_review(request, item_id):
    reviews = Review.objects.get(id=item_id)
    data = {'reviews': reviews}
    return render(request, 'loops/view_reviews.html', data)


@login_required
def create_review(request, item_id):
    item = Item.objects.get(id=item_id)
    # user = User.objects.get(id=user_id)
    if item.post_user != request.user:
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                text = form.cleaned_data['text']
                review = Review.objects.create(subject=subject, text=text, user=request.user, item=item)
                text_content = 'Thank you for posting a review of {} on HobbySwap'.format(review.item)
                html_content = 'Thank you for posting a review of {} on HobbySwap'.format(review.item)
                msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [review.user.email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                return redirect('home')
        else:
            form = ReviewForm(initial={'item': item.item})
        data = {"form": form , 'item': item}
        return render(request, "forms/review_item.html", data)

    else:
        return redirect('error')


@login_required
def edit_review(request, item_id, user_id):
    item = Item.objects.get(id=item_id)
    review = item.reviewed_item.filter()
    user = User.objects.get(id=user_id)
    # edit_reviews = Review.objects.get(id=review_id)
    if review.user == request.user:
        if request.method == "POST":
            form = PostItemForm(request.POST, request.FILES)
            if form.is_valid():
                Review.subject = form.cleaned_data['subject']
                Review.text= form.cleaned_data['text']
                review.save()
                return redirect("/view_review/{}".format(item_id))
        else:
            form = PostItemForm(initial={"subject": review, "text": review})
        data = {"form": form, "review": review}
        return render(request, "forms/edit_review.html", data)
    else:
        return redirect("error")


