import asyncio
import random
import time
import os
from actions import ACTIONS, ALL_ACTIONS
from teko.config import PRIVATE_KEYS
from eth_account import Account

# Clear terminal secara lintas platform
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

clear_terminal()

def print_header(text, width=70):
    print(f"\n{'=' * width}")
    print(f"  NubiZen - {text}".ljust(width-2))
    print(f"{'=' * width}")

def print_section(text, width=70):
    print(f"\n{'-' * width}")
    print(f"  {text}".ljust(width-2))
    print(f"{'-' * width}")

def print_action(wallet, action_name, status, details="", width=70):
    wallet_short = f"{wallet[:6]}...{wallet[-4:]}"
    status_text = "SUCCESS" if status == "success" else "FAILED"
    line = f"  {wallet_short}  |  {action_name:<20}  |  {status_text:<7}  |  {details}"
    print(line[:width-2].ljust(width-2))

def get_user_choice():
    print_header("Mode Selection")
    print("  Available Modes:")
    print("  1. 1x Jalan")
    print("  2. Loop Acak")
    print("  3. Loop Beruruta")
    print("-" * 70)
    choice = input("  Enter your number: ")
    return choice

async def execute_action(wallet, pk, action_name, action_func, is_async):
    Account._active_key = pk
    try:
        if is_async:
            await action_func()
        else:
            action_func()
        print_action(wallet, action_name, "success")
    except Exception as e:
        print_action(wallet, action_name, "error", str(e))

async def process_wallet(wallet, pk, actions):
    print_header(f"Processing Wallet: {wallet[:6]}...{wallet[-4:]}")
    print("  Wallet           |  Action               |  Status  |  Details")
    print("-" * 70)
    for action_name, action_func, is_async in actions:
        print(f"  Executing: {action_name}")
        await execute_action(wallet, pk, action_name, action_func, is_async)
    print_section(f"Completed Wallet: {wallet[:6]}...{wallet[-4:]}")

async def main():
    print_header("Starting Action Executor")
    choice = get_user_choice()

    if choice == "2":
        while True:
            for pk in PRIVATE_KEYS:
                account = Account.from_key(pk.strip())
                wallet = account.address
                tasks = ALL_ACTIONS.copy()
                random.shuffle(tasks)
                await process_wallet(wallet, pk, tasks)
            print_header("Starting New Random Cycle")
            time.sleep(5)

    elif choice == "3":
        while True:
            for pk in PRIVATE_KEYS:
                account = Account.from_key(pk.strip())
                wallet = account.address
                await process_wallet(wallet, pk, ACTIONS)
            print_header("Repeating User-Defined Actions")
            time.sleep(5)

    else:  # Default to mode 1
        for pk in PRIVATE_KEYS:
            account = Account.from_key(pk.strip())
            wallet = account.address
            await process_wallet(wallet, pk, ACTIONS)

    print_header("Execution Completed")

if __name__ == "__main__":
    asyncio.run(main())