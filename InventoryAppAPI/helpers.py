
def pid_is_valid(pid):
    if len(str(pid)) == 7:
        try:
            pid.isdigit()
        except TypeError:
            return False
    else:
        return False
