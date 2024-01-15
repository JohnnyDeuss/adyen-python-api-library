from ..base import AdyenServiceBase


class BusinessLinesApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(BusinessLinesApi, self).__init__(client=client)
        self.service = "legalEntityManagement"
        self.baseUrl = "https://kyc-test.adyen.com/lem/v3"

    def create_business_line(self, request, idempotency_key=None, **kwargs):
        """
        Create a business line
        """
        endpoint = self.baseUrl + f"/businessLines"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def delete_business_line(self, id, idempotency_key=None, **kwargs):
        """
        Delete a business line
        """
        endpoint = self.baseUrl + f"/businessLines/{id}"
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_business_line(self, id, idempotency_key=None, **kwargs):
        """
        Get a business line
        """
        endpoint = self.baseUrl + f"/businessLines/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_business_line(self, request, id, idempotency_key=None, **kwargs):
        """
        Update a business line
        """
        endpoint = self.baseUrl + f"/businessLines/{id}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

