import rules
from django.conf import settings
from rules.permissions import add_perm
from rules.predicates import predicate, is_authenticated, always_allow


@rules.predicate
def is_own_ticket(user, obj):
    if not obj:
        return False
    return user.is_authenticated and obj.user == user


@rules.predicate
def is_own_review(user, review):
    if not review:
        return False
    return user.is_authenticated & review.user == user


rules.add_perm('litreview.view_ticket', always_allow)
rules.add_perm('litreview.add_ticket', is_authenticated)
rules.add_perm('litreview.change_ticket', is_own_ticket)
rules.add_perm('litreview.delete_ticket', is_own_ticket)


rules.add_perm('litreview.view_review', always_allow)
rules.add_perm('litreview.add_review', is_authenticated)
rules.add_perm('litreview.change_review', is_own_review)
rules.add_perm('litreview.delete_review', is_own_review)
