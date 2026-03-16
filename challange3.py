# dirty = "968-maleria, ( d@t@ Engineer );; 27y.."
# clean = f"name: {dirty[4:9].lower()} | role:{dirty[12:26].lower()
# .replace('@','a')}| age:{dirty[31:33]}"

# print("*"*50)
# print(dirty)
# print("*"*50)
# print(clean)

phone1 = "+1-6567887464"
phone2 = "+234-9024343825"
phone3 = "+229-89888464646"

print(phone1[phone1.find("-"):].strip('-'))
print(phone2[phone2.find("-"):].strip('-'))
print(phone3[phone3.find("-"):].strip('-'))