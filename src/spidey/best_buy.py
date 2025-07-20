import requests


def check_if_best_buy_item_sellable(skuId: str) -> bool:
    """
    Checks if Best Buy item is sellable online by attempting to add to cart.
    """
    url = "https://www.bestbuy.com/cart/api/v1/addToCart"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json; charset=UTF-8",
        "Origin": "https://www.bestbuy.com",
    }
    payload = {"items": [{"skuId": skuId}], "fetchInterruptorData": True}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return "ITEM_NOT_SELLABLE" not in response.text
    except Exception as e:
        print(f"Request failed: {e}")
        return False
