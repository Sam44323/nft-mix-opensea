from brownie import SimpleCollectible
from scripts.utils.helpful_scripts import get_account

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URL = 'https://testnets.opensea.io/assets/{}/{}'


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    transaction = simple_collectible.createCollectible(
        sample_token_uri, {"from": account})
    transaction.wait(1)
    print(
        f"Awesome, now you can view your nft at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}")
    return simple_collectible


def main():
    deploy_and_create()
