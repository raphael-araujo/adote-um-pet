from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .email_service import enviar_email_confirmacao
from .serializers import AdocaoSerializer


class AdocaoList(APIView):
    def post(self, request, format=None):
        serializer = AdocaoSerializer(data=request.data)

        if serializer.is_valid():
            adocao = serializer.save()
            enviar_email_confirmacao(adocao)
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(
            {"errors": serializer.errors, "message": "Houveram erros de validação."},
            status=HTTP_400_BAD_REQUEST,
        )
