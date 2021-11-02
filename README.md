FASTRAL-constrained
=========================

```bash
python3 fastral_constrained.py -i $genes -j $constraint -o $output 
```

## Dependencies

FASTRAL-constrained currently only works on Linux (x86_64 architecture) due
to its dependency on `asterid` (https://pypi.org/project/asterid/), a Python3 binding for [ASTRID](https://github.com/pranjalv123/ASTRID).

FASTRAL-constrained requires the following packages from pip:

```python3
asterid # currently for Linux x86_64 only
```

Additionally, FASTRAL-constrained runs two versions of ASTRAL (so it requires Java),
the ASTRAL from FASTRAL (that allows specifying the search space `X`, from https://github.com/PayamDiba/FASTRAL), and the ASTRAL
from constrained ASTRAL (a forked version, available from https://github.com/RuneBlaze/Constrained-search).
These two ASTRALs are prepackaged in this repository.