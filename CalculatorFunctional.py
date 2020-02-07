import Operations as op

print('Hello, welcome to the calculator.')

while True:
    function = input('Would you like to add, subtract, multiply or divide?').strip().lower()
    if function == 'break':
        break

    user_input = input('Please give me a number. If done type DONE').strip().lower()
    list = []
    is_true = True
    while is_true == True:
        user_input = input('Please give me a number. If done type DONE').strip().lower()
        if user_input.isnumeric() == True:
            user_input = int(user_input)
            list.append(user_input)

        elif user_input == 'break':
            break

        elif not user_input.isnumeric():
            if user_input == 'done':
                if function == 'multiply':
                    calc = op.multiply(list)
                    print(calc)
                    is_true = False

                elif function == 'divide':
                    calc = op.divide(list)
                    print(calc)
                    is_true = False

                elif function == 'add':
                    calc = op.add(list)
                    print(calc)
                    is_true = False
                elif function == 'subtract':
                    calc = op.subtract(list)
                    print(calc)
                    is_true = False

                else:
                    print('Please give a valid operation')
                    is_true = False

            else:
                print('Invalid input')