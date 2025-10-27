"""Inventory management system for tracking stock items."""

import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item and its quantity to the stock data."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid item or quantity type.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove specified quantity of an item."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        logging.error(f"Item '{item}' not found: {e}")
    except Exception as e:
        logging.error(f"Unexpected error while removing {item}: {e}")


def get_qty(item):
    """Get quantity of the given item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.warning(f"File {file} not found. Starting with empty stock.")
    except json.JSONDecodeError as e:
        logging.error(f"Error reading JSON file: {e}")


def save_data(file="inventory.json"):
    """Save stock data to file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Print all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items with quantity below threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data() 
    print_data()


if __name__ == "__main__":
    main()
