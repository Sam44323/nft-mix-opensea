from scripts.utils.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.simple_collectible.deploy_and_create import deploy_and_create
from brownie import network
import pytest


def network_checker():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()


def test_can_create__simple_collectible():
    network_checker()
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()
