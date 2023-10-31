from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from flowerAPI.firebase_client import FirebaseClient
from django.contrib.auth.decorators import login_required



@login_required
def home(request):      #Not used
    
    return redirect("inventory")




#\\--------------------------------Signup---------------------------------\\




def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Account sucessfully created")

        return redirect("signin")
    

    return render(request, "authentication/signup.html")


#\\---------------------------------------Signup End------------------------------------\\







#\\---------------------------------------Signin------------------------------------\\



def signin(request):

    if request.method == "POST":

        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            
            return redirect("inventory")

        else:
            messages.error(request, "Incorrect Credentiials")
            return redirect('signin')
    
    
    return render(request, "authentication/signin.html")


#\\---------------------------------------Signin END------------------------------------\\






#\\---------------------------------------Sign Out------------------------------------\\



def signout(request):
    return render(request, "authentication/signout.html")





#\\---------------------------------------Sign Out END------------------------------------\\



#\\---------------------------------------Type------------------------------------\\

@login_required
def TypeList(request):

    types = type.objects.all()

    context = {
        "type" : types
    }

    return render(request, "modules/type.html", context)

@login_required
def add_type(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('type')  
    else:
        form = TypeForm()

    return render(request, 'modules/add_type.html', {'form': form})

@login_required
def update_type(request, type_id):
    types = get_object_or_404(type, pk=type_id)
     

    if request.method == 'POST':
        form = TypeForm(request.POST, instance=types)
        if form.is_valid():
            form.save()

            return redirect('type')  
    else:
        form = TypeForm(instance=types)
    
    return render(request, 'modules/update_type.html', {'form': form, 'type': types})


@login_required
def delete_type(request, type_id):
   
    types = get_object_or_404(type, id=type_id)
    
    # Check if the HTTP request method is POST (indicating the delete action)
    if request.method == 'POST':
     
        types.delete()
               
        return redirect('type')  
    
    return redirect('type')






#\\---------------------------------------Type END------------------------------------\\




#\\---------------------------------------Color------------------------------------\\



@login_required
def ColorList(request):

    colors = color.objects.all()

    context = {
        "color" : colors
    }

    return render(request, "modules/color.html", context)

@login_required
def add_color(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new inventory item
            return redirect('color')  # Redirect to the inventory list page
    else:
        form = ColorForm()

    return render(request, 'modules/add_color.html', {'form': form})

@login_required
def update_color(request, color_id):
    colors = get_object_or_404(color, pk=color_id)
      

    if request.method == 'POST':
        form = ColorForm(request.POST, instance=colors)
        if form.is_valid():
            form.save()

            return redirect('color')  
    else:
        form = ColorForm(instance=colors)
    
    return render(request, 'modules/update_color.html', {'form': form, 'color': colors})



@login_required
def delete_color(request, color_id):
   
    colors = get_object_or_404(color, id=color_id)
    
    # Check if the HTTP request method is POST (indicating the delete action)
    if request.method == 'POST':
     
        colors.delete()
               
        return redirect('color')  
    
    return redirect('color')


#\\---------------------------------------Color END------------------------------------\\

@login_required
def InventoryList(request):

    inventory_items = Inventory.objects.all()

    context = {
        "inventory" : inventory_items
    }

    return render(request, "modules/inventory.html", context)


@login_required
def add_inventory(request):
    if request.method == 'POST':
        form = AddInventoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new inventory item
            return redirect('inventory')  # Redirect to the inventory list page
    else:
        form = AddInventoryForm()

    return render(request, 'modules/add_inventory.html', {'form': form})


@login_required
def update_inventory(request, inventory_id):
    inventory_item = get_object_or_404(Inventory, pk=inventory_id)
    firestore_client = FirebaseClient()  # Initialize your Firestore client

    if request.method == 'POST':
        form = InventoryUpdateForm(request.POST, instance=inventory_item)
        if form.is_valid():
            form.save()

            # Update the corresponding Firestore document
            firestore_data = {
                "name": form.cleaned_data['name'],
                "type": form.cleaned_data['type'].name,
                "color": form.cleaned_data['color'].name,
                "price": form.cleaned_data['price'],
                "description": form.cleaned_data['description'],
            }
            firestore_client.update(inventory_item.firestore_document_id, firestore_data)

            return redirect('inventory')  # Redirect to the inventory list page after updating
    else:
        form = InventoryUpdateForm(instance=inventory_item)
    
    return render(request, 'modules/update_inventory.html', {'form': form, 'inventory_item': inventory_item})


@login_required
def view_inventory(request, inventory_id):
    inventory_item = get_object_or_404(Inventory, pk=inventory_id)
    return render(request, 'modules/view_inventory.html', {'inventory_item': inventory_item})


@login_required
def delete_inventory(request, item_id):
    # Get the inventory item from Django database
    inventory_item = get_object_or_404(Inventory, id=item_id)
    
    # Check if the HTTP request method is POST (indicating the delete action)
    if request.method == 'POST':
        # Delete the inventory item from Firestore using the FirebaseClient
        firestore_client = FirebaseClient()
        firestore_client.delete_by_id(inventory_item.firestore_document_id)
        
        # Delete the inventory item from Django database
        inventory_item.delete()
        
        # Redirect to the inventory.html page or another appropriate URL
        return redirect('inventory')  # Update 'inventory' with the correct URL name
    
    # If the request method is not POST, render the inventory.html page
    return redirect('inventory')



@login_required
def CustomerList(request):

    customers = Customer.objects.all()

    context = {
        "customers" : customers
    }

    return render(request, "modules/customer.html", context)

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new inventory item
            return redirect('customer')  # Redirect to the inventory list page
    else:
        form = CustomerForm()

    return render(request, 'modules/add_customer.html', {'form': form})

@login_required
def view_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'modules/view_customer.html', {'customer': customer})


@login_required
def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
      # Initialize your Firestore client

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()

            return redirect('customer')  # Redirect to the inventory list page after updating
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'modules/update_customer.html', {'form': form, 'customer': customer})



@login_required
def delete_customer(request, customer_id):
    # Get the inventory item from Django database
    customer = get_object_or_404(Customer, id=customer_id)
    
    # Check if the HTTP request method is POST (indicating the delete action)
    if request.method == 'POST':
        
        
        # Delete the inventory item from Django database
        customer.delete()
        
        # Redirect to the inventory.html page or another appropriate URL
        return redirect('customer')  # Update 'inventory' with the correct URL name
    
    # If the request method is not POST, render the inventory.html page
    return redirect('customer')




