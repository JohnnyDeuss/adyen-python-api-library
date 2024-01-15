from ..base import AdyenServiceBase


class TerminalActionsCompanyLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TerminalActionsCompanyLevelApi, self).__init__(client=client)
        self.service = "management"
        self.baseUrl = "https://management-test.adyen.com/v3"

    def get_terminal_action(self, companyId, actionId, idempotency_key=None, **kwargs):
        """
        Get terminal action
        """
        endpoint = self.baseUrl + f"/companies/{companyId}/terminalActions/{actionId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def list_terminal_actions(self, companyId, idempotency_key=None, **kwargs):
        """
        Get a list of terminal actions
        """
        endpoint = self.baseUrl + f"/companies/{companyId}/terminalActions"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

