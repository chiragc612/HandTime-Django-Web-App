from itertools import product
from django.urls import path
from .views import about, addToCarts, addToWishlists, addproducts, callback, carts, changeQty, changepassword, contact, deleteproducts, details, editproducts, forgotpassword, index, initiate_payment, logout, newpassword, products, remove, removeFromCart, signin, signup, testimonial, verify, viewproducts, wishlists

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('products/', products, name="products"),
    path('testimonial/', testimonial, name="testimonial"),
    path('contact/', contact, name="contact"),
	path('signup/', signup, name="signup"),
	path('signin/', signin, name="signin"),
	path('forgotpassword/', forgotpassword, name="forgotpassword"),
	path('verify/', verify, name="verify"),
	path('newpassword/', newpassword, name="newpassword"),
	path('logout/', logout, name="logout"),
	path('changepassword/', changepassword, name="changepassword"),
	path('addproducts/', addproducts, name="addproducts"),
	path('viewproducts/', viewproducts, name="viewproducts"),
	path('editproducts/<int:pk>', editproducts, name="editproducts"),
	path('deleteproducts/<int:pk>', deleteproducts, name="deleteproducts"),
	path('details/<int:pk>',details,name="details"),
	path('addToWishlists/<int:pk>',addToWishlists, name="addToWishlists"),
	path('addToCarts/<int:pk>',addToCarts, name="addToCarts"),
	path('wishlists/',wishlists,name="wishlists"),
	path('carts/',carts,name="carts"),
	path('remove/<int:pk>',remove,name="remove"),
	path('removeFromCart/<int:pk>',removeFromCart,name="removeFromCart"),
	path('changeQty/',changeQty,name="changeQty"),
	path('pay/', initiate_payment, name='pay'),
	path('callback/', callback, name='callback'),
]
