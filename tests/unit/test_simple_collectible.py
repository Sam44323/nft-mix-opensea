from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network
import pytest


def network_checker():
  if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
      pytest.skip()

def test_can_create__simple_collectible():
    network_checker()
