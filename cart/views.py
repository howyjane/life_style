from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from catalog.models import Course, CoursePass
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.

# def view_cart(request):
#     cart = request.session.get('shopping_cart', {})
#     subtotal = 0
#     total = 0
    
#     # Calculate and display total price
#     for course,cart_item in cart.items():
#         cart[course]['subtotal'] = cart[course]['quantity']
#         total = total + cart[course]['subtotal']
    
#     return render(request, 'cart/view_cart.template.html', {
#         'shopping_cart':cart,
#         'subtotal':subtotal,
#         'total':total
#     })



def add_to_cart(request, course_id):
    
    # get the object specified by the key 'shopping_cart', if not found, return an empty dictionary
    cart = request.session.get('shopping_cart', {})
    
    # Add the products specified by the products_id argument to cart
    course = get_object_or_404(Course, pk=course_id)
    if course_id not in cart:
        
        cart[course_id] = {
            'id':course_id,
            'title': course.title,
            'cost': course.cost,
            'quantity':1,
           
       
        }
        
        # save the cart back to the session under the key 'shopping_cart'
        request.session['shopping_cart'] = cart
        
        messages.success(request, 'Product successfully added to your cart!')
        return redirect('show_courses')
    else:
        
        request.session['shopping_cart'] = cart
        
        messages.success(request, "Course is already added to your cart!")
        return redirect('show_courses')
        
        cart[course_id]['quantity']+=1
        request.session['shopping_cart'] = cart
        return redirect('show_courses')
    

def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    subtotal = 0.00
    total = 6.00
    # new_total = 0.00
    
    # Total Price for each item added to cart
    for course,cart_item in cart.items():
        cart[course]['subtotal'] = cart[course]['quantity']*cart[course]['cost']
        total = total + cart[course]['subtotal']
    
    # for course,cart_item in cart.items.all():
    #     new_total += [course.cost]
    
    # cart.total = new_total
        
    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart':cart,
        'subtotal':subtotal,
        'total':total
    })


# @login_required
# def view_cart(request):
#     cart = request.session.get('shopping_cart', {})

#     return render(request, 'cart/view_cart.template.html', {
#         'shopping_cart':cart

      
#     })

# @login_required
# def add_to_cart(request, course_id):
#     # attempt to get existing cart from the session using the key "shopping_cart"
#     # the second argument will be the default value if 
#     # if the key does not exist in the session
#     cart = request.session.get('shopping_cart', {})
    

#     # we check if the course_id is not in the cart. If so, we will add it
#     if course_id not in cart:
#         course = get_object_or_404(Course, pk=course_id)
#         # course is found, let's add it to the cart
#         cart[course_id] = {
#             'id':course_id,
#             'title': course.title,
#             'cost': course.cost,
#             'quantity': 1,
            
#         }
        

#         # save the cart back to sessions
#         request.session['shopping_cart'] = cart
        
#         messages.success(request, "Course is added to your cart!")
#         return redirect('show_courses')
#     else:
        
#         request.session['shopping_cart'] = cart
        
#         messages.success(request, "Course is already added to your cart!")
#         return redirect('show_courses')
        


# @login_required
# def add_to_cart(request, course_id):
    
#     # get the object specified by the key 'shopping_cart', if not found, return an empty dictionary
#     cart = request.session.get('shopping_cart', {})
    
#     # Add the products specified by the products_id argument to cart
    
#     if course_id not in cart:
#         course = get_object_or_404(Course, pk=course_id)
    
#         cart[course_id] = {
#             'id':course_id,
#             'title': course.title,
#             'cost': course.cost,
#             'quantity': course.quantity,
#             'image_url':course.image.cdn_url
#         }
        
#         # save the cart back to the session under the key 'shopping_cart'
#         request.session['shopping_cart'] = cart
        
#         messages.success(request, 'Product successfully added to your cart!')
#         return redirect('show_courses')
#     else:
#         cart[course_id]['quantity']+= 1
#         request.session['shopping_cart'] = cart
#         return redirect('show_courses')
        
        
# @login_required
# def add_quantity(request, course_id):
#     # attempt to get existing cart from the session using the key "shopping_cart"
#     # the second argument will be the default value if 
#     # if the key does not exist in the session
#     cart = request.session.get('shopping_cart', {})

#     # we check if the course_id is not in the cart. If so, we will add it

#     course = get_object_or_404(Course, pk=course_id)
#         # course is found, let's add it to the cart
        
#     cart[course]['quantity']+=1

#         # save the cart back to sessions
#     request.session['shopping_cart'] = cart

#     return redirect('view_cart')

def add_quantity(request, course_id):
    
    # get the object specified by the key 'shopping_cart', if not found, return an empty dictionary
    cart = request.session.get('shopping_cart', {})
    
    # Add the products specified by the products_id argument to cart
    course = get_object_or_404(Course, pk=course_id)

    cart[course_id]['quantity']+=1
    request.session['shopping_cart'] = cart
    return redirect('view_cart')


def minus_quantity(request, course_id):
    
    # get the object specified by the key 'shopping_cart', if not found, return an empty dictionary
    cart = request.session.get('shopping_cart', {})
    
    # Add the products specified by the products_id argument to cart
    course = get_object_or_404(Course, pk=course_id)
    
    # check and prevent the quantity drop less than 1
    if cart[course_id]['quantity'] > 1:
        cart[course_id]['quantity']-=1
    
    request.session['shopping_cart'] = cart
    return redirect('view_cart')

@login_required
def remove_from_cart(request, course_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the course is in the cart
    if course_id in cart:
        # remove it from the cart
        del cart[course_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")
        
    return redirect('view_cart')



