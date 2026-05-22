import json
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()
DB_FILE = "airdrops.json"

def load_data():
    if not os.path.exists(DB_FILE):
        default_data = [
            {"name": "Grass Network", "type": "DePIN Node", "status": "Mainnet Phase", "daily_check": True},
            {"name": "Tea Protocol", "type": "Web3 Dev Platform", "status": "Testnet Incentivized", "daily_check": False},
            {"name": "Interlink Network", "type": "Data Protocol", "status": "Early Alpha", "daily_check": True},
            {"name": "Billions Network (OpenClaw)", "type": "Airdrop Automation", "status": "Configuring Task", "daily_check": True}
        ]
        with open(DB_FILE, "w") as f:
            json.dump(default_data, f, indent=4)
        return default_data
    with open(DB_FILE, "r") as f:
        return json.load(f)

def display_dashboard():
    airdrops = load_data()
    console.print("\n[bold cyan]🚀 CRYPTO AIRDROP & WEB3 TASK TRACKER CLI[/bold cyan]", justify="center")
    console.print(f"📅 System Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", justify="center")
    
    table = Table(title="Active Networks & Tasks", title_style="bold magenta")
    table.add_column("No", justify="center", style="dim")
    table.add_column("Network Name", style="bold white")
    table.add_column("Category/Type", style="yellow")
    table.add_column("Status", justify="center")
    table.add_column("Daily Action?", justify="center")

    for idx, item in enumerate(airdrops, 1):
        status_color = "green" if "Mainnet" in item["status"] else "cyan"
        action_str = "[green]YES (Check-in)[/green]" if item["daily_check"] else "[dim white]No[/dim white]"
        
        table.add_row(str(idx), item["name"], item["type"], f"[{status_color}]{item['status']}[/{status_color}]", action_str)

    console.print(table)
    console.print("[dim italic]*Tip: Use GitHub Codespaces or Termux to execute automated skills.*[/dim italic]\n")

if __name__ == "__main__":
    display_dashboard()
