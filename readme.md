
<h1 align="center"><strong>Monte Carlo simulations of Ising Model</strong></h>

</br>
</br>

![](progress.gif)

![](magnetization.svg)

## ABOUT

The program provide the Monte Carlo simulations of 2D Ising model.

## COMMAND LINE INTERFACE

    py main.py [-a|--algorithm <string>] [-h|--external-magnetic-field <float>] [--help] [-J|--J|--interaction <float>] [-K|--K|--steps <int>] [-L|--length <int>] [-m0|--initial-magnetization <float>] [-s|--seed <int>] [-sc|--save-configuration [<path>]] [-sm|--save-magnetization [<path>]] [-T*|--temperature-reduced <float>] [-v|--visualization [<char><char>]]


## MANUAL

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
    The default is 1997.
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
    
## REQUIREMENTS

    Python >= 3.10.2

## EXAMPLES

    py main.py -T* 2.26 -a "metropolis" -v
    py main.py -L 30 -m0 1.0 -sc
    py main.py --seed 23 -K 3000 -sm "./data/"

## DATASETS

Check examples of generated datasets in 
<a href="https://www.kaggle.com/datasets/quantumbraindisorder/magnetization" target="_blank">Kaggle</a>