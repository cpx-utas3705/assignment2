import pandas as pd

def print_menu():
    print()
    print("1.Daily outlook for total revenue")
    print("2.Daily report")
    print("3.Mothly outlook for total revenue")
    print("4.Monthly report for detail")
    print("5.quite")

def main():
    select_fountion=0     
    #data = pd.read_csv(input("Pleace anter the file name with .csv : "))
    data = pd.read_csv("coffee-shop-sales-revenue.csv",sep='|')


    while select_fountion !=5:
        print_menu()
        select_fountion= int(input("What function do you want to use: "))

        
        
main()