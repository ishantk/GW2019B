message = "\nWork Hard Get Luckier !!"
print(message)

# file = open("quotes.txt","w")
file = open("quotes.txt","a")
file.write(message)
file.close()

print("Data Written")