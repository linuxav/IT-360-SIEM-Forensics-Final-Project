 # API token/config manager
import os 
import configparser
import getpass
from pathlib import Path

def create_config(config_path: Path) -> configparser.ConfigParser:
    """Prompt the user for their API Key and generate the config.ini"""
    print(f"Configuration file {config_path} not found! Generating config file...")
    api_key = getpass.getpass("Enter your AbuseIPDB API Key: ").strip()
    if not api_key:
        raise ValueError("API Key cannot be empty!")
    
    config = configparser.ConfigParser()
    config["ABUSEIPDB"] = {"api_key" : api_key}
    
    with config_path.open("w", encoding="utf-8") as f:
        config.write(f)
    
    os.chmod(config_path, 0o600)
    
    print(f"Configuration file saved to {config_path}.\n")
    return config
    
def load_config(config_path: str = "config.ini") -> dict:
    """Load config.ini and override with environment variables if available"""
    config = configparser.ConfigParser()
    path = Path(config_path)
    env_api_key = os.getenv("ABUSEIPDB_KEY")
    
    if path.exists():
        config.read(path, encoding="utf-8")
    elif not env_api_key:
        config = create_config(path)
        
    ini_api_key = config.get("ABUSEIPDB", "api_key", fallback=None)
    final_api_key = env_api_key or ini_api_key
    
    if not final_api_key:
        raise ValueError("Missing AbuseIPDB API Key in environment and/or config.ini")
    
    return {"ABUSEIPDB_KEY": final_api_key}