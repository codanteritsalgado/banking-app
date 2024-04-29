from rest_framework.views import APIView
from rest_framework.response import Response

class IndexAPI(APIView):
    def get(self, request):
        data = [{
            "url": request.build_absolute_uri('/api/user/')
        }]
        return Response(data)
