"""
Glauber algorithms for the Monte Carlo method in the 2D Ising model.
"""
import sys 
import os

def magnetization(nodesNumber, lattice): 
    return 1/nodesNumber*sum([sum(row) for row in lattice])

def print_configuration(S, AM_UP, AM_DOWN):
        configuration = ""
        for row in S:
            for spin in row:
                configuration = "".join([configuration, str(spin)])
            configuration = "".join([configuration, '\n'])
        configuration = configuration.replace('-1', AM_DOWN)
        configuration = configuration.replace('1', AM_UP)
        os.system('cls')
        sys.stdout.write(configuration)
        sys.stdout.flush()

def glauberRAW(S: list[list[int]], K: int, TRED: float, BETA: float, SEED: int) -> tuple[list[list[int]], list[float]]:
    "Raw Glauber algorithm."
    import random
    from math import exp

    random.seed(SEED)

    L = len(S)                      # number of rows/columns in the lattice
    N = L*L                         # number of nodes
    J = 1/BETA/TRED                 # parameter of interaction
    
    m = [magnetization(N, S)]       # initial state
    
    # evolution
    for MCS in range(0,K):
        for iteration in range(0,N):
            ir = random.randrange(L) # index of a random row
            ic = random.randrange(L) # index of a random column

            DeltaE = 2*J*S[ir][ic]*(S[ir-1][ic] + S[ir][(ic+1)%L] + S[(ir+1)%L][ic] + S[ir][ic-1])

            if      DeltaE < 0:                                 S[ir][ic] *= -1
            elif    random.random() < 1/(1 + exp(DeltaE*BETA)): S[ir][ic] *= -1

        m.append(magnetization(N, S))

    return S, m


def glauberH(S: list[list[int]], K: int, TRED: float, H: float, BETA: float, SEED: int) -> tuple[list[list[int]], list[float]]:
    "Glauber algorithm with included external magnetic field."
    import random
    from math import exp

    random.seed(SEED)

    L = len(S)                      # number of rows/columns in the lattice
    N = L*L                         # number of nodes
    J = 1/BETA/TRED                 # parameter of interaction
    
    m = [magnetization(N, S)]       # initial state
    
    # evolution
    for MCS in range(0,K):
        for iteration in range(0,N):
            ir = random.randrange(L) # index of a random row
            ic = random.randrange(L) # index of a random column

            DeltaE = 2*J*S[ir][ic]*(S[ir-1][ic] + S[ir][(ic+1)%L] + S[(ir+1)%L][ic] + S[ir][ic-1]) + 2*H*S[ir][ic]

            if      DeltaE < 0:                                 S[ir][ic] *= -1
            elif    random.random() < 1/(1 + exp(DeltaE*BETA)): S[ir][ic] *= -1

        m.append(magnetization(N, S))

    return S, m



def glauberA(S: list[list[int]], K: int, TRED: float, BETA: float, SEED: int, AM: tuple[str, str]) -> tuple[list[list[int]], list[float]]:
    "Animated Glauber algorithm."
    import random
    from math import exp
    import sys
    import os

    random.seed(SEED)

    L = len(S)                      # number of rows/columns in the lattice
    N = L*L                         # number of nodes
    J = 1/BETA/TRED                 # parameter of interaction
    
    m = [magnetization(N, S)]       # initial state

    # resizing the window
    os.system(''.join(['MODE ', str(L), ',', str(L)]))

    AM_UP   = AM[0]     # marker of spins "up"
    AM_DOWN = AM[1]     # marker of spins "down"
    print_configuration(S, AM_UP, AM_DOWN)

    # evolution
    for MCS in range(0,K):
        for iteration in range(0,N):
            ir = random.randrange(L) # index of a random row
            ic = random.randrange(L) # index of a random column

            DeltaE = 2*J*S[ir][ic]*(S[ir-1][ic] + S[ir][(ic+1)%L] + S[(ir+1)%L][ic] + S[ir][ic-1])

            if      DeltaE < 0:                                 S[ir][ic] *= -1
            elif    random.random() < 1/(1 + exp(DeltaE*BETA)): S[ir][ic] *= -1

        m.append(magnetization(N, S))
        print_configuration(S, AM_UP, AM_DOWN)

    return S, m


def glauberHA(S: list[list[int]], L: int, K: int, TRED: float, H: float, BETA: float, SEED: int, AM: tuple[str, str]) -> tuple[list[list[int]], list[float]]:
    "Animated Glauber algorithm with external magneticc field."
    import random
    from math import exp
    import sys
    import os

    random.seed(SEED)

    L = len(S)                      # number of rows/columns in the lattice
    N = L*L                         # number of nodes
    J = 1/BETA/TRED                 # parameter of interaction
    
    m = [magnetization(N, S)]       # initial state

    # resizing the window
    os.system(''.join(['MODE ', str(L), ',', str(L)]))

    AM_UP   = AM[0]     # marker of spins "up"
    AM_DOWN = AM[1]     # marker of spins "down"
    print_configuration(S, AM_UP, AM_DOWN)

    # evolution
    for MCS in range(0,K):
        for iteration in range(0,N):
            ir = random.randrange(L) # index of a random row
            ic = random.randrange(L) # index of a random column

            DeltaE = 2*J*S[ir][ic]*(S[ir-1][ic] + S[ir][(ic+1)%L] + S[(ir+1)%L][ic] + S[ir][ic-1]) + 2*H*S[ir][ic]

            if      DeltaE < 0:                                 S[ir][ic] *= -1
            elif    random.random() < 1/(1 + exp(DeltaE*BETA)): S[ir][ic] *= -1

        m.append(magnetization(N, S))
        print_configuration(S, AM_UP, AM_DOWN)

    return S, m