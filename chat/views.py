from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_list_or_404
from django.shortcuts import render


@login_required
def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id)
    except:
        return HttpResponseForbidden()

    return render(request, "chat/room.html", {"course": course})
