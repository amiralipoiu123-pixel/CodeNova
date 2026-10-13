from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ProjectOrder

def home(request):
    return render(request, 'shop/home.html')

def order(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        contact = request.POST.get("contact", "").strip()
        service = request.POST.get("service", "").strip()
        description = request.POST.get("description", "").strip()

        valid_services = {
            choice[0] for choice in ProjectOrder.SERVICE_CHOICES
        }

        if (
            not name
            or not contact
            or service not in valid_services
            or not description
        ):
            messages.error(request, "لطفاً همهٔ فیلدها را درست تکمیل کن.")
            return render(request, "shop/order.html")

        ProjectOrder.objects.create(
            name=name,
            contact=contact,
            service=service,
            description=description,
        )

        messages.success(request, "سفارش شما با موفقیت ثبت شد.")
        return redirect("home")

    return render(request, "shop/order.html")
