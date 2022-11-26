from pytest_factoryboy import register
from factories import ProviderFactory
import pytest

# Register Approach
register(ProviderFactory)


@pytest.fixture
def providers():
    return ProviderFactory.create_batch(10)
