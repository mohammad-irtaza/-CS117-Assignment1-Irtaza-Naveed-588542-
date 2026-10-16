def star_to_delta(ra,rb,rc):
    Rnum=ra*rb + rb*rc + rc*ra
    Rab=Rnum/rc
    Rbc=Rnum/ra
    Rca=Rnum/rb
    return round(Rab,2),round(Rbc,2), round(Rca,2)
print("46, 20, 90 star to delta is",star_to_delta(46, 20, 90))
