from rest_framework.throttling import UserRateThrottle

class ReviewDetailThrottle(UserRateThrottle):
    scope = 'review_detail_throttle'

class ReviewListThrottle(UserRateThrottle):
    scope = 'review_list_throttle'
