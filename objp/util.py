pyref = object()

def objcname(name):
    def decorator(func):
        func.objcname = name
        return func
    return decorator

def dontwrap(func):
    func.dontwrap = True
    return func