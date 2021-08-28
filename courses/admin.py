from courses.models.comment import Comment
from django.contrib import admin

from courses import models
import courses
from courses.models import Course, Prerequisite, coursemod, learning, tag
from courses.models.video import vid
from courses.models import user_course,payment
from courses.models.couponcode import Coupon
from django.utils.html import format_html

# Register your models here.


class Tagadmin(admin.TabularInline):
    model = tag


class learnadmin(admin.TabularInline):
    model = learning


class preadmin(admin.TabularInline):
    model = Prerequisite

class courseadmin(admin.ModelAdmin):
    inlines = [Tagadmin, learnadmin, preadmin]
    list_display=["get_cname","get_cprice","get_cdiscount","final_price"]
    def get_cname(self,Course):
        return Course.cname
    def get_cprice(self,Course):
        return f"₹{Course.cprice}"
    def get_cdiscount(self,Course):
        return f"{Course.cdiscount}%"
    def final_price(self,Course):
        return Course.cprice-(Course.cprice*Course.cdiscount/100)
    list_filter=["cname"]
    get_cname.short_description = "Name"
    get_cprice.short_description = "Price"
    get_cdiscount.short_description = "Discount"
    final_price.short_description = "Final Price"
class paymentadmin(admin.ModelAdmin):
    model = payment
    list_display=["course","get_user","order_id","status"]
    list_filter=["status"]
    def get_user(self,payment):
        return format_html(f"<a target='_blank' href='/adminauth/user/{payment.user.id}/'>{payment.user}</a>")
    get_user.short_description = "User"
class user_courseadmin(admin.ModelAdmin):
    model = user_course
    list_display=["user","course"]
    list_filter=["course"]
class videoadmin(admin.ModelAdmin):
    model = vid
    list_display=["title","get_course","serial_num","is_preview"]
    list_filter=["course","is_preview"]
    def get_course(self,vid):
        return format_html(f"<a href='/admincourses/course/{vid.course.id}/'>{vid.course}</a>")
admin.site.register(Course, courseadmin)
admin.site.register(vid,videoadmin)
admin.site.register(user_course,user_courseadmin)
admin.site.register(payment,paymentadmin)
admin.site.register(Coupon)
admin.site.register(Comment)