def metropolisRAW(S: list[list[int]], L: int, K: int, TRED: float, H: float, BETA: float, SEED: int) -> tuple[list[list[int]], list]:
    "Metropolis algorithm"
    import random
    from math import exp
    random.seed(SEED)

    N = L*L # number of nodes
    J = 1/BETA/TRED # parameter of interaction
    magnetization = lambda nodesNumber, lattice: 1/nodesNumber*sum([sum(row) for row in lattice])

    m = [magnetization(N, S)]
    if H == 0.0:
        for MCS in range(0,K):
            for iteration in range(0,N):
                ir = random.randrange(L) # index of a random row
                ic = random.randrange(L) # index of a random column

                DeltaE = 2*J*S[ir][ic]*(S[ir-1][ic] + S[ir][(ic+1)%L] + S[(ir+1)%L][ic] + S[ir][ic-1])

                if      DeltaE < 0:                             S[ir][ic] *= -1
                elif    random.random() < exp(-DeltaE*BETA):    S[ir][ic] *= -1

            m.append(magnetization(N, S))
    if H != 0.0:
        for MCS in range(0,K):
            for iteration in range(0,N):
                ir = random.randrange(L) # index of a random row
                ic = random.randrange(L) # index of a random column

                DeltaE = 2*J*S[ir][ic]*(S[ir-1][ic] + S[ir][(ic+1)%L] + S[(ir+1)%L][ic] + S[ir][ic-1]) + 2*H*S[ir][ic]

                if      DeltaE < 0:                             S[ir][ic] *= -1
                elif    random.random() < exp(-DeltaE*BETA):    S[ir][ic] *= -1

            m.append(magnetization(N, S))
    return S, m

