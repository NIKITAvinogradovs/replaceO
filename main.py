teksts = input ("Ievadi tekstu ar O vai o :")
def replaceO (teksts):
  if teksts.count("o")>0 or teksts.count("O")>0:
    teksts = teksts.replace("O", "%")
    teksts = teksts.replace("o", "%")
    print (teksts)
  else:
    teksts = "teksta nav burtu o"
    print (teksts)
  return teksts
replaceO (teksts)