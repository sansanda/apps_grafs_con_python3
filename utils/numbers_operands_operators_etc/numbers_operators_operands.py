import random


def get_random_operator_and_operands(operand1_numbers_range: list,
                                      operators: list,
                                      operand2_numbers_range: list):
    if len(operand1_numbers_range) != 2 or len(operand2_numbers_range) != 2:
        raise Exception("Operand numbers range must content exatly two numbers.")
    if len(operators) == 0:
        raise Exception("Operators dict can't be empty")

    op = random.choice(operators)
    operand1 = random.randint(operand1_numbers_range[0], operand1_numbers_range[1])
    operand2 = random.randint(operand2_numbers_range[0], operand2_numbers_range[1])
    while operand2 == 0:
        operand2 = random.randint(operand2_numbers_range[0], operand2_numbers_range[1])

    result = None
    if op == '/':
        while not operand1 % operand2 == 0:
            operand1 = random.randint(operand1_numbers_range[0], operand1_numbers_range[1])
            operand2 = random.randint(operand2_numbers_range[0], operand2_numbers_range[1])
            while operand2 == 0:
                operand2 = random.randint(operand2_numbers_range[0], operand2_numbers_range[1])

    if op == '*':
        result = operand1 * operand2
    if op == '/':
        result = operand1 / operand2
    if op == '+':
        result = operand1 + operand2
    if op == '-':
        result = operand1 - operand2

    return operand1, op, operand2, int(result)
