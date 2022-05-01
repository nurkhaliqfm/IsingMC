
<h1 align="center"><strong>Monte Carlo simulations of an Ising Model</strong></h>

</br>
</br>

![](IsingMCgif.gif)

## ABOUT

The program provide Monte Carlo simulations of 2D Ising model.

## CLI

    py main.py [-a|--algorithm <string>] [-h|--external-magnetic-field <float>] [--help] [-J|--J|--interaction <float>] [-K|--K|--steps <int>] [-L|--length <int>] [-m|-m0|--initial-magnetization <float>] [-s|--seed <int>] [-sc|--save-configuration [<path>]] [-sm|--save-magnetization [<path>]] [-T*|--temperature-reduced <float>] [-v|--visualization [<char><char>]]


## DESCRIPTION

`-a <string>`</br>
`--algorithm <string>`</br>
<div>
  <ul>
    An algorithm used by the Monte Carlo method to computing evolution of the system. Avaliable algorithms:</br>
        <div>
        <ul>
            <code>&lt;string&gt;</code>=='metropolis'</br>
            <code>&lt;string&gt;</code>=='glauber'
        </ul>
        </div>
    The default is 'glauber'.
  </ul>
</div>
</br>

`-h <float>`</br>
`--external-magnetic-field <float>`</br>
<div>
  <ul>
    External homogenious magnetic field h=<code>&lt;float&gt;</code> of the system.</br>
    The default is 0.0.
  </ul>
</div>
</br>

`--help`</br>
<div>
  <ul>
    Prints that text, without executing the program.
  </ul>
</div>

`-J <float>`</br>
`--J <float>`</br>
`--interaction <float>`</br>
<div>
  <ul>
    Interaction J=<code>&lt;float&gt;</code> between a pair of spins.</br>
    The default is 1.0.
  </ul>
</div>
</br>

`-K <int>`</br>
`--K <int>`</br>
`--steps <int>`</br>
<div>
  <ul>
    Number of desired MCSs (iterations) K==<code>&lt;int&gt;</code>.</br>
    The default is 1.
  </ul>
</div>
</br>

`-L <int>`</br>
`--length <int>`</br>
<div>
  <ul>
    A length L=<code>&lt;int&gt;</code> of the lattice LxL in the system of spins.</br>
    The default is 10.
  </ul>
</div>
</br>

`-m0 <float>`</br>
`--initial-magnetization <float>`</br>
<div>
  <ul>
    Initiated magnetization m(t=0)=<code>&lt;float&gt;</code>.</br>
    The default is 0.0.
  </ul>
</div>
</br>

`-s <int>`</br>
`--seed <int>`</br>
<div>
  <ul>
    A seed <code>&lt;int&gt;</code> for the random number generator in module "random".</br>
    The default is 1997.
  </ul>
</div>
</br>

`-sc [<path>]`</br>
`--save-configuration [<path>]`</br>
<div>
  <ul>
    At the end of the simulation the configuration of spins S[ij] will be saved in a given directory <code>&lt;path&gt;</code>.</br>
    The dafault is "./".
  </ul>
</div>
</br>

`-sm [<path>]`</br>
`--save-magnetization [<path>]`</br>
<div>
  <ul>
    At the end of the simulation the time-dependent evolution of magnetization m(t) [MCS] of the system will be saved in a given directory <code>&lt;path&gt;</code>.</br>
    The dafault is "./" (the path of this module).
  </ul>
</div>

`-T* <float>`</br>
`--temperature-reduced <float>`</br>
<div>
  <ul>
    Reduced temperature T*=<code>&lt;float&gt;</code> of the system, where T*=1/(J x Beta).</br>
    The default is 1.0.
  </ul>
</div>
</br>

`-v [<char><char>]`</br>
`--visualization [<char><char>]`</br>
<div>
  <ul>
    Turns on the visual evolution of the system. <code>&lt;char&gt;&lt;char&gt;</code> is a pair of characters that represents spin "up" and spin "down". The total time of execution will increase.</br>
    The default pair is U+0020, U+2588.
  </ul>
</div>
</br>
    
## REQUIREMENTS

    Python >= 3.10.2

## EXAMPLES

    py main.py -L 40 -T* 2.26 -v -a "metropolis"
    py main.py -L 30 -m0 1.0 -sc
    py main.py --seed 23 -K 3000 -sm "./data3/"