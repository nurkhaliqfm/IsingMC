import platform

def kernel(S: list[list[int]], 
           L: int, 
           K: int, 
           TRED: float, 
           H: float, 
           BETA: float, 
           SEED: int, 
           ANIMATION: tuple[str, str],
           ALGORITHM: str
          ) -> tuple[list[list[int]], list]:

    match platform.system():
        case 'Windows': 
            match ALGORITHM:
                # case 'metropolis' if H == 0 and not ANIMATION:  from metropolis import metropolisRAW    as evolution
                # case 'metropolis' if H != 0 and not ANIMATION:  from metropolis import metropolisH      as evolution
                # case 'metropolis' if H == 0 and     ANIMATION:  from metropolis import metropolisA      as evolution
                # case 'metropolis' if H != 0 and     ANIMATION:  from metropolis import metropolisHA     as evolution
                case 'glauber' if H == 0 and not ANIMATION:  
                    from glauber import glauberRAW
                    return glauberRAW(S, K, TRED, BETA, SEED)
                case 'glauber' if H != 0 and not ANIMATION:  
                    from glauber import glauberH
                    return glauberH(S, K, TRED, H, BETA, SEED)
                case 'glauber' if H == 0 and ANIMATION:  
                    from glauber import glauberA
                    return glauberA(S, K, TRED, BETA, SEED, ANIMATION)
                case 'glauber' if H != 0 and ANIMATION:  
                    from glauber import glauberHA
                    return glauberHA(S, L, K, TRED, H, BETA, SEED, ANIMATION)
        case _: pass
    