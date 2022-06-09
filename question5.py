# program to compute the molecular weight of a carbohydrate
print("Enter the number of atoms of Hydrogen, Carbon and Oxygen in your carbohydrate respectively")
H_atom = int(input())
C_atom = int(input())
O_atom = int(input())
mol_weight = (H_atom * 1.00794)+(C_atom * 12.0107)+(O_atom * 15.9994)
print("The molecular weight of the given carbohydrate is ",mol_weight," grams/mole")