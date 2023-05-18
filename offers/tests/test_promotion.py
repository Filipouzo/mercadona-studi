from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from ..models import Product, Promotion, Category


class PromotionModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Vêtements')

    def test_promotion_is_active(self):
        # Promo partant d'hier et finissant demain
        start_date = timezone.now().date() - timedelta(days=1)
        end_date = timezone.now().date() + timedelta(days=1)
        product1 = Product.objects.create(name='short1', description='red', price=100, category=self.category)
        promotion1 = Promotion.objects.create(product=product1, start_date=start_date, end_date=end_date,
                                              discount_percentage=10)

        self.assertTrue(promotion1.is_active())

        # Promo qui s'est terminée hier
        start_date = timezone.now().date() - timedelta(days=2)
        end_date = timezone.now().date() - timedelta(days=1)
        product2 = Product.objects.create(name='short2', description='blue', price=100, category=self.category)
        promotion2 = Promotion.objects.create(product=product2, start_date=start_date, end_date=end_date,
                                              discount_percentage=10)

        self.assertFalse(promotion2.is_active())

        # Promo qui commence demain
        start_date = timezone.now().date() + timedelta(days=1)
        end_date = timezone.now().date() + timedelta(days=2)
        product3 = Product.objects.create(name='short3', description='green', price=100, category=self.category)
        promotion3 = Promotion.objects.create(product=product3, start_date=start_date, end_date=end_date,
                                              discount_percentage=10)

        self.assertFalse(promotion3.is_active())
