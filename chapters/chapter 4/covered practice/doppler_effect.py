status = None
fs = float(input(" what is fs \n"))
vs = float(input(" what is vs \n"))
vo = float(input(" what is vo \n"))
v  = float(input(" what is v \n"))


if ( vs>0 and vo>0 ):
    if (abs(vs)<abs(vo)):
        status = "away"
    else:
        status = "toward"
elif( abs(vs)<abs(vo) ):
    status = "toward"
elif( abs(vs)>abs(vo) ):
    status = "away"


if ( vs*vo < 0 ):
    if ( vs>0 and vo<0):
        status = "toward"
    else:
        status = "away"

if ( status == "away" ):
    fo = fs*( (v-vo)/(v+vs) )
else:
    fo = fs*( (v+vo)/(v-vs) )

print(status)
print(fo)
