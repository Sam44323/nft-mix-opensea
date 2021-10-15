from brownie import AdvancedCollectible, config, network
from scripts.utils.helpful_scripts import get_account, OPENSEA_URL, get_contract, fund_with_link


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract('vrf_coordinator'),
        get_contract('link_token'),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account}, publish_source=config["networks"][network.show_active()].get("verify", False))
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})

    creating_tx.wait(1)
    print("New token has been created!")
    return advanced_collectible


def main():
    deploy_and_create()
