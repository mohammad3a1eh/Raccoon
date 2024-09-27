import os
import importlib.util
import subprocess
import sys
import argparse
import asyncio

MODULES_DIR = './module'
# REQUIREMENTS = []

parser = argparse.ArgumentParser(description='Send RSS feed updates to Telegram bot.')
parser.add_argument('--telegram_token', type=str, required=True, help='Your Telegram bot token')
parser.add_argument('--chat_id', type=str, required=True, help='Your Telegram chat ID')
args = parser.parse_args()

if not args.telegram_token:
    print("Error: Telegram bot token is required.")
    sys.exit(1)


if not args.chat_id:
    print("Error: Telegram chat ID is required.")
    sys.exit(1)
    

telegram_token = args.telegram_token
chat_id = args.chat_id


# for requirement in REQUIREMENTS:
#     try:
#         importlib.import_module(requirement)
#     except ImportError:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", requirement])

async def run_module(module_name, module_path):
    try:
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, 'run'):
            print(f"Running 'run' in module: {module_name}")
            await module.run(token=telegram_token, chat_id=chat_id)
        else:
            print(f"The module '{module_name}' doesn't have a 'run' function.")
    except Exception as e:
        print(f"Failed to run module '{module_name}': {e}")


async def main():
    for file_name in os.listdir(MODULES_DIR):
        if file_name.startswith('module_') and file_name.endswith('.py'):
            module_path = os.path.join(MODULES_DIR, file_name)
            module_name = file_name[:-3]
            await run_module(module_name, module_path)

if __name__ == "__main__":
    asyncio.run(main())
