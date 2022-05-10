# BM_DFO
Benchmarking suite for DFO algorithms

---

**Version 1.0.0**

Testing suite aims to benchmark derivative-free optimization (DFO) algorithms mainly 'OMADS.py'


---
## License & copyright

© Ahmed H. Bayoumy 
---
---
## Installation

```commandline
$ pip install BM_DFO
```
---
## How to use

After installing the libraries listed in the `requirements.txt`, `BM_suite.py` can be called directly from a 
terminal window under the src directory or imported in the optimization solver code. The path of the JSON template, 
which contains the problem input parameters, should be entered as an input argument to the `OMADS.py` call. 

```commandline
python .\BM_suite.py uncon ..\tests
```

```OMADS.py
import BM_DFO as bm
```

