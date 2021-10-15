from brownie import AdvancedCollectible, network
import pytest
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.utils.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_can_create_advanced_collectible():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    advanced_collectible = deploy_and_create()
    assert advanced_collectible.tokenCounter() == 1
