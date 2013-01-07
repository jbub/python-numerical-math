def user_input(prompt=None, default=None):
    if default:
        prompt = '{0} [{1}]: '.format(prompt, default)
    else:
        prompt = '{0}: '.format(prompt)
    input = raw_input(prompt)
    return default if default else input


def float_input(prompt=None, positive=True, default=None):
    while True:
        try:
            input = float(user_input(prompt, default))
        except ValueError:
            pass
        else:
            if (positive and input > 0.0) or not positive:
                return input


def int_input(prompt=None, positive=True, default=None):
    while True:
        try:
            input = int(user_input(prompt, default))
        except ValueError:
            pass
        else:
            if (positive and input > 0) or not positive:
                return input