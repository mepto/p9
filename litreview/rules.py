import rules
from rules.predicates import predicate, is_authenticated, always_allow

from litreview.models import Review


@rules.predicate
def is_own_ticket(user, obj):
    if not obj:
        return False
    return user.is_authenticated and obj.user == user


@rules.predicate
def is_own_review(user, review):
    if not review:
        return False
    return user.is_authenticated & (review.user == user)


@rules.predicate
def is_own_follower(user, follower):
    if not follower:
        return False
    return user.is_authenticated & (follower.user == user)


@rules.predicate
def ticket_has_review(user, ticket):
    if not ticket:
        return False
    if Review.objects.get(ticket_id=ticket.id):
        return True
    else:
        return False


rules.add_perm('litreview.view_ticket', is_authenticated)
rules.add_perm('litreview.add_ticket', is_authenticated)
rules.add_perm('litreview.change_ticket', is_own_ticket)
rules.add_perm('litreview.delete_ticket', is_own_ticket)


rules.add_perm('litreview.view_review', is_authenticated)
rules.add_perm('litreview.add_review', is_authenticated & ~ticket_has_review)
rules.add_perm('litreview.change_review', is_own_review)
rules.add_perm('litreview.delete_review', is_own_review)

rules.add_perm('litreview.view_followers', is_authenticated)
rules.add_perm('litreview.delete_followers', is_authenticated & is_own_follower)
