
<h1 align="center"><strong>Monte Carlo simulations of the Ising Model</strong></h>

</br>
</br>

![](progress.gif)

![](magnetization.svg)

## ABOUT

In selected materials, e.g. Fe, Ni, Gd, Co, the temperature strongly affects to their behavior. Each of them has a unique threshold, the Critical Point T<sup>c</sup>, 1034 K for Fe and 292 K for Gd, that causes a transition between the ferromagnetic phase and the paramagnetic phase of the material. When you put a ferromagnetic in a strong magnetic field, it is quite likely that it will move or at least change itself orientation along with trying to keep this established orientation all the time. Now, if you start to cooling the material, till the temperature T will be lower than the critical temperature T<sup>c</sup> (paramagnetic phase), the material should be emancipated from the magnetic field, there will be no correlation between them. This works because of spins. Each atom of a material has the spin feature. If all of spins are the same (an ordered arrangement), the material will be interacting with the magnetic field (ferromagnetic phase), in otherwise (no ordered arrangement) there will be no interaction with the magnetic field (paramagnetic phase). The 2D Ising Model provides procedures to calculate the evolution of behavior of 2D materials at various temperatures. You can find more informations about the Ising Model at [Wei Cai's paper](http://micro.stanford.edu/~caiwei/me334/Chap12_Ising_Model_v04.pdf).

The Python is needed for using the program. The center of the source code is module main.py in which: at the beginning is given the short manual; then there are placed used functions; the trailing if statement controls everything. The listing included in this statement consists of few following sections: modules import; parameters initiation; creation of a system; evolution of the system; results save.

## REQUIREMENTS

    Python >= 3.10

## INTERFACE

### OVERVIEW 

The program is written in Python as few linked modules. To start a simulation, module main.py must be executed. Specifying arguments gives the opportunity to controll the simulation. You can find short description of them below. Here is the general command to run the program:

    python main.py [-a|--algorithm <string>] [-h|--external-magnetic-field <float>] [--help] [-J| --J|--interaction <float>] [-K|--K|--steps <int>] [-L|--length <int>] [-m0|--initial-magnetization <float>] [-s|--seed <int>] [-sc|--save-configuration [<path>]] [-sm|--save-magnetization [<path>]] [-T*|--temperature-reduced <float>] [-v|--visualization [<char><char>]]

This formula looks different, dependently of work station, installed Python and way of execution. The following part exposes some of practical examples.

### INTEGRATION

Exists several ways to run a Python script, you can do it by a Pyton interpreter, an integrated development environment, a terminal or a command line. Some of them are described below. 

<!-- ####  READ-EVAL-PRINT-LOOP
The simplest method to run the probram via an interpreter is to use the REPL. Dependently of form of installed Python, just call out function exec() to run a script. Here are examples

#### IDLE 

Python’s Integrated Development and Learning Environment is the standard Integrated Development Environment provided by Python's installer. It works on REPL in basis, so you can use the same commands. 

#### BASH-->

#### POWERSHELL

The PowerShell given by the Windows, in general demands the the path to the Python and the path to the program

    PS C:\Users\Administrator> . "C:\Program Files\Python\python.exe"   C:\Users\Administrator\IsingMC\main.py -L 30 -m0 1.0 -sc

Both of them can be abbreviated in some cases e.g. in current working directory

    PS C:\Users\Administrator\IsingMC> . "C:\Program Files\Python\python.exe" main.py -L 30 -m0 1.0 -sc

If the Python is added to the Environment Variables in Windows, appears a simpler procedure

    PS C:\Users\Administrator\IsingMC> python main.py -L 30 -m0 1.0 -sc

This command can be even shorter, if the Python Launcher is present

    PS C:\Users\Administrator\IsingMC> py main.py -L 30 -m0 1.0 -sc

<!-- ### EXAMPLES

    py main.py -T* 2.26 -a "metropolis" -v
    py main.py -L 30 -m0 1.0 -sc
    py main.py --seed 23 -K 3000 -sm "./data/" -->


### ARGUMENTS

Specified arguments gives the opportunity to controll the parameters of simulation. You can find a short description below.

<div>
  <code>-a &lt;string&gt;</code></br>
  <code>--algorithm &lt;string&gt;</code></br>
  <ul>
    An algorithm used by Monte Carlo method to computing the evolution of system.</br> Avaliable algorithms: "metropolis"; "glauber". </br>
    The default is "glauber".
  </ul>
</div>
</br>

<div>
  <code>-h &lt;float&gt;</code></br>
  <code>--external-magnetic-field &lt;float&gt;</code></br>
  <ul>
    External homogenious magnetic field h in the system.</br>
    The default is 0.0.
  </ul>
</div>
</br>

<div>
  <code>--help</code></br>
  <ul>
    Prints that text, without executing the code.
  </ul>
</div>
</br>

<div>
  <code>-J &lt;float&gt;</code></br>
  <code>--J &lt;float&gt;</code></br>
  <code>--interaction &lt;float&gt;</code></br>
  <ul>
    Interaction parameter J between each pair of spins.</br>
    The default is 1.0.
  </ul>
</div>
</br>

<div>
  <code>-K &lt;int&gt;</code></br>
  <code>--K &lt;int&gt;</code></br>
  <code>--steps &lt;int&gt;</code></br>
  <ul>
    Time limit. Number of MCSs (iterations).</br>
    The default is 400.
  </ul>
</div>
</br>

<div>
  <code>-L &lt;int&gt;</code></br>
  <code>--length &lt;int&gt;</code></br>
  <ul>
    Length L of lattice LxL in the system of spins.</br>
    The default is 40.
  </ul>
</div>
</br>

<div>
  <code>-m0 &lt;float&gt;</code></br>
  <code>--initial-magnetization &lt;float&gt;</code></br>
  <ul>
    Initial magnetization m(t=0) in the system.</br>
    The default is 0.0.
  </ul>
</div>
</br>

<div>
  <code>-s &lt;int&gt;</code></br>
  <code>--seed &lt;int&gt;</code></br>
  <ul>
    A seed for random number generator in module "random" from the standard library.</br>
    The default is 255.
  </ul>
</div>
</br>

<div>
  <code>-sc [&lt;path&gt;]</code></br>
  <code>--save-configuration [&lt;path&gt;]</code></br>
  <ul>
    At the end of the simulation the configuration of spins S[ij] will be saved in given directory.</br>
    The dafault is ".\".
  </ul>
</div>
</br>

<div>
  <code>-sm [&lt;path&gt;]</code></br>
  <code>--save-magnetization [&lt;path&gt;]</code></br>
  <ul>
    At the end of a simulation, time-dependent evolution of magnetization m in the system will be saved in given directory.</br>
    The dafault is ".\".
  </ul>
</div>
</br>

<div>
  <code>-T* &lt;float&gt;</code></br>
  <code>--temperature-reduced &lt;float&gt;</code></br>
  <ul>
    Reduced temperature T* in the system. T*==1/(J x Beta).</br>
    The default is 1.0.
  </ul>
</div>
</br>

<div>
  <code>-v [&lt;char&gt;&lt;char&gt;]</code></br>
  <code>--visualization [&lt;char&gt;&lt;char&gt;]</code></br>
  <ul>
    Turns on the visual evolution of the system. <code>&lt;char&gt;&lt;char&gt;</code> is a pair of characters which represent spin "up" and spin "down". The total time of the execution will increase.</br>
    The default pair is U+0020, U+2588.
  </ul>
</div>
</br>

## DATA

Check the examples of generated data at [Kaggle](https://www.kaggle.com/datasets/aw6ro7zcd/magnetization).
