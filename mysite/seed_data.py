import os
import django

# Djangoの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from core.models import Category, Item

def seed():
    print("Seeding categories...")
    # 画像の種類に合わせてカテゴリを作成
    categories = ['Paddle', 'Ball', 'Apparel']
    category_objs = {}
    for name in categories:
        obj, created = Category.objects.get_or_create(name=name)
        category_objs[name] = obj
        if created:
            print(f"Created category: {name}")

    print("Seeding items with images...")
    items_data = [
        {
            'name': 'Professional Paddle Model 1',
            'price': 25000,
            'description': 'High performance graphite paddle.',
            'category': category_objs['Paddle'],
            'image': 'item_images/paddle1.jpg'
        },
        {
            'name': 'Tournament Paddle Model 2',
            'price': 18000,
            'description': 'Lightweight and durable.',
            'category': category_objs['Paddle'],
            'image': 'item_images/paddle2.jpg'
        },
        {
            'name': 'Premium Outdoor Ball (Yellow)',
            'price': 1200,
            'description': 'Approved for tournament play.',
            'category': category_objs['Ball'],
            'image': 'item_images/ball1.png'
        },
        {
            'name': 'Indoor Training Ball (Orange)',
            'price': 900,
            'description': 'Soft and consistent bounce.',
            'category': category_objs['Ball'],
            'image': 'item_images/ball2.png'
        },
        {
            'name': 'Pickleball Performance T-shirt (Blue)',
            'price': 4500,
            'description': 'Breathable fabric for intense matches.',
            'category': category_objs['Apparel'],
            'image': 'item_images/t-shirts1.png'
        },
        {
            'name': 'Pickleball Fan T-shirt (Gray)',
            'price': 3800,
            'description': 'Comfortable cotton for casual wear.',
            'category': category_objs['Apparel'],
            'image': 'item_images/t-shirts2.png'
        },
    ]

    for item_info in items_data:
        obj, created = Item.objects.get_or_create(
            name=item_info['name'],
            defaults={
                'price': item_info['price'],
                'description': item_info['description'],
                'category': item_info['category'],
                'image': item_info['image']
            }
        )
        if created:
            print(f"Created item: {item_info['name']} with image {item_info['image']}")
        else:
            # 既存の場合は画像を更新（念のため）
            obj.image = item_info['image']
            obj.save()
            print(f"Updated item image: {item_info['name']}")

if __name__ == '__main__':
    seed()
    print("Seeding completed successfully!")
