import pytest


class TestPyTestExample:

    @pytest.fixture(autouse=True, scope="function")
    def setup(self):
        print("\nThis is a setup")
        yield
        print("\nThis is a teardown")

    def test_01(self):
        print("\nTest01")

    def test_02(self):
        print("\nTest02")
