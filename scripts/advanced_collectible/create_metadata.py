from brownie import AdvancedCollectible, network
from scripts.utils.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
import pathlib


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_collectibles} number of collectibles!")
    for tokenId in range(number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(tokenId))
        metadata_filename = f'../../metadata/{network.show_active()}/{tokenId}-{breed}'
        print(metadata_filename)
