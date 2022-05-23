from django.contrib import admin
from litreview.models.user import LitUser, UserFollows
from litreview.models.ticket import Ticket
from litreview.models.review import Review


# Register your models here.
admin.site.register(LitUser)
admin.site.register(UserFollows)
admin.site.register(Ticket)
admin.site.register(Review)
