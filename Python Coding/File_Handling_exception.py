try:
    f = open("dem.txt" , mode = 'r')

except Exception as var:
    print(var)

else:
    f.close()
print('Rest of code')