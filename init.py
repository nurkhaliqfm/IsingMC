"""
The module provide a set of functions to initialize parameters.
"""
FLAGS =  [
        '-s', '--seed',
        '-L', '--length',
        '-T*', '--temperature-reduced',
        '-h', '--external-magnetic-field',
        '-J', '--J', '--interaction',
        '-K', '--K', '--steps',
        '-m0', '--initial-magnetization',
        '-a', '--algorithm',
        '-v', '--visualization',
        '-sc', '--save-configuration',
        '-sm', '--save-magnetization'
        ]

def get_value(argv: list[str], args: list[str]):
    """Checks if an any argument from the list Args were given in the list Argv and returns it is value or None object."""
    index = None        # index of an appropriate argument in the list argv

    for arg in args:
        try:
            index = argv.index(arg)
            break
        except ValueError:
            continue

    if index:
        value = None

        try:
            value = argv[index+1]
        except IndexError:
            return None

        if value not in FLAGS:
            return value

    return None

def seed_from(argv: list[str]) -> int:
    """Returns the given random seed form the command line."""
    args = ['-s', '--seed']     # appropriate arguments

    value = 1997        # the default value
    try:
        value = int(get_value(argv, args))
    except ValueError as exc:
        raise ValueError('seed must be an integer') from exc
    except TypeError as exc:
        for arg in args:
            if arg in argv:
                raise TypeError('seed must be not empty') from exc

    return value

def lattice_length_from(argv: list[str]) -> int:
    """Returns the given length L of the lattice of spins L x L."""
    args = ['-L', '--length']       # appropriate arguments

    value = 40
    try:
        value = int(get_value(argv, args))
    except ValueError as exc:
        raise ValueError('length L of the lattice must be an integer') from exc
    except TypeError as exc:
        for arg in args:
            if arg in argv:
                raise TypeError('length L of the lattice must be not empty') from exc

    if value <= 0:
        raise ValueError('length L of the lattice must be greater than zero')

    return value

def reduced_temperature_from(argv: list[str]) -> float:
    """Returns the given reduced temperature T*."""
    args = ['-T*', '--temperature-reduced']

    value = 1.0
    try:
        value = float(get_value(argv, args))
    except ValueError as exc:
        raise ValueError('reduced temperature T* must be a float') from exc
    except TypeError as exc:
        for arg in args:
            if arg in argv:
                raise TypeError('reduced temperature must be not empty') from exc

    if value <= 0:
        raise ValueError('reduced temperature T* must be greater than zero')

    return value

def external_magnetic_field_from(argv: list[str]) -> float:
    """Returns the given value of an external magnetic field h in the system."""
    args = ['-h', '--external-magnetic field']

    value = 0.0
    try:
        value = float(get_value(argv, args))
    except ValueError as exc:
        raise ValueError('external magnetic field h must be a float') from exc
    except TypeError as exc:
        for arg in args:
            if arg in argv:
                raise TypeError('external magnetic field h must be not empty') from exc

    return value

def interaction_from(argv: list[str]) -> float:
    """Returns the given interaction parameter J."""
    args = ['-J', '--J', '--intercation']

    value = 1.0
    try:
        value = float(get_value(argv, args))
    except ValueError as exc:
        raise ValueError('parameter of interaction J must be a float') from exc
    except TypeError as exc:
        for arg in args:
            if arg in argv:
                raise TypeError('parameter of interaction J must be not empty') from exc

    return value

def mcss_from(argv: list[str]) -> int:
    """Returns the given number of MCSs."""
    args = ['-K', '--K', '--steps']

    value = 400
    try:
        value = int(get_value(argv, args))
    except ValueError as exc:
        raise ValueError('number of MCSs K must be an integer') from exc
    except TypeError as exc:
        for arg in args:
            if arg in argv:
                raise TypeError('number of MCSs K must be not empty') from exc

    if value < 0:
        raise ValueError('number of MCSs K must be greater than zero')

    return value

def initial_magnetization_from(argv: list[str]) -> str:
    """Returns the given value of initial magnetization in the system."""
    args = ['-m0', '--initial-magnetization']

    value = 0.0
    try:
        value = float(get_value(argv, args))
    except ValueError as exc:
        raise ValueError('initial magnetization m0 must be float') from exc
    except TypeError as exc:
        for arg in args:
            if arg in argv:
                raise TypeError('initial magnetization m0 must be not empty') from exc

    if value < -1.0 or value > 1.0:
        raise ValueError('initial magnetization m0 should be in [-1,1]')

    return value

def algorithm_from(argv: list[str]) -> str:
    """Returns the given name of choosen algorithm."""
    args = ['-alg', '--algorithm']

    value = ...
    try:
        value = get_value(argv, args)
    except TypeError as exc:
        for arg in args:
            if arg in argv:
                raise TypeError('am algorithm for the Monte Carlo method must be not empty') from exc

    if not value:
        return 'glauber'
    if value in ['metropolis', 'glauber']:
        return value
    raise ValueError('the choosen algorithm must be \'metropolis\' or \'glauber\'')

def visualization_markers_from(argv: list[str]) -> tuple[str]:
    """This function optionally returns the given markers for displaying an visualization of evolution in the system."""
    args = ['-v', '--visualization']

    value = get_value(argv, args)
    if value:
        if len(value) == 1:
            return value, '\u2588'
        return value[0], value[1]
    for arg in args:
        if arg in argv:
            return ' ', '\u2588'

    return value

def save_configuration_path_from(argv: list[str]) -> str:
    """Returns the given path to save the final state of the system."""
    args = ['-sc', '--save-configuration']

    value = get_value(argv, args)
    if value is not None:
        return value + '\\'

    for arg in args:
        if arg in argv:
            return '.\\'

    return value

def save_magnetization_path_from(argv: list[str]) -> str:
    """Returns the given path to save the evolution of magnetization in the system."""
    args = ['-sm', '--save-magnetization']

    value = get_value(argv, args)
    if value is not None:
        return value + '\\'

    for arg in args:
        if arg in argv:
            return '.\\'

    return value

DOCS = """
ABOUT
The program provide Monte Carlo simulations of 2D Ising model.

EVOKE
py main.py [-a|--algorithm <string>] [-h|--external-magnetic-field <float>] [--help] [-J|--J|--interaction <float>] [-K|--K|--steps <int>] [-L|--length <int>] [-m|-m0|--initial-magnetization <float>] [-s|--seed <int>] [-sc|--save-configuration [<path>]] [-sm|--save-magnetization [<path>]] [-T*|--temperature-reduced <float>] [-v|--visualization [<char><char>]]

DESCRIPTION
-a <string>
--algorithm <string>
    An algorithm used by the Monte Carlo method to computing evolution of the system. Avaliable algorithms:
        <string> == 'metropolis'
        <string> == 'glauber'
    The default is 'glauber'.

-h <float>
--external-magnetic-field <float>
    External homogenious magnetic field h = <float> of the system.
    The default is 0.0.

--help
    Prints that text, without executing the program.

-J <float>
--J <float>
--interaction <float>
    Interaction J = <float> between a pair of spins.
    The default is 1.0.

-K <int>
--K <int>
--steps <int>
    Number of desired MCSs (iterations) K == <int>.
    The default is 400.

-L <int>
--length <int>
    A length L=<int> of the lattice LxL in the system of spins.
    The default is 40.

-m0 <float>
--initial-magnetization <float>
    Initiated magnetization m = <float>.
    The default is 0.0

-s <int>
--seed <int>
    A seed <int> for the random number generator in module "random".
    The default is 1997.

-sc [<path>]
--save-configuration [<path>]
    At the end of the simulation the configuration of spins S[ij] will be saved in a given directory <path>.
    The dafault is "./".

-sm [<path>]
--save-magnetization [<path>]
    At the end of the simulation the time-dependent evolution of magnetization m(t) [MCS] of the system will be saved in a given directory <path>. 
    The dafault is "./" (the path of this module).

-T* <float>
--temperature-reduced <float>
    Reduced temperature T* = <float> of the system, where T*=1/(J x Beta).
    The default is 1.0.

-v [<char><char>]
--visualization [<char><char>]
    Turns on the visual evolution of the system. <char><char> is a pair of characters that represents spin "up" and spin "down". The total time of execution will increase.
    The default pair is U+0020, U+2588.
"""