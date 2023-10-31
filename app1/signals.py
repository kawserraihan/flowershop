from django.db.models.signals import post_save
from django.dispatch import receiver
from app1.models import Inventory
from flowerAPI.firebase_client import FirebaseClient
from django.http import JsonResponse

@receiver(post_save, sender=Inventory)
def create_firestore_document(sender, instance, created, **kwargs):
    if created:
        data = {
            "flowerName": instance.name,
            "flowerType": instance.type.name,
            "flowerColor": instance.color.name,
            "flowerPrice": instance.price,
            "flowerDescription": instance.description,
            "flowerImage": instance.image,

        }

        firestore_client = FirebaseClient()
        doc_ref = firestore_client.create(data)
       

        if doc_ref:
            # Store the Firestore document ID in the Inventory model
            instance.firestore_document_id = doc_ref
            instance.save()
        else:
            print("Firestore document creation failed.")