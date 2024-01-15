"""Hard soft A
Foundations B
Creative C
OS D
Soft dev E
Soft eng F
Language G

Incompatibilités:
Creative / Language -> C, G
Foundations + soft dev / Hard soft -> B, E, A
Foundations / Soft eng -> B, F
Foundations + soft dev / Language -> B, E, G
Language / Soft eng -> G, F
Language / Hard soft -> G, A
Hard soft / Creative -> A, C"""

X = [["A","B","C","D"],
["A","B","C","E"],
["A","B","C","F"],
["A","B","C","G"],
["A","B","D","E"],
["A","B","D","F"],
["A","B","D","G"],
["A","B","E","F"],
["A","B","E","G"],
["A","B","F","G"],
["A","C","D","E"],
["A","C","D","F"],
["A","C","D","G"],
["A","C","E","F"],
["A","C","E","G"],
["A","C","F","G"],
["A","D","E","F"],
["A","D","E","G"],
["A","D","F","G"],
["A","E","F","G"],
["B","C","D","E"],
["B","C","D","F"],
["B","C","D","G"],
["B","C","E","F"],
["B","C","E","G"],
["B","C","F","G"],
["B","D","E","F"],
["B","D","E","G"],
["B","D","F","G"],
["B","E","F","G"],
["C","D","E","F"],
["C","D","E","G"],
["C","D","F","G"],
["C","E","F","G"],
["D","E","F","G"]]

dico = {"A": "Hardware-Software Interface",
"B": "Foundations 2",
"C": "Creative Design Project",
"D": "Operating Systems & Concurrency",
"E": "Software Development 2",
"F": "Introduction to Software Engineering",
"G": "Language Processors"}

Y = []

for element in X:
    if ("C" in element and "G" in element) or ("B" in element and "F" in element) or ("B" in element and "E" in element and "A" in element) or ("B" in element and "E" in element and "G" in element) or ("F" in element and "G" in element) or ("A" in element and "G" in element) or ("A" in element and "C" in element):
        pass
    else:
        Y.append([])
        for j in range(len(element)):
            Y[-1].append(dico[element[j]])

for X in Y:
    print("- "+str(X)[1:-1].replace("'", ""))

input()
