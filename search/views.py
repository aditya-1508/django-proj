from django.shortcuts import render
from django.db.models import Q
from accounts.models import CustomUser
from connections.models import Connection


def search_users(request):
    query = request.GET.get("q", "").strip()  # ✅ Ensure query is always a string

    # ✅ Check if the user is authenticated
    if not request.user.is_authenticated:
        return render(
            request, "search/results.html", {"error": "Please log in to search."}
        )

    user = request.user  # ✅ Get logged-in user

    # ✅ Fetch all users except the logged-in user
    all_results = CustomUser.objects.exclude(id=user.id)

    # ✅ Apply search filter if a query is provided
    if query:
        all_results = all_results.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
            | Q(phone__icontains=query)
        )

    # ✅ Fetch only connected users
    connected_results = CustomUser.objects.filter(
        id__in=Connection.objects.filter(from_user=user).values_list(
            "to_user", flat=True
        )
    )

    # ✅ Exclude already connected users from the list of users to connect with
    not_connected_results = all_results.exclude(
        id__in=connected_results.values_list("id", flat=True)
    )

    return render(
        request,
        "search/results.html",
        {
            "query": query,
            "connected_results": connected_results,
            "not_connected_results": not_connected_results,  # ✅ Fixing the issue
        },
    )
