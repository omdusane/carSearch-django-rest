from rest_framework.pagination import PageNumberPagination

class ReviewListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'limit'
    max_page_size = 10
    last_page_strings = 'last'
