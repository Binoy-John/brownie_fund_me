from brownie import config, network, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]
DECIMALS = 8
STARTING = 2000000000000000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        return accounts[0]
    else:
        # accounts.add(config["wallets"]["from_key"])
        # return config["wallets"]["from_key"]
        # print(accounts.add(config["wallets"]["from_key"]))
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    account = get_account()
    print("from deploy ")
    print("the active network is ", network.show_active())
    print("deploying the contract")

    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING, {"from": account})
        print("Deployed a new Mock because the length of MockV3Aggregator was 0")
    # print("mock aggregator is ", mock_aggregator)
    print("Mock deployed!")

    # print("Mocks deployed on ", mock_aggregator)
