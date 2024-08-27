#!/usr/bin/env python3
import torch
from torch import nn
import numpy as np
from functools import reduce
import base64

output = "1VfgPsBNALxwfdW9yUmwPpnI075HhKg9bD5gPDLvjL026ho/xEpQvU5D4L3mOso+KGS7vvpT5T0FeN284inWPXyjaj7oZgI8I7q5vTWhOj7yFEq+TtmsPaYN7jxytdC9cIGwPti6ALw28Pm9eFZ/PkVBV75iV/U9NoP4PDoFn72+rI8+HHZivMwJvr2s5IQ+nASFvhoW2j1+uHE98MbuvdSNsT4kzrK82BGLvRrikz6oU66+oCGCPajDmzyg7Q69OjiDPvQtnjxwWw2+IB9ZPmaCLb4Mwhc+LimEPXXBQL75OQ8/ulQUvZZMsr3iO88+ZHz3viUgLT2U/d68C2xYPQ=="
flaglen = 64
flag = b"buckeye{???????????????????????????????????????????????????????}"

newmodel = torch.load("model.pth")

decryptedflag = base64.b64decode(output)
decryptedflag = np.frombuffer(decryptedflag, dtype="float32")
decryptedflag = np.reshape(decryptedflag, (8, 8))
decryptedflag = torch.from_numpy(decryptedflag)

decryptedflag = decryptedflag[..., None]
for i in range(7):
    decryptedflag = torch.linalg.solve(newmodel['stack.0.weight'], decryptedflag)

almost = []
for i in decryptedflag:
    for j in i:
        j = float(j)
        almost.append(chr(int(round(j, 0))))
print("".join(almost))
