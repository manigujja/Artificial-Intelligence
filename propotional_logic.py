import sympy

p, q, r = sympy.symbols('p q r')

prop1 = p
prop2 = sympy.Not(q)
prop3 = sympy.And(p, q)
prop4 = sympy.Or(p, q)
prop5 = sympy.Implies(p, q)
prop6 = sympy.Eq(p, q)

prop7 = sympy.Not(p)
prop8 = sympy.And(p, p)
prop9 = sympy.Or(p, p)
prop10 = sympy.Or(p, sympy.Not(p))
prop11 = sympy.And(p, sympy.Not(p))
prop12 = sympy.Implies(p, q)

prop15 = sympy.Eq(sympy.Or(p, q), sympy.Or(q, p))
prop16 = sympy.Eq(sympy.And(p, q), sympy.And(q, p))
prop17 = sympy.Eq(sympy.Or(p, sympy.Or(q, r)), sympy.Or(sympy.Or(p, q), r))
prop18 = sympy.Eq(sympy.And(p, sympy.And(q, r)), sympy.And(sympy.And(p, q), r))
prop19 = sympy.Eq(sympy.Or(p, sympy.And(q, r)),
                  sympy.And(sympy.Or(p, q), sympy.Or(p, r)))

prop13 = sympy.Or(p, q, r)
prop14 = sympy.And(p, q, r)

p_value = True
q_value = False

print(f"p = {p_value}, q = {q_value}")
print(f"prop1: {prop1.subs({p: p_value})}")
print(f"prop2: {prop2.subs({q: q_value})}")
print(f"prop3: {prop3.subs({p: p_value, q: q_value})}")
print(f"prop4: {prop4.subs({p: p_value, q: q_value})}")
print(f"prop5: {prop5.subs({p: p_value, q: q_value})}")
print(f"prop6: {prop6.subs({p: p_value, q: q_value})}")
print(f"prop7: {prop7.subs({p: p_value})}")
print(f"prop8: {prop8.subs({p: p_value})}")
print(f"prop9: {prop9.subs({p: p_value})}")
print(f"prop10: {prop10.subs({p: p_value})}")
print(f"prop11: {prop11.subs({p: p_value})}")
print(f"prop12: {prop12.subs({p: p_value, q: q_value})}")

print(f"prop15: {prop15.subs({p: p_value, q: q_value})}")
print(f"prop16: {prop16.subs({p: p_value, q: q_value})}")
print(f"prop17: {prop17.subs({p: p_value, q: q_value, r: p_value})}")
print(f"prop18: {prop18.subs({p: p_value, q: q_value, r: p_value})}")
print(f"prop19: {prop19.subs({p: p_value, q: q_value, r: p_value})}")

def is_valid(proposition):
    return all(
        proposition.subs({p: p_val, q: q_val})
        for p_val in [True, False]
        for q_val in [True, False]
    )

print(f"Is prop1 valid? {is_valid(prop1)}")
print(f"Is prop2 valid? {is_valid(prop2)}")
print(f"Is prop3 valid? {is_valid(prop3)}")
print(f"Is prop4 valid? {is_valid(prop4)}")
print(f"Is prop5 valid? {is_valid(prop5)}")
print(f"Is prop6 valid? {is_valid(prop6)}")

print(f"prop1 satisfiable? {sympy.satisfiable(prop1)}")
print(f"prop2 satisfiable? {sympy.satisfiable(prop2)}")
print(f"prop3 satisfiable? {sympy.satisfiable(prop3)}")
print(f"prop4 satisfiable? {sympy.satisfiable(prop4)}")

print(f"Does prop1 entail prop2? {sympy.ask(sympy.Implies(prop1, prop2))}")

print(f"prop13 DNF: {sympy.to_dnf(prop13)}")
print(f"prop13 CNF: {sympy.to_cnf(prop13)}")
print(f"prop14 DNF: {sympy.to_dnf(prop14)}")
print(f"prop14 CNF: {sympy.to_cnf(prop14)}")
