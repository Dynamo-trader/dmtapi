from enum import Enum

from pydantic import BaseModel, Field


class TradeDirection(Enum):
    """
    Enumeration of possible trade directions.
    """
    buy = "buy"
    sell = "sell"


class TakeProfit(BaseModel):
    """
    Configuration for take profit levels.

    Attributes:
        price (float): Take profit price level.
        close_pct (float): Percentage of position to close (0-1).
        tp_as_pip (float): Take profit in pips (priority over tp_as_pct).
        tp_as_pct (float): Take profit as percentage.
    """
    price: float = Field(default=None, ge=0)
    close_pct: float = Field(
        gt=0, le=1, description="Close percentage of the total volume"
    )
    tp_as_pip: float = Field(
        default=0,
        ge=0,
        le=1,
        description="Take profit as pips. Priority: price > tp_as_pip > tp_as_pct",
    )
    tp_as_pct: float = Field(
        default=0,
        ge=0,
        le=1,
        description="Take profit as percentage. Priority: price > tp_as_pip > tp_as_pct",
    )


class TradeSetup(BaseModel):
    """
    Configuration for opening a new trade.

    Attributes:
        symbol (str): Trading symbol (e.g., "EURUSD").
        volume (float): Trading volume (0-100).
        direction (TradeDirection): Trade direction (buy/sell).
        magic (int): Magic number for trade identification.
        entry_price (float): Entry price for the trade.
        stop_loss (float): Stop loss price.
        sl_as_pip (float): Stop loss in pips (priority over sl_as_pct).
        sl_as_pct (float): Stop loss as percentage.
        take_profits (list[TakeProfit]): List of take profit levels.
        deviation (int): Maximum price deviation (0-100).
    """
    symbol: str
    volume: float = Field(..., gt=0, le=100)
    direction: TradeDirection
    magic: int = Field(None, ge=0)
    entry_price: float = Field(default=0.0, ge=0)
    stop_loss: float = Field(default=0.0, ge=0)
    sl_as_pip: float = Field(
        default=None,
        gt=0,
        le=1,
        description="Stop loss as pips, stop_loss is ignored if set. Takes priority over sl_as_pct",
    )
    sl_as_pct: float = Field(
        default=None,
        gt=0,
        le=1,
        description="Stop loss as percentage, stop_loss is ignored if set",
    )
    take_profits: list[TakeProfit] = Field(default_factory=list)
    deviation: int = Field(default=0, ge=0, le=100)
