from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Q
from shop.models import ProjectOrder


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("dashboard:home")

    error = None

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user and user.is_active and user.is_staff:
            login(request, user)
            return redirect("dashboard:home")

        error = "نام کاربری یا رمز عبور اشتباه است."

    return render(
        request,
        "dashboard/login.html",
        {"error": error},
    )


from django.db.models import Q

@login_required(login_url="dashboard:login")
def admin_home(request):
    if not request.user.is_staff:
        logout(request)
        return redirect("dashboard:login")

    orders = ProjectOrder.objects.all()

    search = request.GET.get("q", "").strip()
    selected_status = request.GET.get("status", "").strip()
    selected_service = request.GET.get("service", "").strip()

    if search:
        orders = orders.filter(
            Q(name__icontains=search) |
            Q(contact__icontains=search)
        )

    allowed_statuses = {
        value for value, label in ProjectOrder.STATUS_CHOICES
    }
    allowed_services = {
        value for value, label in ProjectOrder.SERVICE_CHOICES
    }

    if selected_status in allowed_statuses:
        orders = orders.filter(status=selected_status)
    else:
        selected_status = ""

    if selected_service in allowed_services:
        orders = orders.filter(service=selected_service)
    else:
        selected_service = ""

    orders = orders.order_by("-created_at")

    all_orders = ProjectOrder.objects.all()

    context = {
        "total_orders": all_orders.count(),

        "new_orders": all_orders.filter(status="new").count(),
        "in_progress_orders": all_orders.filter(
            status="in_progress"
        ).count(),
        "completed_orders": all_orders.filter(
            status="completed"
        ).count(),
        "cancelled_orders": all_orders.filter(
            status="cancelled"
        ).count(),

        "orders": orders,
        "search": search,
        "selected_status": selected_status,
        "selected_service": selected_service,
        "status_choices": ProjectOrder.STATUS_CHOICES,
        "service_choices": ProjectOrder.SERVICE_CHOICES,
    }

    return render(request, "dashboard/home.html", context)


@login_required(login_url="dashboard:login")
@require_POST
def update_order_status(request, order_id):
    if not request.user.is_staff:
        logout(request)
        return redirect("dashboard:login")

    order = get_object_or_404(ProjectOrder, pk=order_id)
    new_status = request.POST.get("status", "")

    allowed_statuses = {
        value for value, label in ProjectOrder.STATUS_CHOICES
    }

    if new_status not in allowed_statuses:
        messages.error(request, "وضعیت انتخاب‌شده معتبر نیست.")
        return redirect("dashboard:home")

    order.status = new_status
    order.save(update_fields=["status"])

    messages.success(
        request,
        f"وضعیت سفارش «{order.name}» تغییر کرد.",
    )

    return redirect("dashboard:home")


@login_required(login_url="dashboard:login")
@require_POST
def admin_logout(request):
    if not request.user.is_staff:
        logout(request)
        return redirect("dashboard:login")

    logout(request)
    return redirect("dashboard:login")