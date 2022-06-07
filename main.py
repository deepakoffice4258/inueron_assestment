input=open("example.txt","rt")
output=open("new.txt","wt")
for line in input:
    output.write(line.replace("placement","screening"))
input.close()
output.close()

