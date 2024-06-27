#link na předpis L-systému: https://onlinemathtools.com/l-system-generator

import turtle as t

t.speed(0)
t.tracer(0,0)
t.lt(110)

g0, g1 = "F++F++F++F++F", ""

gens = 4
for i in range(gens):
    for znak in g0:
        if znak == 'F':
            g1 += 'F++F++F+++++F-F++F'
        else:
            g1 += znak
    g0, g1= g1, ""
    
for znak in g0:
    match znak:
        case "F":
            t.fd(5)
        case "+":
            t.rt(36)
        case "-":
            t.lt(36)

t.update()

t.done()