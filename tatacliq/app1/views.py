from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Wishlist,Category
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def Men_view(request):
    return render(request, 'app1/Men.html')

def Women_view(request):
    return render(request,'app1/women.html')

def KIDS_view(request):
    return render(request,'app1/kids.html')

def HOMENAVBAR_view(request):
    return render(request,'app1/Homenavbar.html')

def BEAUTY_view(request):
    return render(request,'app1/beauty.html')

def GENZ_view(request):
    return render(request,'app1/genz.html')

def STUDIO_view(request):
    return render(request,'app1/studio.html')





#drop down views ke liya function  MAN

def T_Shirts_view(request):
    return render(request,'app1/tshirt.html')

def Cusual_Shirts_view(request):
    return render(request,'app1/Cusual_Shirts.html')

def Formal_Shirts_view(request):
    return render(request,'app1/Formal_Shirts.html')

def Sweatshirts_view(request):
    return render(request,'app1/Sweatshirts.html')

def Sweaters_view(request):
    return render(request,'app1/Sweaters.html')

def Jackets_view(request):
    return render(request,'app1/Jackets.html')

def Blazers_Coats_view(request):
    return render(request,'app1/Blazers_Coats.html')

def Suits_view(request):
    return render(request,'app1/Suits.html')

def Rain_Jackets_view(request):
    return render(request,'app1/Rain_Jackets.html')

def Kurtas_Kurta_Sets_view(request):
    return render(request,'app1/Kurtas_Kurta_Sets.html')

def Sherwanis_view(request):
    return render(request,'app1/Sherwanis.html')

def Nehru_Jackets_view(request):
    return render(request,'app1/Nehru_Jackets.html')

def Dhotis_view(request):
    return render(request,'app1/Dhotis.html')

def Wallets_view(request):
    return render(request,'app1/Wallets.html')

def Belts_view(request):
    return render(request,'app1/Belts.html')

def Perfumes_Body_Mists_view(request):
    return render(request,'app1/Perfumes_Body_Mists.html')

def Trimmers_view(request):
    return render(request,'app1/Trimmers.html')

def Deodorants_view(request):
    return render(request,'app1/Deodorants.html')

def Ties_Cufflinks_Pocket_Squares_view(request):
    return render(request,'app1/Ties_Cufflinks_Pocket_Squares.html')

def Accessory_Gift_Sets_view(request):
    return render(request,'app1/Accessory_Gift_Sets.html')

def Caps_Hats_view(request):
    return render(request,'app1/Caps_Hats.html')

def Mufflers_Scarves_Gloves_view(request):
    return render(request,'app1/Mufflers_Scarves_Gloves.html')

def Phone_Cases_view(request):
    return render(request,'app1/Phone_Cases.html')

def Rings_Wristwear_view(request):
    return render(request,'app1/Rings_Wristwear.html')

def Helmets_view(request):
    return render(request,'app1/Helmets.html')

def Jeans_view(request):
    return render(request,'app1/Jeans.html')

def Casual_Trousers_view(request):
    return render(request,'app1/Casual_Trousers.html')

def Formal_Trousers_view(request):
    return render(request,'app1/Formal_Trousers.html')

def Shorts_view(request):
    return render(request,'app1/Shorts.html')

def Track_Pants_Joggers_view(request):
    return render(request,'app1/Track_Pants_Joggers.html')

def Briefs_Trunks_view(request):
    return render(request,'app1/Briefs_Trunks.html')

def Boxers_view(request):
    return render(request,'app1/Boxers.html')

def Vests_view(request):
    return render(request,'app1/Vests.html')

def Sleepwear_Loungewear(request):
    return render(request,'app1/Sleepwear_Loungewear.html')

def Thermals_view(request):
    return render(request,'app1/Thermals.html')


def Casual_Shoes_view(request):
    return render(request,'app1/Casual_Shoes.html')

def Formal_Shoes_view(request):
    return render(request,'app1/Formal_Shoes.html')

def Sneakers_view(request):
    return render(request,'app1/Sneakers.html')

def Sandals_Floaters_view(request):
    return render(request,'app1/Sandals_Floaters.html')

def Flip_Flops_view(request):
    return render(request,'app1/Flip_Flops.html')

def Socks_view(request):
    return render(request,'app1/Socks.html')

def Sports_Shoes_view(request):
    return render(request,'app1/Sports_Shoes.html')

def Active_T_Shirts_view(request):
    return render(request,'app1/Active_T_Shirts.html')

def Track_Pants_Shorts_view(request):
    return render(request,'app1/Track_Pants_Shorts.html')

def Tracksuits_view(request):
    return render(request,'app1/Tracksuits.html')

def Jackets_Sweatshirts_view(request):
    return render(request,'app1/Jackets_Sweatshirts.html')

def Sports_Accessories_view(request):
    return render(request,'app1/Sports_Accessories.html')

def Swimwear_view(request):
    return render(request,'app1/Swimwear.html')

def Fitness_Gadgets_view(request):
    return render(request,'app1/Fitness_Gadgets.html')


def Headphones_view(request):
    return render(request,'app1/Headphones.html')

def Speakers_view(request):
    return render(request,'app1/Speakers.html')

def Smart_Wearables_view(request):
    return render(request,'app1/Smart_Wearables.html')


#women
def Kurtas_Suits_view(request):
    return render(request,'app1/Kurtas_Suits.html')

def Kurtis_Tunics_Tops_view(request):
    return render(request,'app1/Kurtis_Tunics_Tops.html')

def Ethnic_Wear_women_view(request):
    return render(request,'app1/Ethnic_women_Wear.html')

def Leggings_Salwars_Churidars_view(request):
    return render(request,'app1/Leggings_Salwars_Churidars.html')

def Sarees_view(request):
    return render(request,'app1/Sarees.html')

def Skirts_Palazzos_view(request):
    return render(request,'app1/Skirts_Palazzos.html')

def Dress_Materials_view(request):
    return render(request,'app1/Dress_Materials.html')

def Lehenga_Cholis_view(request):
    return render(request,'app1/Lehenga_Cholis.html')

def Dupattas_Shawls_view(request):
    return render(request,'app1/Dupattas_Shawls.html')

def Jackets_women_view(request):
    return render(request,'app1/Jackets_women.html')


def Jeans_women_view(request):
    return render(request,'app1/Jeans_women.html')

def Trousers_Capris_view(request):
    return render(request,'app1/Trousers_Capris.html')


def Shorts_Skirts_women_view(request):
    return render(request,'app1/Shorts_Skirts_women.html')

def Co_ords_women_view(request):
    return render(request,'app1/Co_ords_women.html')

def Playsuits_women_view(request):
    return render(request,'app1/Playsuits_women.html')

def Jumpsuits_women_view(request):
    return render(request,'app1/Jumpsuits_women.html')

def Shrugs_view(request):
    return render(request,'app1/Shrugs.html')

def Sweaters_Sweatshirts_women_view(request):
    return render(request,'app1/Sweaters_Sweatshirts_women.html')

def Jackets_Coats_women_view(request):
    return render(request,'app1/Jackets_Coats_women.html')

def Blazers_Waistcoats_view(request):
    return render(request,'app1/Blazers_Waistcoats.html')


def Flats_view(request):
    return render(request,'app1/Flats.html')

def Casual_Shoes_women_view(request):
    return render(request,'app1/Casual_Shoes_women.html')

def Heels_view(request):
    return render(request,'app1/Heels.html')

def Boots_view(request):
    return render(request,'app1/Boots.html')

def Sports_Shoes_Floaters_view(request):
    return render(request,'app1/Sports_Shoes_Floaters.html')


def Clothing_view(request):
    return render(request,'app1/Clothing.html')

def Footwear_view(request):
    return render(request,'app1/Footwear.html')

def Sports_Accessories_women_view(request):
    return render(request,'app1/Sports_Accessories_women.html')


def Sports_Equipment_view(request):
    return render(request,'app1/Sports_Equipment.html')


def Bra_view(request):
    return render(request,'app1/Bra.html')

def Briefs_view(request):
    return render(request,'app1/Briefs.html')

def Shapewear_view(request):
    return render(request,'app1/Shapewear.html')


def Sleepwear_Loungeweart_women_view(request):
    return render(request,'app1/Sleepwear_Loungewear_women.html')

def Swimwear_women_view(request):
    return render(request,'app1/Swimwear_women.html')


def Camisoles_Thermals_view(request):
    return render(request,'app1/Camisoles_Thermals.html')


def Makeup_view(request):
    return render(request,'app1/Makeup.html')


def Skincare_view(request):
    return render(request,'app1/Skincare.html')



#kids  

def T_Shirts_kids_view(request):
    return render(request,'app1/T_Shirts_kids.html')

def Shirts_kids_view(request):
    return render(request,'app1/Shirts_kids.html')

def Shorts_view(request):
    return render(request,'app1/Shorts_kids.html')

def Jeans_kids_view(request):
    return render(request,'app1/Jeans_kids.html')

def Trousers_kids_view(request):
    return render(request,'app1/Trousers_kids.html')

def Clothing_Sets_kids_view(request):
    return render(request,'app1/Clothing_Sets_kids.html')

def Ethnic_Wear_kids_view(request):
    return render(request,'app1/Ethnic_Wear_kids.html')


def Track_Pants_Pyjamas_kids_view(request):
    return render(request,'app1/Track_Pants_Pyjamas_kids.html')

def Jacket_Sweater_Sweatshirts_kids_view(request):
    return render(request,'app1/Jacket_Sweater_Sweatshirts_kids.html')


def Party_Wear_kids_view(request):
    return render(request,'app1/Party_Wear_kids.html')

def Innerwear_Thermals_kids_view(request):
    return render(request,'app1/Innerwear_Thermals_kids.html')


def Nightwear_Loungewear_kids_view(request):
    return render(request,'app1/Nightwear_Loungewear_kids.html')


def Value_Pack_kids_view(request):
    return render(request,'app1/Value_Pack_kids.html')

def Dresses_kids_view(request):
    return render(request,'app1/Dresses_kids.html')

def Tops_kids_view(request):
    return render(request,'app1/Tops_kids.html')

def Tshirts_kids_view(request):
    return render(request,'app1/Tshirts_kids.html')

def Jeans_kids_view(request):
    return render(request,'app1/Jeans_kids.html')

def Trousers_Capris_kids_view(request):
    return render(request,'app1/Trousers_Capris_kids.html')


def Shorts_Skirts_kids_view(request):
    return render(request,'app1/Shorts_Skirts_kids.html')

def Co_ords_kids_view(request):
    return render(request,'app1/Co_ords_kids.html')

def Playsuits_kids_view(request):
    return render(request,'app1/Playsuits_kids.html')


def Jumpsuits_kids_view(request):
    return render(request,'app1/Jumpsuits_kids.html')


def Shrugs_kids_view(request):
    return render(request,'app1/Shrugs_kids.html')


def Sweaters_Sweatshirts_kids_view(request):
    return render(request,'app1/Sweaters_Sweatshirts_kids.html')


def Jackets_Coats_kids_view(request):
    return render(request,'app1/Jackets_Coats_kids.html')


def Blazers_Waistcoats_kids_view(request):
    return render(request,'app1/Blazers_Waistcoats_kids.html')

def Casual_Shoes_kids_view(request):
    return render(request,'app1/Casual_Shoes_kids.html')

def Flipflops_kids_view(request):
    return render(request,'app1/Flipflops_kids.html')


def Sports_Shoes_kids_view(request):
    return render(request,'app1/Sports_Shoes_kids.html')




#Home

def Bed_Runners_home_view(request):
    return render(request,'app1/Bed_Runners_home.html')


def Mattress_Protectors_home_view(request):
    return render(request,'app1/Mattress_Protectors_home.html')

def Bedsheets_home_view(request):
    return render(request,'app1/Bedsheets_home.html')

def Bath_Towels_home_view(request):
    return render(request,'app1/Bath_Towels_home.html')

def  Hand_Face_Towels_home_view(request):
    return render(request,'app1/Hand_Face_Towels_home.html')



def Plants_Planters_home_view(request):
    return render(request,'app1/Plants_Planters_home.html')

def Aromas_Candles_home_view(request):
    return render(request,'app1/Aromas_Candles_home.html')

def  Mirrors_home_view(request):
    return render(request,'app1/Mirrors_home.html')




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserSignupForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserSignupForm
from .models import UserProfile



def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']

            # Assign role to user profile
            user.userprofile.role = role
            user.userprofile.save()

            login(request, user)

            if role == 'admin':
                return redirect('admin')
            elif role == 'seller':
                return redirect('seller_page')
            else:
                return redirect('customer_dashboard')
    else:
        form = UserSignupForm()

    return render(request, 'app1/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Superuser check for admin
            if user.is_superuser:
                return redirect('/admin/')

            try:
                role = user.userprofile.role
            except UserProfile.DoesNotExist:
                role = None

            if role == 'seller':
                return redirect('seller_page')
            else:
                return redirect('home')
        else:
            return render(request, 'app1/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'app1/login.html')



@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('login')

def myorders_view(request):
    return render(request,'app1/myorder.html')



from django.contrib.auth.decorators import login_required



#imp
@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'app1/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('wishlist')

from django.shortcuts import render, redirect
from .models import Product, Cart, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'app1/products.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)
    product_id_str = str(product_id)  # force key to string
    
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id_str, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id_str))
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total,
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'app1/mybag.html', context)

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            del cart[str(product_id)]
        request.session['cart'] = cart

    return redirect('view_cart')




from .models import Profile
from .forms import ProfileForm


@login_required
def profile_view(request):
    # Get the user's profile or create one if it doesn't exist
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'app1/myprofile.html', {'profile': profile, 'form': form})



@login_required
def checkout_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id_str, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id_str))
        subtotal = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })
        total_price += subtotal

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }

    return render(request, 'app1/checkout.html', context)

from django.http import JsonResponse

def complete_checkout(request):
    # Perform the order completion logic (payment, order creation)
    return redirect('order_success')

from django.http import JsonResponse

def get_cart_summary(request):
    # Assuming you have a cart in session
    cart_items = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart_items.values())
    cart_items_count = len(cart_items)
    
    return JsonResponse({
        'cart_items_count': cart_items_count,
        'total_price': total_price,
    })

def order_success(request):
    # Logic to display order success, for example, thank you message or order details
    return render(request, 'app1/order_success.html')



from .forms import ProductForm

from .models import Category, Product

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            category=category,
            image=image
        )

        return redirect('product_list') 
    else:
        categories = Category.objects.all()
        return render(request, 'app1/add_product.html', {'categories': categories})
    


@login_required
def seller_dashboard(request):
    return render(request, 'app1/seller_dashboard.html')

def customer_dashboard(request):
    return render(request, 'app1/home.html')


@login_required
def admin_dashboard(request):
    return render(request, 'app1/admin_dashboard.html')

def dashboard_view(request):
    return render(request, 'app1/home.html')


@login_required
def seller_page(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        stock = request.POST['stock']
        category_id = request.POST['category']
        image = request.FILES['image']
        
        category = Category.objects.get(id=category_id)
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            category=category,
            image=image
        )
        return redirect('seller_page')  # Replace with your URL name
    return render(request, 'app1/seller_page.html', {'categories': categories})
from django.http import HttpResponseForbidden


@login_required
def admin_page(request):
    # Check if the logged-in user is an admin
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to view this page.")
    
    return render(request, 'app1/admin_page.html')