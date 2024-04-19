from rest_framework.views import APIView


class WorkAreaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        drf_request = APIView().initialize_request(request)
        user = drf_request.user
        work_area = request.headers.get("Work-Area", "-1")
        request.work_area = int(work_area)
        response = self.get_response(request)
        return response
