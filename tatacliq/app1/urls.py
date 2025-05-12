from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import product_list, add_to_cart
from .views import checkout_view

urlpatterns = [
  path('',views.home,name='home'),
  path('Men/',views.Men_view,name="Men"),
  path('Women/',views.Women_view,name="women"),
  path('Kids/',views.KIDS_view,name="kids"),
  path('Home/',views.HOMENAVBAR_view,name="homenavbar"),
  path('Beauty/',views.BEAUTY_view,name="beauty"),
  path('Genz/',views.GENZ_view,name="genz"),
  path('studio/',views.STUDIO_view,name="studio"),
  path('tshirt/',views.T_Shirts_view,name='tshirt'),
  path('cusualshirt/',views.Cusual_Shirts_view,name="cusualshirt"),
  path('Formal_Shirts/',views.Formal_Shirts_view,name="Formal_Shirts"),
  path('Sweatshirts/',views.Sweatshirts_view,name='Sweatshirts'),
  path('Sweaters/',views.Sweaters_view,name='Sweaters'),
  path('Jackets/',views.Jackets_view,name='Jackets'),
  path('Blazers_Coats',views.Blazers_Coats_view,name='Blazers_Coats'),
  path('Suits/',views.Suits_view,name='Suits'),
  path('Rain_Jackets/',views.Rain_Jackets_view,name='Rain_Jackets'),


  path('Kurtas_Kurta_Sets/',views.Kurtas_Kurta_Sets_view,name='Kurtas_Kurta_Sets'),
  path('Sherwanis/',views.Sherwanis_view,name='Sherwanis'),
  path('Nehru_Jackets/',views.Nehru_Jackets_view,name='Nehru_Jackets'),
  path('Dhotis/',views.Dhotis_view,name='Dhotis'),
  path('Wallets/',views.Wallets_view,name='Wallets'),
  path('Belts/',views.Belts_view,name='Belts'),
  path('Perfumes_Body_Mists/',views.Perfumes_Body_Mists_view,name='Perfumes_Body_Mists'),
  path('Trimmers/',views.Trimmers_view,name='Trimmers'),
  path('Deodorants/',views.Deodorants_view,name='Deodorants'),
  path('Ties_Cufflinks_Pocket_Squares/',views.Ties_Cufflinks_Pocket_Squares_view,name='Ties_Cufflinks_Pocket_Squares'),
  path('Accessory_Gift_Sets/',views.Accessory_Gift_Sets_view,name='Accessory_Gift_Sets'),
  path('Caps_Hats/',views.Caps_Hats_view,name='Caps_Hats'),
  path('Mufflers_Scarves_Gloves/',views.Mufflers_Scarves_Gloves_view,name='Mufflers_Scarves_Gloves'),
  path('Phone_Cases/',views.Phone_Cases_view,name='Phone_Cases'),
  path('Rings_Wristwear',views.Rings_Wristwear_view,name='Rings_Wristwear'),
  path('Helmets/',views.Helmets_view,name='Helmets'),
  path('Jeans/',views.Jeans_view,name='Jeans'),
  path('Casual_Trousers/',views.Casual_Trousers_view,name='Casual_Trousers'),
  path('Formal_Trousers/',views.Formal_Trousers_view,name='Formal_Trousers'),
  path('Shorts/',views.Shorts_view,name='Shorts'),
  path('Track_Pants_Joggers/',views.Track_Pants_Joggers_view,name='Track_Pants_Joggers'),
  path('Briefs_Trunks/',views.Briefs_Trunks_view,name='Briefs_Trunks'),
  path('Boxers/',views.Boxers_view,name='Boxers'),
  path('Vests',views.Vests_view,name='Vests'),
  path('Sleepwear_Loungewear/',views.Sleepwear_Loungewear,name='Sleepwear_Loungewear'),
  path('Thermals/',views.Thermals_view,name='Thermals'),
  path('Casual_Shoes/',views.Casual_Shoes_view,name='Casual_Shoes'),
  path('Formal_Shoes/',views.Formal_Shoes_view,name='Formal_Shoes'),
  path('Sneakers/',views.Sneakers_view,name='Sneakers'),
  path('Sandals_Floaters/',views.Sandals_Floaters_view,name='Sandals_Floaters'),
  path('Flip_Flops/',views.Flip_Flops_view,name='Flip_Flops'),
  path('Socks/',views.Socks_view,name='Socks'),
  path('Sports_Shoes/',views.Sports_Shoes_view,name='Sports_Shoes'),
  path('Active_T_Shirts/',views.Active_T_Shirts_view,name='Active_T_Shirts'),
  path('Track_Pants_Shorts/',views.Track_Pants_Shorts_view,name='Track_Pants_Shorts'),
  path('Tracksuits/',views.Tracksuits_view,name='Tracksuits'),
  path('Jackets_Sweatshirts/',views.Jackets_Sweatshirts_view,name='Jackets_Sweatshirts'),
  path('Sports_Accessories/',views.Sports_Accessories_view,name='Sports_Accessories'),
  path('Swimwear/',views.Swimwear_view,name='Swimwear'),
  path('Fitness_Gadgets/',views.Fitness_Gadgets_view,name='Fitness_Gadgets'),
  path('Headphones/',views.Headphones_view,name='Headphones'),
  path('Speakers',views.Speakers_view,name='Speakers'),
  path('Smart_Wearables',views.Smart_Wearables_view,name='Smart_Wearables'),
  path('Kurtas_Suits/',views.Kurtas_Suits_view,name='Kurtas_Suits'),
  path('Kurtis_Tunics_Tops/',views.Kurtis_Tunics_Tops_view,name='Kurtis_Tunics_Tops'),
  path('Ethnic_women_Wear/',views.Ethnic_Wear_women_view,name='Ethnic_women_Wear'),
  path('Leggings_Salwars_Churidars/',views.Leggings_Salwars_Churidars_view,name='Leggings_Salwars_Churidars'),
  path('Sarees.html/',views.Sarees_view,name='Sarees'),
  path('Skirts_Palazzos/',views.Skirts_Palazzos_view,name='Skirts_Palazzos'),
  path('Dress_Materials/',views.Dress_Materials_view,name='Dress_Materials'),
  path('Lehenga_Cholis/',views.Lehenga_Cholis_view,name='Lehenga_Cholis'),
  path('Dupattas_Shawls/',views.Dupattas_Shawls_view,name='Dupattas_Shawls'),
  path('Jackets_women/',views.Jackets_women_view,name='Jackets_women'),
  path('Jeans_women/',views.Jeans_women_view,name='Jeans_women'),
  path('Trousers_Capris/',views.Trousers_Capris_view,name='Trousers_Capris'),
  path('Shorts_Skirts_women/',views.Shorts_Skirts_women_view,name='Shorts_Skirts_women'),
  path('Co_ords_women/',views.Co_ords_women_view,name='Co_ords_women'),
  path('Playsuits_women/',views.Playsuits_women_view,name='Playsuits_women'),
  path('Jumpsuits_women/',views.Jumpsuits_women_view,name='Jumpsuits_women'),
  path('Shrugs/',views.Shrugs_view,name='Shrugs'),
  path('Sweaters_Sweatshirts/',views.Sweaters_Sweatshirts_women_view,name='Sweaters_Sweatshirts'),
  path('Jackets_Coats/',views.Jackets_Coats_women_view,name='Jackets_Coats'),
  path('Blazers_Waistcoats/',views.Blazers_Waistcoats_view,name='Blazers_Waistcoats'),
  path('Flats/',views.Flats_view,name='Flats'),
  path('Casual_Shoes/',views.Casual_Shoes_women_view,name='Casual_Shoes'),
  path('Heels/',views.Heels_view,name='Heels'),
  path('Boots/',views.Boots_view,name='Boots'),
  path('Sports_Shoes_Floaters/',views.Sports_Shoes_Floaters_view,name='Sports_Shoes_Floaters'),
  path('Clothing/',views.Clothing_view,name='Clothing'),
  path('Footwear/',views.Footwear_view,name='Footwear'),
  path('Sports_Accessories/',views.Sports_Accessories_women_view,name='Sports_Accessories'),
  path('Sports_Equipment/',views.Sports_Equipment_view,name='Sports_Equipment'),
  path('Bra/',views.Bra_view,name='Bra'),
  path('Briefs/',views.Briefs_view,name='Briefs'),
  path('Shapewear/',views.Shapewear_view,name='Shapewear'),
  path('Sleepwear_Loungewear/',views.Sleepwear_Loungeweart_women_view,name='Sleepwear_Loungewear'),
  path('Swimwear/',views.Swimwear_view,name='Swimwear'),
  path('Camisoles_Thermals/',views.Camisoles_Thermals_view,name='Camisoles_Thermals'),
  path('Makeup/',views.Makeup_view,name='Makeup'),
  path('Skincare/',views.Shorts_Skirts_women_view,name='Skincare'),
  path('T_Shirts_kids/',views.T_Shirts_kids_view,name='T_Shirts_kids'),
  path('Shirts_kids/',views.Shirts_kids_view,name='Shirts_kids'),
  path('Shorts_kids/',views.Shorts_Skirts_kids_view,name='Shorts_kids'),
  path('Jeans_kids/',views.Jeans_kids_view,name='Jeans_kids'),
  path('Trousers_kids/',views.Trousers_kids_view,name='Trousers_kids'),
  path('Clothing_Sets_kids/',views.Clothing_Sets_kids_view,name='Clothing_Sets_kids'),
  path('Ethnic_Wear_kids/',views.Ethnic_Wear_kids_view,name='Ethnic_Wear_kids'),
  path('Track_Pants_Pyjamas_kids/',views.Track_Pants_Pyjamas_kids_view,name='Track_Pants_Pyjamas_kids'),
  path('Jacket_Sweater_Sweatshirts_kids/',views.Jacket_Sweater_Sweatshirts_kids_view,name='Jacket_Sweater_Sweatshirts_kids'),
  path('Party_Wear_kids/',views.Party_Wear_kids_view,name='Party_Wear_kids'),
  path('Innerwear_Thermals_kids/',views.Innerwear_Thermals_kids_view,name='Innerwear_Thermals_kids'),
  path('Nightwear_Loungewear_kids/',views.Nightwear_Loungewear_kids_view,name='Nightwear_Loungewear_kids'),
  path('Value_Pack_kids/',views.Value_Pack_kids_view,name='Value_Pack_kids'),
  path('Dresses_kids/',views.Dresses_kids_view,name='Dresses_kids'),
  path('Tops_kids/',views.Tops_kids_view,name='Tops_kids'),
  path('Tshirts/',views.T_Shirts_kids_view,name='Tshirts'),
  path('Jeans_kids/',views.Jeans_kids_view,name='Jeans_kids'),
  path('Trousers_Capris_kids/',views.Trousers_Capris_kids_view,name='Trousers_Capris_kids'),
  path('Shorts_Skirts_kids/',views.Shorts_Skirts_kids_view,name='Shorts_Skirts_kids'),
  path('Co_ords_kids/',views.Co_ords_kids_view,name='Co_ords_kids'),
  path('Playsuits_kids/',views.Playsuits_kids_view,name='Playsuits_kids'),
  path('Jumpsuits_kids/',views.Jumpsuits_kids_view,name='Jumpsuits_kids'),
  path('Shrugs_kids/',views.Shrugs_view,name='Shrugs_kids'),
  path('Sweaters_Sweatshirts/',views.Sweaters_Sweatshirts_kids_view,name='Sweaters_Sweatshirts'),
  path('Jackets_Coats_kids/',views.Jackets_Coats_kids_view,name='Jackets_Coats_kids'),
  path('Blazers_Waistcoats_kids/',views.Blazers_Waistcoats_kids_view,name='Blazers_Waistcoats_kids'),
  path('Casual_Shoes_kids/',views.Casual_Shoes_kids_view,name='Casual_Shoes_kids'),
  path('Flipflops_kids/',views.Flipflops_kids_view,name='Flipflops_kids'),
  path('Sports_Shoes_kids/',views.Sports_Shoes_kids_view,name='Sports_Shoes_kids'),
  path('Bed_Runners_home/',views.Bed_Runners_home_view,name='Bed_Runners_home'),
  path('Mattress_Protectors_home/',views.Mattress_Protectors_home_view,name='Mattress_Protectors_home'),
  path('Bedsheets_home/',views.Bedsheets_home_view,name='Bedsheets_home'),
  path('Bath_Towels_home/',views.Bath_Towels_home_view,name='Bath_Towels_home'),
  path('Hand_Face_Towels_home/',views.Hand_Face_Towels_home_view,name='Hand_Face_Towels_home'),
  path('Plants_Planters_home/',views.Plants_Planters_home_view,name='Plants_Planters_home'),
  path('Aromas_Candles_home/',views.Aromas_Candles_home_view,name='Aromas_Candles_home'),
  path('Mirrors_home/',views.Mirrors_home_view,name='Mirrors_home'),


 path('login/', views.login_view, name='login'),
 path('logout/',views.logout_view,name='logout'),
 path('signup/',views.signup_view,name='signup'),
 path('myorders/',views.myorders_view,name='myorders'),



  path('wishlist/', views.wishlist_view, name='wishlist'),
  path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
  path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
 

  

    

  #cart

   path('products/', product_list, name='product_list'),
   path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   path('cart/', views.view_cart, name='view_cart'),
   path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),


#profile

 path('profile/', views.profile_view, name='profile'),


#checkout
  path('checkout/', checkout_view, name='checkout'), 
  path('checkout/', views.checkout_view, name='checkout'),
  path('complete_checkout/', views.complete_checkout, name='complete_checkout'), 
  path('order_success/', views.order_success, name='order_success'),
  path('get_cart_summary/', views.get_cart_summary, name='get_cart_summary'),


path('add-product/', views.add_product, name='add_product'),

   path('dashboard/', views.dashboard_view, name='dashboard'),


    path('seller/',views.seller_page, name='seller_page'),
path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
 path('admin-page/', views.admin_page, name='admin_page'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)