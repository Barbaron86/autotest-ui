import random

import pytest

PLATFORM = "linux"


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
    assert random.choice([True, False]), "Random failure to test reruns"


@pytest.mark.flaky(reruns=2, reruns_delay=1)
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False]), "Random failure to test reruns in class"

    def test_rerun_2(self):
        assert random.choice([True, False]), "Random failure to test reruns in class"


@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "windows")
def test_rerun_with_condition():
    assert random.choice([True, False]), "Random failure to test reruns with condition"
