"""
ABOUT
This program provides Monte Carlo simulations of 2D Ising model.

EVOKE
py IsingMC.py [-s|--seed <int>] [-l|--length <int>] [-t|--temperature-reduced <float>] [-j|--j <float>] [-k|--k <int>] [-i|--initial-state <int>] [-alg|--algorithm <string>] [-a|--animation [<char><char>]] [-ss|--save-system [<path>]] [-sm|--save-magnetization [<path>]]

DESCRIPTION
-s <int>
--seed <int>
    A seed <int> for the random number generator in module "random".
    The default is 1997.

-L <int>
--length <int>
    A length L=<int> of the lattice LxL in the system of spins.
    The default is 10.

-T* <float>
--temperature-reduced <float>
    Reduced temperature T* = <float> of the system, where T*=1/(J x Beta).
    The default is 1.0.

-h <float>
--external-magnetic-field <float>
    External homogenious magnetic field h = <float> of the system.
    The default is 0.0.

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

-m0 <float>
--initial-magnetization <float>
    Initiated magnetization m = <float>.
    The default is 0.0

-alg <string> 
--algorithm <string>
    An algorithm used by the Monte Carlo method to computing evolution of the system. Avaliable algorithms:
        <string> == 'metropolis'
        <string> == 'glauberg'
    The default is 'glauber'.

-a [<char><char>]
--animation [<char><char>]
    Turns on the visual evolution of the system. <char><char> is a pair of characters that represents spin "up" and spin "down". The total time of execution will increase. Works only on Windows OS.
    The default pair is U+0020, U+2588.

-ss [<path>]
--save-system [<path>]
    At the end of the simulation the configuration of spins S[ij] will be saved in a given directory <path>.
    The dafault is "./".

-sm [<path>]
--save-magnetization [<path>]
    At the end of the simulation the time-dependent evolution of magnetization m(t) [MCS] of the system will be saved in a given directory <path>. 
    The dafault is "./" (the path of this module).

AUTHOR
Wojciech Rożek
"""
if __name__ == '__main__':
    import sys
    import init
    import core
    import random
    import os

    ARGV = sys.argv

    SEED = init.seed(ARGV)  # for random trajectories
    L = init.length(ARGV)   # length of the lattice
    TRED = init.reduced_temperature(ARGV)    # reduced temperature T*
    H = init.external_magnetic_field(ARGV)    # external magnetic field h
    J = init.j(ARGV)    # interaction parameter
    K = init.k(ARGV)    # number of MCS
    M0 = init.initial_magnetization(ARGV)     # mod of the initial state od the system
    ALGORITHM = init.algorithm(ARGV)    # an algorithm for computing the Monte Carlo method
    ANIMATION = init.animation_markers(ARGV)     # animation markers
    SAVE_DIR_SYSTEM = init.save_system_path(ARGV)     # a path to save lattice
    SAVE_DIR_MAGNETIZATION = init.save_magnetization_path(ARGV)   # a path to save magnetization

    BETA = 1/J/TRED     # 1/(k_BT)

    def generate_spin(p: float) -> int:
        "Return a spin 'up' with the probability p."
        if random.random() <= p:    return 1
        else:                       return -1

    # initializing a system of spins
    random.seed(SEED)
    p = (M0 + 1)/2   # probability of initiation of a "up" spin
    lattice = [[generate_spin(p) for column in range(0,L)] for row in range(0,L)]

    # general processing
    lattice, magnetization = core.kernel(lattice, L, K, TRED, H, BETA, SEED, ANIMATION, ALGORITHM)

    # saving the configuration of spins 
    if SAVE_DIR_SYSTEM:
        FILE_NAME = ''.join(['L', str(L),
                              'Tred', str(TRED),
                              'h', str(H),
                              'J', str(J),
                              'K', str(K),
                              'm', str(M0),
                              ALGORITHM,
                              ' lattice'])
        file_path = SAVE_DIR_SYSTEM + FILE_NAME + ' (1)'
        file_counter = 1
        while os.path.isfile(file_path): 
            file_counter += 1
            file_path = ''.join([SAVE_DIR_SYSTEM, FILE_NAME, ' (', str(file_counter), ')'])
        file = open(file_path, "w")
        for row in lattice:
            for spin in row:
                if spin > 0:    file.write('1')
                else:           file.write('0')
            file.write('\n')
        file.close()

    # saving the evolution of magnetization
    if SAVE_DIR_MAGNETIZATION:
        FILE_NAME = ''.join(['L', str(L),
                              'Tred', str(TRED),
                              'h', str(H),
                              'J', str(J),
                              'K', str(K),
                              'm', str(M0),
                              ALGORITHM,
                              ' magnetization'])
        file_path = ''.join([SAVE_DIR_MAGNETIZATION, FILE_NAME, ' (1)'])
        file_counter = 1
        while os.path.isfile(file_path): 
            file_counter += 1
            file_path = ''.join([SAVE_DIR_MAGNETIZATION, FILE_NAME, ' (', str(file_counter), ')'])
        file = open(file_path, "w")
        for m in magnetization:
            file.write(str(m) + '\n')
        file.close()