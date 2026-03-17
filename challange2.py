number = "+49 (176) 123-4567"
newnumber = number.replace('+','').replace('""','').replace("(",
'').replace(")",'').replace(" ","").replace("-",'')

print(f"number: {number}\nnewnumber: {newnumber}")