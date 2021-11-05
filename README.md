FASTRAL-constrained
=========================

FASTRAL-constrained (FASTRAL-J) is a summary method based on [FASTRAL](https://academic.oup.com/bioinformatics/article/37/16/2317/6130791) that can honor user constraints (analogous to [ASTRAL with user constraints](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-020-6607-z), which this work also depends on). This uploaded version works only for x86_64 Linux machines.

```bash
python3 fastral_constrained.py -i $genes -j $constraint -o $output 
```

 - `$genes`: path to newline-separated Newick formatted single-label gene trees
- `$constraint`: the user-specified unresolved constraint tree
- `$output`: output species-tree path

## Dependencies

FASTRAL-constrained currently only works on Linux (x86_64 architecture) due
to its dependency on `asterid` (https://pypi.org/project/asterid/), a Python3 binding for [ASTRID](https://github.com/pranjalv123/ASTRID).

FASTRAL-constrained requires the following packages from pip:

```python3
asterid # currently for Linux x86_64 only
treeswift # we used v1.1.19, although latest stable version likely also works
numpy
```

Additionally, FASTRAL-constrained runs two versions of ASTRAL (so it requires a Java version that can run ASTRAL),
the ASTRAL from FASTRAL (that allows specifying the search space `X`, from https://github.com/PayamDiba/FASTRAL), and the ASTRAL
from constrained ASTRAL (a branched version of ASTRAL. I further modified it to expose some of its subroutines, available at https://github.com/RuneBlaze/Constrained-search).
These two ASTRALs are prepackaged in this repository.