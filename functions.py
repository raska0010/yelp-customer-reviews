import pandas as pd

def get_file(filename):

    import pandas as pd

    while True:
        user_input = input(
            '''
                Do you want to load {0}?
                Press 1 to load the file, 
                press 2 to terminate without loading the file
                '''.format(filename)
        )

        try:
            user_input = int(user_input)

            if user_input == 1:
                print('Loading file...')

                try:
                    f = pd.read_csv(filename)
                    print('File loaded...')
                    return f
                except FileNotFoundError:
                    print('File does not exist...')
                    break

            elif user_input == 2:
                print('Terminated without loading the file...')
                break

            else:
                print('Invalid input. Please enter either 1 or 2')

        except ValueError:
            print('Invalid input. Please enter either 1 or 2')