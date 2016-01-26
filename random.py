import random
import string

def gen_random_id(size=6, chars=string.ascii_lowercase + string.digits):
    '''
    generate a string using char + digit
    ref: http://stackoverflow.com/a/2257449/4328963
    '''
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
