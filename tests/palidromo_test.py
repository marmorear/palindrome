from palindrome.palindrome import valid_palindrome, valid_null, slugfy
from unittest import main, TestCase


class TestPalindrome(TestCase):
    def test_if_returns_lowerletterfisrt_palindrome_true(self):
        result = valid_palindrome("Rotator")
        expected = "É palindrome!!!"
        self.assertEqual(result, expected)

    def test_if_returns_phrase_palindrome_true(self):
        result = valid_palindrome("Able was I, ere I saw Elba")
        expected = "É palindrome!!!"
        self.assertEqual(result, expected)

    def test_if_returns_numbers_palindrome_true(self):
        result = valid_palindrome("1")
        expected = "É palindrome!!!"
        self.assertEqual(result, expected)

    def test_if_returns_special_caracter_palindrome_true(self):
        result = valid_palindrome("Socorram-me subi no ônibus em marrocos")
        expected = "É palindrome!!!"
        self.assertEqual(result, expected)

    def test_if_returns_random_letters_palindrome_false(self):
        result = valid_palindrome("xyz")
        expected = "Não é palindrome! :("
        self.assertEqual(result, expected)

    def test_if_returns_special_caracter_palindrome_false(self):
        result = valid_palindrome("Top . post!")
        expected = "Não é palindrome! :("
        self.assertEqual(result, expected)

    def test_input_null_value_false(self):
        result = valid_null("  ")
        expected = False
        self.assertEqual(result, expected)

    def test_input_null_value_0_input_false(self):
        result = valid_null("")
        expected = False
        self.assertEqual(result, expected)

    def test_input_value_true(self):
        result = valid_null("abc")
        expected = True
        self.assertEqual(result, expected)

    def test_slugfy(self):
        result = slugfy("AblewasI,ereIsawElba")
        expected = "ablewasiereisawelba"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
