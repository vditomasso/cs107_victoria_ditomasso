Team members: Anastasia Ershova, Victoria DiTomasso, Ju Chulakadabba

# f0

| Trace | Operation | Value | Derivative |
|---|---|---|---|
| x | input | 1 | [1, 0] |
| y | input | 1 | [0, 1] |
| v1 | pow(y, 2) | 1 | [0, 2] |
| v2 | pow(x, 2) | 1 | [2, 0] |
| f | add(v2, v1) | 2 | [2, 2] |

# f1

| Trace | Operation | Value | Derivative |
|---|---|---|---|
| x | input | 1 | [1, 0] |
| y | input | 1 | [0, 1] |
| v1 | add(x, y) | 2 | [1, 1] |
| f | exp(v1) | exp(2) | [exp(2), exp(2)] |