from brownie import SimpleStorage, accounts

def main():
   account = accounts[0]
   some_gas_price = 671091690
   simple_storage_contract = SimpleStorage.deploy({"from": account, "gas_price" : some_gas_price})
   print(simple_storage_contract.number())

   simple_storage_contract.setNumber(777, {"from": account , "gas_price" : some_gas_price})
   print(simple_storage_contract.number())