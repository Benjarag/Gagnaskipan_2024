
f1 = open("vika 3/ArrayListSolution/out.txt")
f2 = open("ArrayListSolution/expected_out.txt")
f3 = open("ArrayListSolution/out_diff.txt", "w+")

line_number = 1
for line1, line2 in zip(f1, f2):
    if line1 != line2:
        print("Difference in line " + str(line_number))
        f3.write("Difference in line " + str(line_number) + "\n")
    line_number += 1

f1.close()
f2.close()
f3.close()