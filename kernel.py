"""
Kernel algorithms for the Monte Carlo method in the 2D Ising model.
"""
import os
import random
from platform import system as pl_sys
from math import exp
from typing import Callable


def magnetization(number_nodes: int, lattice: list[list[int]]) -> float:
    "Returns magnetization of a system."
    return 1/number_nodes*sum([sum(row) for row in lattice])

def set_condition(algorithm: str) -> Callable[[float, float], float]:
    """
    Returns a respectiv conditional function.

    ### Parameters
    algorithm
    str
        Conditional function. "glauber" or "metropolis".

    ### Returns
    FunctionType
        Choosen function.
    """
    match algorithm:
        case 'glauber':
            return lambda x, y: 1/(1 + exp(x*y))
        case 'metropolis':
            return lambda x, y: exp(-x*y)

def chose_print_function(lattice_length: int) -> Callable[[list[list[int]], str, str], None]:
    "Returns an essential function for displaying the animation."

    match pl_sys():
        case 'Windows':
            os.system(''.join(['MODE ', str(lattice_length), ',', str(lattice_length)]))  # resizing the window
            return print_configuration_powershell
        case 'Linux':
            os.system(''.join(['resize -s ', str(lattice_length), ' ', str(lattice_length)]))  # resizing the window
            return print_configuration_bash
        case _:
            return print_configuration_empty

def print_configuration_powershell(configuration_spins: list[list[int]], marker_up: str, marker_down: str) -> None:
    "Prints given configuration of spins."
    configuration = ""
    for row in configuration_spins:
        for spin in row:
            configuration = "".join([configuration, str(spin)])
        configuration = "".join([configuration, '\n'])
    configuration = configuration.replace('-1', marker_down)
    configuration = configuration.replace('1', marker_up)
    os.system('cls')
    print(configuration)

def print_configuration_bash(configuration_spins: list[list[int]], marker_up: str, marker_down: str) -> None:
    "Prints given configuration of spins."
    configuration = ""
    for row in configuration_spins:
        for spin in row:
            configuration = "".join([configuration, str(spin)])
        configuration = "".join([configuration, '\n'])
    configuration = configuration.replace('-1', marker_down)
    configuration = configuration.replace('1', marker_up)
    os.system('clear')
    print(configuration)

def print_configuration_empty() -> None:
    "An empty function."

def mc_raw(configuration: list[list[int]], monte_carlo_steps: int, reduced_temperature: float, beta: float, algorithm: str, seed: int) -> tuple[list[list[int]], list[float]]:
    """
    A raw Monte Carlo method.

    ### Parameters
    configuration
    list[list[int]]
        A lattice-wise system of spins.
    monte_carlo_steps
    int
        Number of iterations.
    reduced_temperature
    float
        J*T/beta - thermodynamic parameter.
    beta
    float
        1/kT - thermodynamic parameter.
    algorithm
    str
        "glauber" or "metropolis".
    seed
    int
        For generatng random numbers.


    ### Returns
    list[list[int]]
        The final configuration.
    list[float]
        Evolution of magnetization.
    """
    random.seed(seed)

    lattice_length = len(configuration)                     # number of rows and columns in the lattice
    nodes_number = lattice_length*lattice_length            # number of nodes
    interaction_parameter = 1/beta/reduced_temperature      # parameter of interaction

    mag = [magnetization(nodes_number, configuration)]      # initial state of magnetization

    # evolution
    condition = set_condition(algorithm)
    for mcs in range(0, monte_carlo_steps):
        for iteration in range(0, nodes_number):
            ir = random.randrange(lattice_length)       # index of a random row
            ic = random.randrange(lattice_length)       # index of a random column

            delta = 2*interaction_parameter*configuration[ir][ic]\
                    *(configuration[ir-1][ic] + configuration[ir][(ic+1)%lattice_length]\
                    + configuration[(ir+1)%lattice_length][ic] + configuration[ir][ic-1])

            if delta < 0:
                configuration[ir][ic] *= -1
            elif random.random() < condition(delta, beta):
                configuration[ir][ic] *= -1

        mag.append(magnetization(nodes_number, configuration))

    return configuration, mag


def mc_h(configuration: list[list[int]], monte_carlo_steps: int, reduced_temperature: float, external_magnetic_field: float, beta: float, algorithm: str, seed: int) -> tuple[list[list[int]], list[float]]:
    """
    A Monte Carlo method with incorporated external magnetic field.

    ### Parameters
    configuration
    list[list[int]]
        A lattice-wise system of spins.
    monte_carlo_steps
    int
        Number of iterations.
    reduced_temperature
    float
        J*T/beta - thermodynamic parameter.
    external_magnetic_field
    float
        Influence on energy change. Incorporated member + 2*h*Sij.
    beta
    float
        1/kT - thermodynamic parameter.
    algorithm
    str
        "glauber" or "metropolis".
    seed
    int
        For generatng random numbers.

    ### Returns
    list[list[int]]
        The final configuration.
    list[float]
        Evolution of magnetization.
    """
    random.seed(seed)

    lattice_length = len(configuration)                     # number of rows and columns in the lattice
    nodes_number = lattice_length*lattice_length            # number of nodes
    interaction_parameter = 1/beta/reduced_temperature      # parameter of interaction
    
    mag = [magnetization(nodes_number, configuration)]      # initial state of magnetization
    
    # evolution
    condition = set_condition(algorithm)
    for mcs in range(0, monte_carlo_steps):
        for iteration in range(0, nodes_number):
            ir = random.randrange(lattice_length)       # index of a random row
            ic = random.randrange(lattice_length)       # index of a random column

            delta = 2*interaction_parameter*configuration[ir][ic]\
                    *(configuration[ir-1][ic] + configuration[ir][(ic+1)%lattice_length]\
                    + configuration[(ir+1)%lattice_length][ic] + configuration[ir][ic-1])\
                    + 2*external_magnetic_field*configuration[ir][ic]

            if delta < 0:
                configuration[ir][ic] *= -1
            elif random.random() < condition(delta, beta):
                configuration[ir][ic] *= -1

        mag.append(magnetization(nodes_number, configuration))

    return configuration, mag

def mc_a(configuration: list[list[int]], monte_carlo_steps: int, reduced_temperature: float, beta: float, algorithm: str, seed: int, animation_markers: tuple[str, str]) -> tuple[list[list[int]], list[float]]:
    """
    A Monte Carlo method on the Glauber algorithm with animation.

    ### Parameters
    configuration
    list[list[int]]
        A lattice-wise system of spins.
    monte_carlo_steps
    int
        Number of iterations.
    reduced_temperature
    float
        J*T/beta - thermodynamic parameter.
    beta
    float
        1/kT - thermodynamic parameter.
    algorithm
    str
        "glauber" or "metropolis".
    seed
    int
        For generatng random numbers.
    animation_markers
    tuple[str, str]
        A pair of markers used for denote "up" spins and "down" spins.

    ### Returns
    list[list[int]]
        The final configuration.
    list[float]
        Evolution of magnetization.
    """
    random.seed(seed)

    lattice_length = len(configuration)                     # number of rows and columns in the lattice
    nodes_number = lattice_length*lattice_length            # number of nodes
    interaction_parameter = 1/beta/reduced_temperature      # parameter of interaction

    mag = [magnetization(nodes_number, configuration)]      # initial state of magnetization

    am_up   = animation_markers[0]     # marker of spins "up"
    am_down = animation_markers[1]     # marker of spins "down"

    print_function = chose_print_function(lattice_length)
    print_function(configuration, am_up, am_down)

    # evolution
    condition = set_condition(algorithm)
    for mcs in range(0, monte_carlo_steps):
        for iteration in range(0, nodes_number):
            ir = random.randrange(lattice_length)       # index of a random row
            ic = random.randrange(lattice_length)       # index of a random column

            delta = 2*interaction_parameter*configuration[ir][ic]\
                    *(configuration[ir-1][ic] + configuration[ir][(ic+1)%lattice_length]\
                    + configuration[(ir+1)%lattice_length][ic] + configuration[ir][ic-1])

            if delta < 0:
                configuration[ir][ic] *= -1
            elif random.random() < condition(delta, beta):
                configuration[ir][ic] *= -1

        mag.append(magnetization(nodes_number, configuration))
        print_function(configuration, am_up, am_down)

    return configuration, mag  

def mc_h_a(configuration: list[list[int]], monte_carlo_steps: int, reduced_temperature: float, external_magnetic_field: float, beta: float, algorithm: str, seed: int, animation_markers: tuple[str, str]) -> tuple[list[list[int]], list[float]]:
    """
    A Monte Carlo method with animation and external magnetic.

    ### Parameters
    configuration
    list[list[int]]
        A lattice-wise system of spins.
    monte_carlo_steps
    int
        Number of iterations.
    reduced_temperature
    float
        J*T/beta - thermodynamic parameter.
    external_magnetic_field
    float
        Influence on energy change. Incorporated member + 2*h*Sij.
    beta
    float
        1/kT - thermodynamic parameter.
    algorithm
    str
        "glauber" or "metropolis".
    seed
    int
        For generatng random numbers.
    animation_markers
    tuple[str, str]
        A pair of markers used for denote "up" spins and "down" spins.

    ### Returns
    list[list[int]]
        The final configuration.
    list[float]
        Evolution of magnetization.
    """
    random.seed(seed)

    lattice_length = len(configuration)                     # number of rows and columns in the lattice
    nodes_number = lattice_length*lattice_length            # number of nodes
    interaction_parameter = 1/beta/reduced_temperature      # parameter of interaction
    
    mag = [magnetization(nodes_number, configuration)]      # initial state of magnetization

    am_up   = animation_markers[0]     # marker of spins "up"
    am_down = animation_markers[1]     # marker of spins "down"

    print_function = chose_print_function(lattice_length)
    print_function(configuration, am_up, am_down)

    # evolution
    condition = set_condition(algorithm)
    for mcs in range(0, monte_carlo_steps):
        for iteration in range(0, nodes_number):
            ir = random.randrange(lattice_length)       # index of a random row
            ic = random.randrange(lattice_length)       # index of a random column

            delta = 2*interaction_parameter*configuration[ir][ic]\
                    *(configuration[ir-1][ic] + configuration[ir][(ic+1)%lattice_length]\
                    + configuration[(ir+1)%lattice_length][ic] + configuration[ir][ic-1])\
                    + 2*external_magnetic_field*configuration[ir][ic]

            if delta < 0:
                configuration[ir][ic] *= -1
            elif random.random() < condition(delta, beta):
                configuration[ir][ic] *= -1

        mag.append(magnetization(nodes_number, configuration))
        print_function(configuration, am_up, am_down)

    return configuration, mag