import pandas as pd

data = pd.read_csv("coffee-shop-sales-revenue.csv",sep='|')


def load_csv(data):
    print (data)
    print (data.dtypes)

    
def validate_data(data):
    valid_data = data[["transaction_date","transaction_qty","unit_price","product_category","product_type"]]
    return valid_data
    
    
def choose_data_by_store(data):
    
    store_list = data["store_location"].unique().tolist()
    i=len(store_list)
    if i>1:
        print("Exist store choose \n",store_list)
        choose_store =input("Which store do you went to over look: ")
        while choose_store not in store_list:
            print("Store can not be found")
            choose_store = input("Pleace anter a store from the list :")
            
    else:
        choose_store = store_list[0]
    return choose_store

choose_data_by_store(data)

