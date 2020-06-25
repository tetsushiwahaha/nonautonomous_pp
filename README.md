# nonautonomous_pp2

Display an orbit of the given nonautonomous ODE. The right hand of the
ODE is described in the setup file. Compared with `nonautonomous_pp`, 
it is not required a function definition file `ppfunc.pp` anymore. 
So, you do not have to maintain two related files `ppfunc.pp` and
setupfile in parallel. Focus on setup file only.
The right hand of the ODE in the setup file is evaluated by
`eval()` function. Possibly this `eval()` consumes much time in general, but
the author does not recognize an obvious delay as far as examined.

## Requirements
* python 3.8 later
    * numpy, scipy
    * matplotlib

## Files
* pp.py -- a simulator 
* ppfunc.py -- right hand of the ODE
* pptools.py -- misc. tools
* in.json -- setup file. A JSON format.

## To exec

    % python pp.py in.json

## Setup file configuration

* func: a list of the right hand of the ODE.
* xrange, yrange: x-y range of the graph
* alpha:  transparency value, zero to one.
* params:	a list of parameter values
* x0:	a list of initial values
* dparams: a list of incremental values corresponding to the parameters
* tick: a time step for drawing a curve

### variables and parameters

* `x[0]`, `x[1]`, ...: state variables
* `data.dict['params'][0]`, `data.dict['params'][1]`, ...: parameters 

## How to use
### mouse operation 

- A new initial values is given by clicking on the appropriate location
in the graph.
 
### key operation

- `s`: print the current status
- `f`: show/hide trajectory (toggle)
- `w`: print the dictionary and dump it to `__ppout__.json`
- `p`: change the active parameter (default: 0, toggle)
- up and down arrows: increase/decrease the active parameter value
- `space`: clear transitions
- `q`: quit 
}

