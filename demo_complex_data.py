from typing import Any, Dict, List

customers = [
    {
        "name": "Murat Knecht",
        "address": {
            "city": "Berlin",
        },
        "account_numbers": ["001727", "029992"],
        3: 7,
     },
]

Account = Dict[str, Any]
Accounts = List[Account]

test: Accounts = customers
