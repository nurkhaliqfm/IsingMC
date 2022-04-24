"""
The module provides a set of functions for initiation of constants and to control the program.
"""
ARGS =  [
        '-s', 
        '--seed',
        '-L',
        '--length',
        '-T*',
        '-h',
        '--external-magnetic-field',
        '--temperature-reduced',
        '-J',
        '--J',
        '-K',
        '--K',
        '-i',
        '--initial-state',
        '-alg',
        '--algorithm',
        '-a',
        '--animation',
        '-ss',
        '--save-system',
        '-sm',
        '--save-magnetization'
        ]

def get_value(argv: list[str], args: list[str]):
    index = None
    for arg in args:
        try:                
            index = argv.index(arg)
            break
        except ValueError:  
            continue
        
    if index:
        value = None

        try:                value = argv[index+1]
        except IndexError:  return None

        if value not in ARGS:   return value
        else:                   return None
    else: 
        return None

def seed(argv: list[str]) -> int:
    "Return a given seed form the command line."
    args = ['-s', '--seed']
    value = 1997
    try:                
        value = int(get_value(argv, args))
    except ValueError:  
        raise ValueError('seed must be an integer')
    except TypeError:  
        for arg in args:
            if arg in argv:
                raise TypeError('seed must be not empty')
    return value

def length(argv: list[str]) -> int:
    "Return a given length L of the lattice of spins L x L."
    args = ['-L', '--length']
    value = 10
    try:                
        value = int(get_value(argv, args))
    except ValueError:  
        raise ValueError('length L of the lattice must be an integer')
    except TypeError:  
        for arg in args:
            if arg in argv:
                raise TypeError('length L of the lattice must be not empty')
    if value <= 0:
        raise ValueError('length L of the lattice must be greater than zero')
    return value

def reduced_temperature(argv: list[str]) -> float:
    "Returns a given reduced temperature T*."
    args = ['-T*', '--temperature-reduced']
    value = 1.0
    try:                
        value = float(get_value(argv, args))
    except ValueError:  
        raise ValueError('reduced temperature T* must be a float')
    except TypeError:  
        for arg in args:
            if arg in argv:
                raise TypeError('reduced temperature must be not empty')
    if value <= 0:
        raise ValueError('reduced temperature T* must be greater than zero')
    return value
    
def external_magnetic_field(argv: list[str]) -> float:
    "Returns a given value of a external magnetic field h in he system."
    args = ['-h', '--external-magnetic field']
    value = 0.0
    try:                
        value = float(get_value(argv, args))
    except ValueError:  
        raise ValueError('external magnetic field h must be a float')
    except TypeError:  
        for arg in args:
            if arg in argv:
                raise TypeError('external magnetic field h must be not empty')
    return value

def j(argv: list[str]) -> float:
    "Returns a given interaction parameter J."
    args = ['-J', '--J', '--intercation']
    value = 1.0
    try:                
        value = float(get_value(argv, args))
    except ValueError:  
        raise ValueError('parameter of interaction J must be a float')
    except TypeError:  
        for arg in args:
            if arg in argv:
                raise TypeError('parameter of interaction J must be not empty')
    return value

def k(argv: list[str]) -> int:
    "Returns a given number of MCSs."
    args = ['-K', '--K', '--steps']
    value = 1
    try:                
        value = int(get_value(argv, args))
    except ValueError:  
        raise ValueError('number of MCSs K must be an integer')
    except TypeError:  
        for arg in args:
            if arg in argv:
                raise TypeError('number of MCSs K must be not empty')
    if value < 0:
        raise ValueError('number of MCSs K must be greater than zero')
    return value

def initial_magnetization(argv: list[str]) -> str:
    "Returns a given value of the ititial state of the system."
    args = ['-m0', '--initial-magnetization']
    value = 0.0
    try:                
        value = float(get_value(argv, args))
    except ValueError:  
        raise ValueError('initial magnetization m0 must be float')
    except TypeError:  
        for arg in args:
            if arg in argv:
                raise TypeError('initial magnetization m0 must be not empty')
    if value < -1.0 or value > 1.0:
        raise ValueError('initial magnetization m0 should be in [-1,1]')
    return value

def algorithm(argv: list[str]) -> str:
    "Returns a given name of choosen algorithm."
    args = ['-alg', '--algorithm']
    value = ...
    try:                
        value = get_value(argv, args)
    except TypeError:  
        for arg in args:
            if arg in argv:
                raise TypeError('am algorithm for the Monte Carlo method must be not empty')
    if value is None:                           return 'glauber'
    elif value in ['metropolis', 'glauber']:    return value
    else:                                       raise ValueError('the choosen algorithm must be \'metropolis\' or \'glauber\'')


def animation_markers(argv: list[str]) -> tuple[str]:
    "This function optionally returns a given markers for displaying the animation of evolution of the system during the execution of program."
    args = ['-a', '--animation']
    value = get_value(argv, args)
    if value is not None: 
        if      len(value) == 1:  return value, u'\u2588'
        else:                     return value[0], value[1]
    else:
        for arg in args:
            if arg in argv:
                return ' ', u'\u2588'
    return value

def save_system_path(argv: list[str]) -> str:
    "Returns a given path to save the final state of the system."    
    args = ['-ss', '--save-system']
    value = get_value(argv, args)
    if value is not None: 
        return value + '\\'
    else:
        for arg in args:
            if arg in argv:
                return '.\\'
    return value

def save_magnetization_path(argv: list[str]) -> str:
    "Returns a given path to save the evolution of magnetization in the system."   
    args = ['-sm', '--save-magnetization']
    value = get_value(argv, args)
    if value is not None: 
        return value + '\\'
    else:
        for arg in args:
            if arg in argv:
                return '.\\'
    return value


