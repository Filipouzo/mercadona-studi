from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from ..models import Product, Promotion, Category


class PromotionModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Testcategories')
        self.product = Product.objects.create(name='TestProduct', description='TestDescription', price=100,
                                              category=self.category)

    def test_promotion_is_active(self):
        # Create a promotion that started yesterday and ends tomorrow
        start_date = timezone.now().date() - timedelta(days=1)
        end_date = timezone.now().date() + timedelta(days=1)
        promotion = Promotion.objects.create(product=self.product, start_date=start_date, end_date=end_date,
                                             discount_percentage=10)

        self.assertTrue(promotion.is_active())

        # Create a promotion that ended yesterday
        start_date = timezone.now().date() - timedelta(days=2)
        end_date = timezone.now().date() - timedelta(days=1)
        promotion = Promotion.objects.create(product=self.product, start_date=start_date, end_date=end_date,
                                             discount_percentage=10)

        self.assertFalse(promotion.is_active())

        # Create a promotion that starts tomorrow
        start_date = timezone.now().date() + timedelta(days=1)
        end_date = timezone.now().date() + timedelta(days=2)
        promotion = Promotion.objects.create(product=self.product, start_date=start_date, end_date=end_date,
                                             discount_percentage=10)

        self.assertFalse(promotion.is_active())