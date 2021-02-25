from hstest.exceptions import WrongAnswer
from hstest.test_case import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
import random
import re

card_number = ''
pin = ''
are_all_inputs_read = False


def get_credentials(output: str):
    number = re.findall(r'^400000\d{10}$', output, re.MULTILINE)
    if not number:
        raise WrongAnswer('You are printing the card number incorrectly. '
                                   'The card number should look like in the example: 400000DDDDDDDDDD,'
                                   ' where D is a digit.\nMake sure the card number is 16-digit length and '
                                   'you don\'t print any extra spaces at the end of the line!')

    PIN = re.findall(r'^\d{4}$', output, re.MULTILINE)
    if not PIN:
        raise WrongAnswer('You are printing the card PIN incorrectly. '
                                   'The PIN should look like in the example: DDDD, where D is a digit.\n'
                                   'Make sure the PIN is 4-digit length and you don\'t print any extra spaces at the'
                                   ' end of the line!')

    return number[0], PIN[0]


def test_card_generation(output: str, value_to_return):
    global card_number, pin, are_all_inputs_read
    are_all_inputs_read = False
    credentials = get_credentials(output)
    card_number = credentials[0]
    pin = credentials[1]
    return value_to_return


def test_difference_between_generations(output: str, value_to_return):
    global card_number, pin, are_all_inputs_read
    credentials = get_credentials(output)
    another_card_number = credentials[0]

    if another_card_number == card_number:
        return CheckResult.wrong('Your program generates two identical card numbers!')
    are_all_inputs_read = True

    return value_to_return


def test_sign_in_with_correct_credentials(output: str, value_to_return):
    global card_number, pin
    return '{}\n{}'.format(card_number, pin)


def test_output_after_correct_sign_in(output: str, value_to_return):
    global are_all_inputs_read
    are_all_inputs_read = True
    if 'successfully' not in output.lower():
        return CheckResult.wrong(
            'There is no \'successfully\' in your output after signing in with correct credentials')
    return value_to_return


def test_sign_in_with_wrong_pin(output: str, value_to_return):
    global card_number, pin
    wrong_pin = pin
    while pin == wrong_pin:
        wrong_pin = ''.join(list(map(str, random.sample(range(1, 10), 4))))
    return '{}\n{}\n'.format(card_number, wrong_pin)


def test_output_after_wrong_pin(output: str, value_to_return):
    global are_all_inputs_read
    are_all_inputs_read = True
    if 'wrong' not in output.lower():
        return CheckResult.wrong(
            'There is no \'wrong\' in your output after signing in with incorrect credentials')
    return value_to_return


def test_sign_in_with_wrong_card_number(output: str, value_to_return):
    global card_number, pin
    wrong_card_number = card_number
    while wrong_card_number == card_number:
        temp = [4, 0, 0, 0, 0, 0]
        for _ in range(10):
            temp.append(random.randint(1, 9))
        wrong_card_number = ''.join(list(map(str, temp)))
    return '{}\n{}\n'.format(wrong_card_number, pin)


def test_output_after_wrong_card_number(output: str, value_to_return):
    global are_all_inputs_read
    are_all_inputs_read = True
    if 'wrong' not in output.lower():
        return CheckResult.wrong(
            'There is no \'wrong\' in your output after signing in with incorrect credentials')
    return value_to_return


def is_passed_luhn_algorithm(number):
    luhn = [int(char) for char in str(number)]
    for i, num in enumerate(luhn):
        if (i + 1) % 2 == 0:
            continue
        temp = num * 2
        luhn[i] = temp if temp < 10 else temp - 9
    return sum(luhn) % 10 == 0


def test_luhn_algorithm(output: str, correct_num_of_cards):
    global are_all_inputs_read

    numbers = re.findall(r'400000\d{10,}', output, re.MULTILINE)

    for number in numbers:
        if len(number) != 16:
            return CheckResult.wrong(f'Wrong card number \'{number}\'. The card number should be 16-digit length.')
        if not is_passed_luhn_algorithm(number):
            return CheckResult.wrong('The card number \'{}\' doesn\'t pass luhn algorithm!'.format(number))

    if len(numbers) != correct_num_of_cards:
        return CheckResult.wrong(
            f'After creating {correct_num_of_cards} cards, found {len(numbers)} cards with correct format\n'
            f'The card number should be 16-digit length and should start with 400000.')

    are_all_inputs_read = True
    return '0'


class BankingSystem(StageTest):

    def generate(self):
        return [
            TestCase(
                stdin=[
                    '1',
                    lambda output: test_card_generation(output, '1'),
                    lambda output: test_difference_between_generations(output, '0')
                ]),
            TestCase(
                stdin=[
                    '1',
                    lambda output: test_card_generation(output, '2'),
                    lambda output: test_sign_in_with_correct_credentials(output, None),
                    lambda output: test_output_after_correct_sign_in(output, '0')
                ]),
            TestCase(
                stdin=[
                    '1',
                    lambda output: test_card_generation(output, '2'),
                    lambda output: test_sign_in_with_wrong_pin(output, None),
                    lambda output: test_output_after_wrong_pin(output, '0')
                ]),
            TestCase(
                stdin=[
                    '1',
                    lambda output: test_card_generation(output, '2'),
                    lambda output: test_sign_in_with_wrong_card_number(output, None),
                    lambda output: test_output_after_wrong_card_number(output, '0')
                ]),
            TestCase(
                stdin=[
                    '1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1',
                    lambda output: test_luhn_algorithm(output, 11),
                ])
        ]

    def check(self, reply: str, attach) -> CheckResult:
        if are_all_inputs_read:
            return CheckResult.correct()
        else:
            return CheckResult.wrong('You didn\'t read all inputs!')


if __name__ == '__main__':
    BankingSystem('banking.banking').run_tests()
