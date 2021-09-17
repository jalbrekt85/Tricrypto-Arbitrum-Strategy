from brownie import accounts, Contract, interface
from web3 import Web3

acct = accounts[0]
WBTC = "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f"

def main():
   swap_eth_for_erc20(WBTC, Web3.toWei(1, 'ether'))

def load_contract(addr):
    try:
        c = Contract(addr)
    except:
        c = Contract.from_explorer(addr)
        print('not loading from explorer')
    return c

def swap_eth_for_erc20(erc20_address, amount):
    router = interface.IUniswapRouterV2("0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506") #Polygon
    weth = "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1"
    router.swapExactETHForTokens(0, [weth, erc20_address], acct.address, 9999999999999999, {"from": acct, "value": amount})