from brownie import AdvancedCollectible, network
from scripts.utils.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_collectibles} number of collectibles!")
    for tokenId in range(number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(tokenId))
        metadata_filename = f'../../metadata/{network.show_active()}/{tokenId}-{breed}'
        collectible_metadata = metadata_template
        if Path(metadata_filename).exists():
            print(f"{metadata_filename} already exists! Delete to overwrite it.")
        else:
            print(f"Creating metadata file {metadata_filename}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} puppy!"
            # getting the image path for that a particular breed
            image_path = '../../img/' + breed.lower().replace('_', '-') + '.png'
            image_url = upload_image(image_path)
            collectible_metadata["image_uri"] = image_url


def upload_image(filepath):
    with Path(filepath).open('rb') as fp:
        image_binary = fp.read()

        # uploading to ipfs...
        ipfs_url = "http://127.0.0.1:5001/webui"
        endpoint = "/api/v0/add"
        response = requests.post(
            ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split('/')[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
