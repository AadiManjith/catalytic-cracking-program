C_count = int(input("Enter number of Carbon atoms in original alkane: "))
H_count = C_count*2 + 2
print("It is C" + str(C_count) + "H" + str(H_count) + ".")
n = int(input("Enter number of different products created: "))
ae = input("If the product you know is an alkane, press 1, if it is an alkene, press 2: ")
c_count = 0
h_count = 0
aneene = ""
if ae == "1":
    c_count = int(input("Enter number of carbons in the alkane: "))
    h_count = c_count*2 + 2
    aneene = "alkene"
elif ae == "2":
    c_count = int(input("Enter number of carbons in the alkene: "))
    h_count = c_count*2
    aneene = "alkane"

C_count = C_count - c_count
H_count = H_count - h_count

print("The " + aneene + " has a molecular formula of C" + str(C_count) + "H" + str(H_count) + ".")