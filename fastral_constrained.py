import argparse
import os
import asterid as ad
import numpy as np
from os.path import join

ASTRALMPATH = join(os.path.realpath(__file__), "astral.5.7.3.modified.jar")
ASTRALJPATH = join(os.path.realpath(__file__), "astral.5.6.9.jar")

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str,
                        help="Input tree list file", required=True)
parser.add_argument("-j", "--constraint", type=str,
                        help="Input constraint tree", required=True)
parser.add_argument("-o", "--output", type=str, required=True)
args = parser.parse_args()
with open(args.input) as files: genes = files.readlines()

def complete_trees(gtrees, ctreepath):
    gtreepath = args.output + ".gtrees"
    with open(gtreepath, "w+") as fh:
        for g in gtrees:
            fh.write(g)
            fh.write("\n")
    import subprocess
    cmd = f"java -cp {ASTRALJPATH} phylonet.coalescent.TreeCompletion {gtreepath} {ctreepath}"
    return subprocess.check_output(cmd, shell=True,text=True)

k = len(genes)
samplelen = []
samplesize = []
samplelen.append(1)
samplesize.append(k)
samplelen.append(10)
samplesize.append(round(k * 0.5))
samplelen.append(20)
samplesize.append(round(k * 0.25))
samplelen.append(20)
samplesize.append(round(k * 0.1))

trees = []
for l, s in zip(samplelen, samplesize):
    ts = ad.get_ts(genes)
    for i in range(l):
        tees = [genes[j] for j in np.random.choice(len(genes), s, replace=False)]
        D = ad.mk_distance_matrix(ts, tees)
        trees.append(ad.fastme_balme(ts, D, 1, 1))

res = complete_trees(trees, args.constraint)

ctreepath = args.output + ".j"
with open(ctreepath, "w+") as fh:
    fh.write(res)

import os
os.system(
    f"java -jar {ASTRALMPATH} -i {args.input} -p 0 -f {ctreepath} -o {args.output}")