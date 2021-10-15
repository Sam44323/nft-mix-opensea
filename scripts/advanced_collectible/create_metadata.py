from brownie import AdvancedCollectible, network
from scripts.utils.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_collectibles} number of collectibles!")
    for tokenId in range(number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(tokenId))
        metadata_filename = f'../../metadata/{network.show_active()}/{tokenId}-{breed}'
        print(metadata_filename)
        if Path(metadata_filename).exists():
            print(f"{metadata_filename} already exists! Delete to overwrite it.")
