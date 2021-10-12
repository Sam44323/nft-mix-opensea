from brownie import AdvancedCollectible
from scripts.utils.helpful_scripts import get_account, OPENSEA_URL


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy({"from": account})


def main():
    deploy_and_create()
