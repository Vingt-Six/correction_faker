import django
django.setup()

from employee.seed import run

if __name__ == '__main__':
    run()