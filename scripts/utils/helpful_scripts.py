from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat",
                                 "development", "ganache", "mainnet-fork"]
OPENSEA_URL = 'https://testnets.opensea.io/assets/{}/{}'

contract_to_mock = {
    "vrf_coordinator": VRFCoordinatorMock,
    "link_token": LinkToken,
}


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])
