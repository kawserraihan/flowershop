from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from flowerAPI.firebase_client import FirebaseClient

# Create your views here.
def home(request):
    return render(request, "base/index.html")

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

def signin(request):

    if request.method == "POST":

        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'base.html', {'fname': fname})

        else:
            messages.error(request, "Incorrect Credentiials")
            return redirect('home')
    

    return render(request, "authentication/signin.html")

def signout(request):
    return render(request, "authentication/signout.html")


def InventoryList(request):

    inventory_items = Inventory.objects.all()

    context = {
        "inventory" : inventory_items
    }

    return render(request, "modules/inventory.html", context)

def add_inventory(request):
    if request.method == 'POST':
        form = AddInventoryForm(request.POST)
        if form.is_valid():
            inventory_item = form.save()  # Save the new inventory item
            return redirect('inventory')  # Redirect to the inventory list page
    else:
        form = AddInventoryForm()

    return render(request, 'modules/add_inventory.html', {'form': form})

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

def view_inventory(request, inventory_id):
    inventory_item = get_object_or_404(Inventory, pk=inventory_id)
    return render(request, 'modules/view_inventory.html', {'inventory_item': inventory_item})

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




