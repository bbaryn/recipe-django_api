from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

  def test_create_user_with_email_successful(self):
    """Create a new user with an emial is successful"""
    email = 'test@example.com'
    password = 'Testpass123'
    user = get_user_model().objects.create_user(
      email=email,
      password=password
    )

    self.assertEqual(user.email,email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email(self):
    """Email for new user is normalized"""
    email = 'test@EXAMPLe.com'
    user = get_user_model().objects.create_user(email, 'test123')

    self.assertEqual(user.email, email.lower())
