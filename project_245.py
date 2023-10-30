from web3 import Web3
from tkinter import *
root = Tk()

root.title("My Ethereum App")
root.geometry("500x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum Block", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2)

block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.38, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.5, anchor=CENTER)


infura_url='https://mainnet.infura/v3/cded6e6690d04259b05137dd10b170c3'
web3=Web3(web3.HTTPProvider(infura_url))

def ethereum_block():
    number=int(block_entry.get())
    block_data=number(web3.eth.getBlock())
    transaction=web3.eth.get_transaction(block_data['transactions'][-1].hex())
    Value=transaction['value']
    value_in_ether=value(Value/10**8)
    current_ether_value=value_in_ether*1,679.27

# Write Code for Task 02 below.
gas=transaction['gas']
value_in_dollars=str("Value:$"str('value_in_dollar')(gasused_info_label["text"]))
block_entry=input_box(block_name_label)


    block_entry.destroy()
    search_btn.destroy()


search_btn = Button(root, text="Search Ethereum transaction fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()