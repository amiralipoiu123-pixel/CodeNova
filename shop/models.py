from django.db import models


class ProjectOrder(models.Model):
    SERVICE_CHOICES = [
        ("website", "طراحی وب‌سایت"),
        ("store", "فروشگاه اینترنتی"),
        ("django", "پایتون و Django"),
        ("custom", "پروژه اختصاصی"),
    ]

    STATUS_CHOICES = [
        ("new", "جدید"),
        ("in_progress", "در حال انجام"),
        ("completed", "تکمیل‌شده"),
        ("cancelled", "لغوشده"),
    ]

    name = models.CharField(max_length=100, verbose_name="نام")
    contact = models.CharField(max_length=150, verbose_name="راه ارتباطی")

    service = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES,
        verbose_name="نوع پروژه",
    )

    description = models.TextField(verbose_name="توضیحات پروژه")

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new",
        verbose_name="وضعیت سفارش",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ثبت",
    )

    def str(self):
        return f"{self.name} - {self.get_service_display()}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "سفارش پروژه"
        verbose_name_plural = "سفارش‌های پروژه"