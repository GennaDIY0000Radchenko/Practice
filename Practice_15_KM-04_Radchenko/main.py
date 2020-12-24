from factorial import factorial
from exp_root import root, exponentiation
from logarithm import logarithm


def main():
    while True:
        choose1 = str(input('\nEXPONENTIATION -> E'
                            '\nFACTORIAL      -> F'
                            '\nLOGARITHM      -> L'
                            '\nROOT           -> R'
                            '\nchoose one->'))
        choose = choose1.upper()

        if choose == 'EXPONENTIATION' or choose == 'E':
            while True:
                choose2 = str(input('\nX POWER 2 ->2'
                                    '\nX POWER 3 ->3'
                                    '\nchoose one->'))
                choose = choose2
                if choose == '2':
                    while True:
                        n = input('Enter real number ->')
                        if n == '':
                            break
                        try:
                            n = float(n)
                            print(f'({n})^2 = {exponentiation.exp2(n)}')
                        except ValueError:
                            print('Invalid!')

                elif choose == '3':
                    while True:
                        n = input('Enter real number ->')
                        if n == '':
                            break
                        try:
                            n = float(n)
                            print(f'({n})^3 = {exponentiation.exp3(n)}')
                        except ValueError:
                            print('Invalid!')

                elif choose == '':
                    break
                else:
                    print('Invalid! Enter "2" or "3"!')

        elif choose == 'FACTORIAL' or choose == 'F':
            while True:
                n = input('Enter natural number ->')
                if n == '':
                    break
                try:
                    n = int(n)
                    assert n >= 0
                    print(f'{n}! = {factorial.fact(n)}')
                except ValueError:
                    print('Invalid!')
                except AssertionError:
                    print('Invalid!')

        elif choose == 'LOGARITHM' or choose == 'L':
            while True:
                choose2 = str(input('\nLog -> log'
                                    '\nLn  -> ln'
                                    '\nLg  -> lg'
                                    '\nchoose one ->'))
                choose = choose2.lower()

                if choose == 'log':
                    while True:
                        while True:
                            base = input('Enter base (not negative number ,which is not equal to one) ->')
                            if base == '':
                                break
                            try:
                                base = float(base)
                                assert base > 0 and base != 1
                                break
                            except ValueError:
                                print('Invalid!')
                            except AssertionError:
                                print('Invalid!')
                        if base == '':
                            break

                        while True:
                            n = input('Enter number (number > 0) ->')
                            if n == '':
                                break
                            try:
                                n = float(n)
                                assert n > 0
                                print(f'log(base={base})({n}) = {logarithm.log(n, base)}')
                                break
                            except ValueError:
                                print('Invalid!')
                            except AssertionError:
                                print('Invalid!')

                elif choose == 'ln':
                    while True:
                        n = input('Enter not negative number (which is not equal to one) ->')
                        if n == '':
                            break
                        try:
                            n = float(n)
                            print(f'ln({n}) = {logarithm.ln(n)}')
                        except ValueError:
                            print('Invalid!')

                elif choose == 'lg':
                    while True:
                        n = input('Enter not negative number (which is not equal to one) ->')
                        if n == '':
                            break
                        try:
                            n = float(n)
                            print(f'lg({n}) = {logarithm.lg(n)}')
                        except ValueError:
                            print('Invalid!')

                elif choose == '':
                    break
                else:
                    print('Invalid! Enter "2" or "3"!')

        elif choose == 'ROOT' or choose == 'R':
            while True:
                choose2 = str(input('\nX ROOT 2 ->2'
                                    '\nX ROOT 3 ->3'
                                    '\nchoose one->'))
                choose = choose2.upper()
                if choose == '2':
                    while True:
                        n = input('Enter not negative number ->')
                        if n == '':
                            break
                        try:
                            n = float(n)
                            assert n >= 0
                            print(f'sqrt({n}) = {root.root2(n)}')
                        except ValueError:
                            print('Invalid!')
                        except AssertionError:
                            print('Invalid!')

                elif choose == '3':
                    while True:
                        n = input('Enter real number ->')
                        if n == '':
                            break
                        try:
                            n = float(n)
                            print(f'cbrt({n}) = {root.root3(n)}')
                        except ValueError:
                            print('Invalid!')

                elif choose == '':
                    break
                else:
                    print('Invalid! Enter "2" or "3"!')

        elif choose == '':
            break
        else:
            print('Invalid! Enter "EXPONENTIATION" or "FACTORIAL" or "LOGARITHM" or "ROOT"!')


if __name__ == '__main__':
    print("Let's start")
    main()
    print('Have a nice day!')
