def main():
     BLUE = "\033[94m"
     RESET = "\033[0m"

     age = int (input("How old are you? "))
     print(f"You entered: {BLUE}{age}{RESET}")

     if age >= 18 :
        print("You can vote in Pakistan where the voting age is 18.")
     else:
        print("You cannot vote in Pakistan where the voting age is 18.")
    
     if age >= 25 :
        print("You can vote in Stanlau where the voting age is 25.")
     else:
        print("You cannot vote in Stantau where the voting age is 25.")
    
     if age >= 48 :
        print("You can vote in Mayengua where the voting age is 48.")
     else:
        print("You cannot vote in Mayengua where the voting age is 48.")
    



if __name__ == "__main__":
    main()
