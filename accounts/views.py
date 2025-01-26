from django.shortcuts import render, redirect, HttpResponse
from .forms import registrationsform
from .models import User
from django.contrib import auth, messages
from django.contrib.auth import login, logout, authenticate

# User Account verification
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from carts.models import Cart, CartItem
from carts.views import _cart_id
import requests

#  Create your views here.
def register(request):
    if request.method == 'POST':
        form = registrationsform(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            phone_number = form.cleaned_data['phone_number']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
            user.phone_number = phone_number
            user.is_active = True
            user.save()
            # current_site = get_current_site(request)
            # mail_subject = "Please activate your account"
            # message = render_to_string("accounts/verification_email.html", {
            #     "user": user,
            #     "domain": current_site,
            #     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            #     "token": default_token_generator.make_token(user)
            # })
            # to_email = email
            # msg = EmailMessage(mail_subject, message, to=[to_email])
            # msg.send()
            # # messages.success(request, "Thank you for registring with us")
            # return redirect("/account/login/?command=verification&email="+email)
            return redirect('accounts/login.html')
    else:
        form = registrationsform()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    for i in cart_item:
                        i.user = user
                        i.save()
            except Cart.DoesNotExist:
                cart = Cart.objects.create(cart_id=_cart_id(request))

            auth.login(request, user)
            messages.success(request, "You are now logged in")
            url = request.META.get("HTTP_REFERER")
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split("=") for x in query.split("&"))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
                
            except:
                return redirect('category:category_view')
        else:
            messages.error(request, "Invalide login credentials")

    return render(request, 'accounts/login.html')

# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User._default_manager.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, "Congratulations! Your account is activated")
#         return redirect("account:login")
#     else:
#         messages.error(request, "Invalide activation")
#         return redirect("account:register")


def logout(request):
    auth.logout(request)
    messages.success(request, "you're logged out")
    return redirect('/')

# def forgotPassword(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         if User.objects.filter(email=email).exists():
#             user = User.objects.get(email__exact=email)
#             current_site = get_current_site(request)
#             mail_subject = "Please Reset Your Password"
#             message = render_to_string("accounts/forgot_activate_email.html", {
#                 "user": user,
#                 "domain": current_site,
#                 "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                 "token": default_token_generator.make_token(user)
#             })
#             to_email = email
#             msg = EmailMessage(mail_subject, message, to=[to_email])
#             msg.send()
#             messages.success(request, "Password reset email has been sent to your email address")
#             return redirect("account:login")
#         else:
#             messages.error(request, "account doesn't exist")
#             return redirect("account:forgotPassword")
#     return render(request, "accounts/forgotPassword.html")

# def password_validate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User._default_manager.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and default_token_generator.check_token(user, token):
#         request.session['uid'] = uid
#         messages.success(request, "Please reset your password")
#         return redirect("account:resetPassword")
#     else:
#         messages.error(request, "This link has been expired")
#         return redirect("account:login")

# def resetPassword(request):
#     if request.method == 'POST':
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         if password == confirm_password:
#             uid = request.session.get('uid')
#             user = User.objects.get(pk=uid)
#             user.set_password(password)
#             user.save()
#             messages.success(request, "password reseted successfuly")
#             return redirect("account:login")
#         else:
#             messages.error(request, "Password do not match")
#             return redirect("account:resetPassword")
#     else:
#         return render(request, "accounts/reset_Password.html")