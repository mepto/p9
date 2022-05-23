from django.contrib import admin
from litreview.src.web.litreview.models.user import LitUser, UserFollows
from litreview.src.web.litreview.models.ticket import Ticket
from litreview.src.web.litreview.models.review import Review


# Register your models here.
admin.site.register(LitUser)
admin.site.register(UserFollows)
admin.site.register(Ticket)
admin.site.register(Review)
