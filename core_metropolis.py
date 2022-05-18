"""Metropolis algorithms for the Monte Carlo method in the 2D Ising model."""
from math import exp
import random

import utils


def mc_raw(configuration: list[list[int]],
           monte_carlo_steps: int,
           reduced_temperature: float,
           beta: float,
           seed: int
          ) -> tuple[list[list[int]], list[float]]:
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

    mag = [utils.magnetization(nodes_number, configuration)]      # initial state of magnetization

    # evolution
    for mcs in range(0, monte_carlo_steps):
        for iteration in range(0, nodes_number):
            ir = random.randrange(lattice_length)       # index of a random row
            ic = random.randrange(lattice_length)       # index of a random column

            delta = 2*interaction_parameter*configuration[ir][ic]\
                    *(configuration[ir-1][ic] + configuration[ir][(ic+1)%lattice_length]\
                    + configuration[(ir+1)%lattice_length][ic] + configuration[ir][ic-1])

            if delta < 0:
                configuration[ir][ic] *= -1
            elif random.random() < exp(-delta*beta):
                configuration[ir][ic] *= -1

        mag.append(utils.magnetization(nodes_number, configuration))

    return configuration, mag


def mc_h(configuration: list[list[int]],
         monte_carlo_steps: int,
         reduced_temperature: float,
         external_magnetic_field: float,
         beta: float,
         seed: int
        ) -> tuple[list[list[int]], list[float]]:
    """
    Monte Carlo method with incorporated external magnetic field.

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

    mag = [utils.magnetization(nodes_number, configuration)]      # initial state of magnetization
    
    # evolution
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
            elif random.random() < exp(-delta*beta):
                configuration[ir][ic] *= -1

        mag.append(utils.magnetization(nodes_number, configuration))

    return configuration, mag


def mc_v(configuration: list[list[int]],
         monte_carlo_steps: int,
         reduced_temperature: float,
         beta: float,
         seed: int,
         visualization_markers: tuple[str, str]
        ) -> tuple[list[list[int]], list[float]]:
    """
    Monte Carlo method on the Glauber algorithm with visualization.

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
    visualization_markers
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

    mag = [utils.magnetization(nodes_number, configuration)]      # initial state of magnetization

    am_up   = visualization_markers[0]     # marker of spins "up"
    am_down = visualization_markers[1]     # marker of spins "down"

    print_function = utils.chose_print_function(lattice_length)
    print_function(configuration, am_up, am_down)

    # evolution
    for mcs in range(0, monte_carlo_steps):
        for iteration in range(0, nodes_number):
            ir = random.randrange(lattice_length)       # index of a random row
            ic = random.randrange(lattice_length)       # index of a random column

            delta = 2*interaction_parameter*configuration[ir][ic]\
                    *(configuration[ir-1][ic] + configuration[ir][(ic+1)%lattice_length]\
                    + configuration[(ir+1)%lattice_length][ic] + configuration[ir][ic-1])

            if delta < 0:
                configuration[ir][ic] *= -1
            elif random.random() < exp(-delta*beta):
                configuration[ir][ic] *= -1

        mag.append(utils.magnetization(nodes_number, configuration))
        print_function(configuration, am_up, am_down)

    return configuration, mag


def mc_h_v(configuration: list[list[int]],
           monte_carlo_steps: int,
           reduced_temperature: float,
           external_magnetic_field: float,
           beta: float,
           seed: int,
           visualization_markers: tuple[str, str]
          ) -> tuple[list[list[int]], list[float]]:
    """
    Monte Carlo method with visualization and external magnetic.

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
    visualization_markers
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
    
    mag = [utils.magnetization(nodes_number, configuration)]      # initial state of magnetization

    am_up   = visualization_markers[0]     # marker of spins "up"
    am_down = visualization_markers[1]     # marker of spins "down"

    print_function = utils.chose_print_function(lattice_length)
    print_function(configuration, am_up, am_down)

    # evolution
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
            elif random.random() < exp(-delta*beta):
                configuration[ir][ic] *= -1

        mag.append(utils.magnetization(nodes_number, configuration))
        print_function(configuration, am_up, am_down)

    return configuration, mag
