a = [i for i in range(1,2000)]
with open("num.txt", "w") as file:
    file.write(" ".join(map(str,a)))