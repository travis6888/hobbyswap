
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import render, redirect
# Create your views here.
from hobby import settings
from hobbyswap.forms import EmailUserCreationForm, PostItemForm, SelectItemForm
from hobbyswap.models import Item


def contact(request):
    return render(request, 'contact.html')

def careers(request):
    return render(request, 'careers.html')

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def category(request):
    listing = Item.objects.all()
    data = {'listing': listing}
    return render(request, 'category.html', data)

def listing(request):
    listings = Item.objects.all()
    data = {'listings': listings}
    return render(request, 'listings.html', data)


def view_listing(request, item_id):
    item = Item.objects.get(id=item_id)
    data = {"item": item}
    return render(request, "view_listing.html", data)

@login_required
def select_listing(request, item_id):
    item = Item.objects.get(id=item_id)
    user = User.objects.all()
    if request.method == "POST":
        form = SelectItemForm(request.post)
        if form.is_valid():
            item = form.cleaned_data['item']
            post_user = form.cleaned_data['post_user']
            renter = request.user
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            beg_date = form.cleaned_data['beg_date']
            end_date = form.cleaned_data['end_date']
            price = form.cleaned_data['price']
            deposit = form.cleaned_data['deposit']
            to_email = item.post_user.email
            select = form.save()
            text_content = 'Thank you for signing up for our website, {}'.format(select.username)

            html_content = '<h2>Thanks {} {} {}{}{}{}{}{}for signing up!</h2> <div>I hope you enjoy using our ' \
                           'site</div>'.format(select.post_user, select.last_name)

            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [userl.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        return render(request, 'home.html')
    else:
            form = SelectItemForm(initial={'item': item, 'post_user': item, 'price': item.price, 'renter': item, 'deposit':
                                         item.deposit,  'end_date': item.end_availability, 'email': item.post_user.email})
    data = {"form": form, "item": item}
    return render(request, "select_listing.html", data)



@login_required
def user(request):
    if not request.user.is_authenticated():
        return redirect("login")
    return render(request, 'user.html', {
        'request': request
    })

@login_required
def thanks(request):
    return render(request, 'thanks.html', {})

@login_required
def profile(request):
    return render(request, 'profile.html', {})


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)

        if form.is_valid():
            userl  = form.save()

            text_content = 'Thank you for signing up for our website, {}'.format(userl.username)

            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our ' \
                           'site</div>'.format(userl.first_name, userl.last_name)

            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [userl.email])
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
            return redirect("view_listing")
    else:
        form = PostItemForm()

    items = Item.objects.all()
    data = {"form": form, "items": items}
    return render(request, "post.html", data)

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
        return render(request, "edit_post.html", data)
    else:
        return redirect("error")