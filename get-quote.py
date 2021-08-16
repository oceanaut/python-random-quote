def main():
  print("Keep it logically awesome.")
  
  secret = (48 6f 77 20 64 69 64 20 79 6f 75 20 64 65 76 65 6c 6f 70 20 74 68 65 20 61 64 76 65 72 73 61 72 69 61 6c 20 6d 69 6e 64 73 65 74 3f 20)
  secret_as_bytes= b"".join(secret.split())
  print(secret_as_bytes)

  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()

  #print(quotes)

if __name__== "__main__":
  main()
