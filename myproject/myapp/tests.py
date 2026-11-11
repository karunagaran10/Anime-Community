from django.contrib.auth.hashers import check_password
from django.test import TestCase
from django.urls import reverse
from django.utils.formats import date_format

from .models import Student


class StudentCrudTests(TestCase):
    def student_data(self, **overrides):
        data = {
            "name": "Aki",
            "email": "aki@example.com",
            "password": "StrongPass123",
            "confirm_password": "StrongPass123",
        }
        data.update(overrides)
        return data

    def test_homepage_registration_form_renders(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'action="/student/"')
        self.assertContains(response, 'name="csrfmiddlewaretoken"')

    def test_information_pages_render_their_own_content(self):
        pages = (
            ("about", "Built by fans."),
            ("service", "Explore the"),
            ("contact", "Say"),
        )
        for route_name, heading in pages:
            with self.subTest(page=route_name):
                response = self.client.get(reverse(route_name))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, heading)

    def test_create_and_list_student(self):
        response = self.client.post(reverse("student"), self.student_data())

        self.assertRedirects(response, reverse("students"))
        student = Student.objects.get(email="aki@example.com")
        self.assertTrue(check_password("StrongPass123", student.password_hash))
        self.assertIsNotNone(student.joined_at)
        list_response = self.client.get(reverse("students"))
        self.assertNotContains(list_response, "StrongPass123")
        self.assertContains(list_response, date_format(student.joined_at, "M j, Y"))

    def test_rejects_mismatched_passwords(self):
        response = self.client.post(
            reverse("student"),
            self.student_data(confirm_password="DifferentPass123"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.count(), 0)
        self.assertContains(response, "Passwords do not match.")

    def test_update_changes_student_and_optional_password(self):
        student = Student.objects.create(
            name="Aki",
            email="aki@example.com",
            password_hash="existing-hash",
        )
        joined_at = student.joined_at

        response = self.client.post(
            reverse("student_edit", args=[student.pk]),
            self.student_data(name="Aki Updated", password="", confirm_password=""),
        )

        self.assertRedirects(response, reverse("students"))
        student.refresh_from_db()
        self.assertEqual(student.name, "Aki Updated")
        self.assertEqual(student.password_hash, "existing-hash")
        self.assertEqual(student.joined_at, joined_at)

    def test_delete_requires_post_and_removes_student(self):
        student = Student.objects.create(
            name="Aki",
            email="aki@example.com",
            password_hash="existing-hash",
        )

        response = self.client.get(reverse("student_delete", args=[student.pk]))
        self.assertEqual(response.status_code, 405)
        self.assertTrue(Student.objects.filter(pk=student.pk).exists())

        response = self.client.post(reverse("student_delete", args=[student.pk]))
        self.assertRedirects(response, reverse("students"))
        self.assertFalse(Student.objects.filter(pk=student.pk).exists())
