Team members: Anastasia Ershova, Victoria DiTomasso, Ju Chulakadabba

| Trace | Operation | Value | Derivative |
|---|---|---|---|
| x | input | π/2 | [1, 0] |
| y | input | π/3 | [0, 1] |
| v1 | cos(y) | 0.5 | [0, -sqrt(3)/2] |
| v2 | sin(x) | 1 | [0, 0] |
| v3 | subtract(v2, v1) | 0.5 | [0, sqrt(3)/2] |
| v4 | pow(v3, 2) | 0.25 | [0, sqrt(3)/2] |
| v5 | neg(v4) | -0.25 | [0, -sqrt(3)/2] |
| f | exp(v5) | exp(-0.25) | [0, -sqrt(3)/(2*(e^0.25))] |

δf/δx=0, δf/δy=-sqrt(3)/(2*(e^0.25))