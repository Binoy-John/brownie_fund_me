from brownie import FundMe, accounts, config, network, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    print("account used is ", account)
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_priceFeed"
        ]
        print("price_feed_address is ", price_feed_address)
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print("contract deployed to ", fund_me.address)
    print("entree fee is ", fund_me.getEntranceFee())
    return fund_me


def main():
    deploy_fund_me()
