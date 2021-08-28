from courses.models import Course, comment, user_course, video
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
# Create your views here.
# def showpage(request, slug):
#     obj = Course.objects.get(slug=slug)
#     pagination(request,obj)
#     action = request.GET.get('action')
# s_num = request.GET.get("lecture")
# next_video = 1
# previous_video = None
# if s_num is None:
#     s_num = 1
# else:
#     next_video += int(s_num)
#     if len(livid) < next_video:
#         next_video = None

#     previous_video = int(s_num) - 1
#     if previous_video < 0 or previous_video == 0:
#         previous_video = None
# player = video.vid.objects.filter(serial_num=s_num, course=obj).first()
# if player.is_preview is False:
# if request.method == "POST" and action=="Addcomment":
#     commentSave(request,obj)
# context = {
# "obj": obj,
# "player": player,
# "listedvideos": livid,
# "nextvideo":next_video,
# "previousvideo":previous_video,
# "allcomment":page_obj,
# "num_pages":num_pages

# }
# return render(request, template_name='courses/showmore.html')


def commentSave(request, obj):
    comment_name = request.POST.get('dname')
    comment_email = request.POST.get('demail')
    comment1 = comment.Comment(user=request.user, body=request.POST.get(
        'dcomment'), Course=obj, Name=comment_name)
    comment1.save()


def pagination(request, obj):
    all_comments = comment.Comment.objects.filter(Course=obj).order_by('id')
    paginator = Paginator(all_comments, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return [int(paginator.num_pages), page_obj]


def playvideo(request, slug):
    obj = Course.objects.get(slug=slug)
    serial_num = request.GET.get("lecture")
    next_video = 1
    previous_video = None
    action = request.GET.get('action')
    if serial_num is None:
        serial_num = 1
    else:
        next_video += int(serial_num)
        previous_video = int(serial_num) - 1
    current_video = video.vid.objects.get(serial_num=serial_num, course=obj)
    videoplayer = obj.vid_set.all().order_by("serial_num")
    if len(videoplayer) < next_video:
        next_video = None
    if previous_video == 0 or previous_video is None:
        previous_video = None
    if request.method == "POST" and action == "Addcomment":
        commentSave(request, obj)
    pagination(request, obj)
    com = pagination(request, obj)
    if (current_video.is_preview is False):
        if request.user.is_authenticated is False:
            return redirect("login")
        user = request.user
        try:
            enrolled_user = user_course.objects.get(user=user, course=obj)
        except:
            return redirect("check-out", slug=obj.slug)
    context = {
        "allcomment": com[1],
        "num_pages" : com[0],
        "obj": obj,
        "listedvideos": videoplayer,
        "nextvideo": next_video,
        "previousvideo": previous_video,
        "video":current_video,
        "CurrentVideo":current_video
    }
    return render(request, template_name='courses/showmore.html', context=context)
