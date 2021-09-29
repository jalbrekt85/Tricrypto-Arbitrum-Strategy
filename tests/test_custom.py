from brownie import *
import brownie
from helpers.constants import AddressZero

"""
  TODO: Put your tests here to prove the strat is good!
  See test_harvest_flow, for the basic tests
  See test_strategy_permissions, for tests at the permissions level
"""



def test_price_feed_change(strategy, strategist, interface):

  wbtc_feed = "0x6ce185860a4963106506C203335A2910413708e9"

  with brownie.reverts("onlyGovernanceOrStrategist"):
    strategy.setPriceFeeds(wbtc_feed, AddressZero, {'from': accounts[1]})

  strategy.setPriceFeeds(wbtc_feed, AddressZero, {'from': strategist})

  feed_from_strat = strategy.WBTC_PRICE_FEED()

  assert feed_from_strat == wbtc_feed

  rate = interface.AggregatorV2V3Interface(wbtc_feed).latestAnswer()
  assert rate != None


def test_set_gauge(strategy, strategist):
  before_bal = strategy.balanceOfPool()
  gauge = "0x97E2768e8E73511cA874545DC5Ff8067eB19B787"
  with brownie.reverts("onlyGovernanceOrStrategist"):
    strategy.setGauge(gauge, {'from': accounts[1]})

  strategy.setGauge(gauge, {'from': strategist})

