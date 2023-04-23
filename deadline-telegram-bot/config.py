import yaml
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"
print(config_dir)
config_yaml = None

with open(config_dir / "config.yml", "r") as f:
    config_yaml = yaml.safe_load(f)

telegram_bot_token = config_yaml["telegram_token"]
time_zone = config_yaml["time_zone"]
