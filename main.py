#!/usr/bin/env python3
"""
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
    The default is 1.

-L <int>
--length <int>
    A length L=<int> of the lattice LxL in the system of spins.
    The default is 10.

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
    Turns on the visual evolution of the system. <char><char> is a pair of characters that represents spin "up" and spin "down". The total time of execution will increase. Works only on Windows OS.
    The default pair is U+0020, U+2588.

AUTHOR
Wojciech Rożek
"""
if __name__ == '__main__':
    import sys
    import init
    import random
    import os

    argv = sys.argv

    if '--help' in argv:
        print(init.DOCS)
        sys.exit()
        
    seed = init.seed_from(argv)                                         # for random trajectories
    lattice_length = init.lattice_length_from(argv)                     # length of the lattice
    red_temperature = init.reduced_temperature_from(argv)               # reduced temperature T*
    emf = init.external_magnetic_field_from(argv)                       # external magnetic field h
    interaction = init.interaction_from(argv)                           # interaction parameter
    mcss = init.mcss_from(argv)                                         # number of Monte Carlo steps
    magnetization0 = init.initial_magnetization_from(argv)              # initial value of magnetization of the system
    algorithm = init.algorithm_from(argv)                               # an algorithm for computing the Monte Carlo method
    visualization = init.visualization_markers_from(argv)               # markers for visualize evolution of the system
    save_configuration_dir = init.save_configuration_path_from(argv)    # path to save final spins configuration
    save_magnetization_dir = init.save_magnetization_path_from(argv)    # path to save magnetization

    beta = 1/interaction/red_temperature            # 1/(k_BT)

    def generate_spin(probability: float) -> int:
        "Return a spin 'up' with the given probability."
        if random.random() <= probability:
            return 1
        return -1

    # initializing a system of spins
    random.seed(seed)
    up_probability = (magnetization0 + 1)/2                                                                                     # probability of initiation a spin as "up"
    config = [[generate_spin(up_probability) for column in range(0, lattice_length)] for row in range(0, lattice_length)]       # a lattice of spins

    # general processing
    magnetization = ...
    if visualization:
        if emf == 0.0:
            from kernel import mc_v
            lattice, magnetization = mc_v(config, mcss, red_temperature, beta, algorithm, seed, visualization)
        else:
            from kernel import mc_h_v
            lattice, magnetization = mc_h_v(config, mcss, red_temperature, emf, beta, algorithm, seed, visualization)
    else:
        if emf == 0.0:
            from kernel import mc_raw
            lattice, magnetization = mc_raw(config, mcss, red_temperature, beta, algorithm, seed)
        else:
            from kernel import mc_h
            lattice, magnetization = mc_h(config, mcss, red_temperature, emf, beta, algorithm, seed)

    # saving the configuration of spins
    if save_configuration_dir:
        file_name = ''.join(['L', str(lattice_length),
                             'Tred', str(red_temperature),
                             'h', str(emf),
                             'J', str(interaction),
                             'K', str(mcss),
                             'm', str(magnetization0),
                             algorithm,
                             ' configuration'])
        file_path = "".join([save_configuration_dir, file_name, ' (1)'])
        file_name_counter = 1
        while os.path.isfile(file_path):
            file_name_counter += 1
            file_path = ''.join([save_configuration_dir, file_name, ' (', str(file_name_counter), ')'])
        with open(file_path, 'w', encoding='UTF-8') as file:
            for row in config:
                for spin in row:
                    if spin > 0:
                        file.write('1')
                    else:
                        file.write('0')
                file.write('\n')
            file.close()

    # saving the evolution of magnetization
    if save_magnetization_dir:
        file_name = ''.join(['L', str(lattice_length),
                             'Tred', str(red_temperature),
                             'h', str(emf),
                             'J', str(interaction),
                             'K', str(mcss),
                             'm', str(magnetization0),
                             algorithm,
                             ' magnetization'])
        file_path = ''.join([save_magnetization_dir, file_name, ' (1)'])
        file_name_counter = 1
        while os.path.isfile(file_path):
            file_name_counter += 1
            file_path = ''.join([save_magnetization_dir, file_name, ' (', str(file_name_counter), ')'])
        with open(file_path, 'w', encoding='UTF-8') as file:
            for m in magnetization:
                file.write(str(m) + '\n')
            file.close()
