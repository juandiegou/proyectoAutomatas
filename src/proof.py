
d={
        "llenarA": [5, "B"],
        "llenarB": ["A", 3], 
        "vaciarA": [0, "B"],
        "vaciarB": ["A", 0],
        "pasarAB": [0, "A+B"],
        "pasarABP": ["A-3+B", 3],
        "pasarBA": ["A+B", 0],
        "pasarBAP": [5, "B-5+A"]
}
s= {
        "llenarA": "A<5",
        "llenarB": "B<3",
        "vaciarA": "A>0",
        "vaciarB": "B>0",
        "pasarAB": "A<=3-B and A>0",
        "pasarABP": "A>3-B and B<3",
        "pasarBA": "B<=5-A and B>0",
        "pasarBAP": "B>5-A and A<5"
}
k= {
    "A": [0, 5],
    "B": [0, 3]
}

for x,_ in d.keys():
    print(d[x])
    print(eval(d[x],k))