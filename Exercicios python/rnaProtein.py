biblioteca = {"UUU" : "F" , "CUU": "L" , "AUU": "I" , "GUU": "V",
"UUC" :"F" , "CUC": "L" , "AUC": "I" , "GUC": "V",
"UUA" :"L" , "CUA": "L" , "AUA": "I" , "GUA": "V",
"UUG" :"L" , "CUG": "L" , "AUG": "M" , "GUG": "V",
"UCU" :"S" , "CCU": "P" , "ACU": "T" , "GCU": "A",
"UCC" :"S" , "CCC": "P" , "ACC": "T" , "GCC": "A",
"UCA" :"S" , "CCA": "P" , "ACA": "T" , "GCA": "A",
"UCG" :"S" , "CCG": "P" , "ACG": "T" , "GCG": "A",
"UAU" :"Y" , "CAU": "H" , "AAU": "N" , "GAU": "D",
"UAC" :"Y" , "CAC": "H" , "AAC": "N" , "GAC": "D",
"UAA" :"" , "CAA": "Q" , "AAA": "K" , "GAA": "E",
"UAG" :"" , "CAG": "Q" , "AAG": "K" , "GAG": "E",
"UGU" :"C" , "CGU": "R" , "AGU": "S" , "GGU": "G",
"UGC" :"C" , "CGC": "R" , "AGC": "S" , "GGC": "G",
"UGA" :"" , "CGA": "R" , "AGA": "R" , "GGA": "G",
"UGG" :"W" , "CGG": "R" , "AGG": "R", "GGG": "G"}

dna = open("C:\\Users\\Gabriel\\Documents\\python\\rosalind_prot.txt","r")
dna = dna.read()

proteina = ""
comeco = 0
pedaco = ""
pedaco1 = ""

for i in range(0, (len(dna)-2)):
  pedaco = dna[i]+dna[i+1]+dna[i+2]
  if (pedaco == "AUG"):
    comeco = i
    break

j = comeco
while(j <= (len(dna)-2)):
  pedaco1 = dna[j]+dna[j+1]+dna[j+2]
  proteina = proteina + biblioteca[pedaco1]
  j += 3
  if(pedaco1 == "UAA" or pedaco1 == "UAG" or pedaco1 == "UGA"):
    j = (len(dna)-2)+1
print(proteina)