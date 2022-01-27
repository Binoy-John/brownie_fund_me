from brownie import FundMe, accounts
from scripts.helpful_scripts import get_account


def fund():
    account = get_account()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print("entrance_fee is:", entrance_fee)
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": account})
    print("withdraw complete!")


def main():
    fund()
    withdraw()
