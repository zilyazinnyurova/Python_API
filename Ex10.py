class TestFirstAPI:
    def test_correct_phrase(self):
        phrase = input("Set a phrase:")
        assert len(phrase) < 15, "The phrase > 15"


