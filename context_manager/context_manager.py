#used to auto close actions like db connetions or files

# with open('example.txt', 'a') as file:
#     file.write('\nHello, Context Manager!')
    # content = file.read()
    # print(content)

class CustomContextManager:
    def __enter__(self):
        print('Entering the context')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting the context')

with CustomContextManager() as manager:
    print('Inside the context')


# Entering the context
# Inside the context
# Exiting the context
