from rest_framework.serializers import ModelSerializer
from rest_framework.request import Request
from ..exceptions.invalid_request_payload_exception import (
    InvalidRequestPayloadException,
)


def assertRequestPayloadIsValidAndGetSerializedData(
    requestData: Request.data, serializer: ModelSerializer
) -> dict:
    requestPayload = serializer(data=requestData)
    if not requestPayload.is_valid():
        raise InvalidRequestPayloadException(requestPayload.errors)
    return requestPayload.data
