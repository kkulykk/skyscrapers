from skyscrapers import check_skyscrapers

if __name__ == "__main__":
    if check_skyscrapers("check.txt") == True:
        print('Program works correctly')
    else:
        print("Program doesn't work correctly")
