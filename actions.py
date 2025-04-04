from teko.stake import stake_tkusdc
from teko.unstake import unstake_tkusdc
from cap.cap import mint_cusd
from gte.gte import swap_tokens, swap_all_tokens_to_eth
from onchaingm.onchaingm import send_gm

ACTIONS = [
    ("Mint cUSD", mint_cusd, False),
    ("Send GM", send_gm, True),
    ("Random Swap", swap_tokens, True),
    ("tkUSDC Staking", stake_tkusdc, True),
    ("Swap All to ETH", swap_all_tokens_to_eth, True),
]

ALL_ACTIONS = [
    ("tkUSDC Staking", stake_tkusdc, True),
    ("tkUSDC Unstaking", unstake_tkusdc, True),
    ("Mint cUSD", mint_cusd, False),
    ("Random Swap", swap_tokens, True),
    ("Swap All to ETH", swap_all_tokens_to_eth, True),
    ("Send GM", send_gm, True),
]