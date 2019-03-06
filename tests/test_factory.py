import pytest
from app import create_app


def test_config():
    with pytest.raises(TypeError):
        create_app().testing
