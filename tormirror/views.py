from rest_framework.response import Response
from rest_framework.views import APIView

from tormirror.serializers import RequestSerializer
from tormirror.utils import get_ok_response


class RequestView(APIView):

    @staticmethod
    def post(request):
        serializer = RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        args = serializer.validated_data['args']
        kwargs = serializer.validated_data['kwargs']
        method = serializer.validated_data['method']
        response = get_ok_response(method, *args, **kwargs)
        return Response(data={'content': response.content.decode(errors='replace')}, status=response.status_code)

