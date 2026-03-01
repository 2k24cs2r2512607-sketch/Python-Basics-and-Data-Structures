g="VS"
dict={
    x:{y:x+y for y in g} for x in g
}
print(dict) 