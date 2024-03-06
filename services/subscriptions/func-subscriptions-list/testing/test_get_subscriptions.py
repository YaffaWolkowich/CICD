from unittest.mock import patch, Mock
from project.get_subscriptions import get_subscriptions


class MockSubscription:
    def __init__(self, tags=None):
        self.tags = tags if tags is not None else {}


class MockSubscriptionClient:
    def __init__(self):
        self.subscriptions = MockListSubscriptions()


class MockListSubscriptions:
    def list(self):
        return [
            MockSubscription(tags={"tag1": "value1"}),
            MockSubscription(),
            MockSubscription(tags={"tag2": "value2"}),
        ]


@patch(
    "project.get_subscriptions.DefaultAzureCredential", Mock(return_value="Credentials")
)
@patch(
    "project.get_subscriptions.SubscriptionClient",
    Mock(return_value=MockSubscriptionClient()),
)
def test_get_subscriptions():
    subscriptions = get_subscriptions()
    assert len(subscriptions) == 2


@patch(
    "project.get_subscriptions.DefaultAzureCredential",
    Mock(side_effect=Exception("raise exception")),
)
@patch(
    "project.get_subscriptions.SubscriptionClient",
    Mock(return_value=MockSubscriptionClient()),
)
def test_get_subscriptions_return_error_message():
    assert get_subscriptions() == "raise exception"
