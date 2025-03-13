'''
AutoScan Demonstration
----------------------
'''

# Import AutoTrader
from autotrader.autotrader import AutoTrader

# Create AutoTrader instance
at = AutoTrader()
at.scan('supertrend')
at.run()