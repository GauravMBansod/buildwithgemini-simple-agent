from google.cloud import firestore

# IMPORTANT: Hardcoded Project ID string to prevent Agent Platform project-number fallback issues
PROJECT_ID = "qwiklabs-gcp-01-81ce122bf040"

def seed_database():
    db = firestore.Client(project=PROJECT_ID)
    
    items = [
        {
            "item_name": "Organic Eggs",
            "category": "Dairy & Eggs",
            "quantity": 12,
            "unit": "pcs",
            "notes": "Grade A Large",
        },
        {
            "item_name": "Almond Milk",
            "category": "Dairy Alternatives",
            "quantity": 1,
            "unit": "carton",
            "notes": "Unsweetened",
        },
        {
            "item_name": "Arborio Rice",
            "category": "Grains & Pasta",
            "quantity": 2,
            "unit": "lbs",
            "notes": "For risotto",
        },
        {
            "item_name": "Extra Virgin Olive Oil",
            "category": "Pantry Staples",
            "quantity": 1,
            "unit": "bottle",
            "notes": "Cold pressed",
        },
    ]

    for item in items:
        doc_id = item["item_name"].lower().replace(" ", "_")
        doc_ref = db.collection("pantry_items").document(doc_id)
        doc_ref.set(item)
        print(f"Seeded document: {doc_id} -> {item['item_name']}")

    print("Firestore seeding finished successfully.")

if __name__ == "__main__":
    seed_database()
