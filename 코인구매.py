import requests

def calculate_profit(received_amount, coin_amount):
    profit = received_amount - coin_amount
    return profit

def calculate_coin_amount(received_amount, company_fee_percentage, korean_fee_percentage):
    korean_fee = received_amount * (korean_fee_percentage / 100)
    coin_amount = received_amount - korean_fee

    return coin_amount, calculate_profit(received_amount, coin_amount)

def calculate_admin_profit(profit):
    admin_profit = profit * 0.4
    return admin_profit

def send_discord_webhook(received_amount, coin_amount, company_profit, admin_profit, admin_name):
    webhook_url = "https://discord.com/api/webhooks/1196828478176243752/4xTUBXBqJoVIBJ9Mqei8byrWONlia65EsqSOqbJ5YbWnqxjJhhW4mJgyY0abvOJ5vQZj"

    payload = {
        "content": f"받은 계좌 금액: {received_amount:.2f} 원\n보내야 할 코인 금액: {coin_amount:.2f} 원\n업체 순수익: {company_profit:.2f} 원\n관리자 순수익 ({admin_name}): {admin_profit:.2f} 원"
    }

    requests.post(webhook_url, json=payload)

def main():
    while True:
        received_amount = float(input("계좌로 받은 금액을 입력하세요: "))
        company_fee_percentage = float(input("업체 수수료(퍼센트)를 입력하세요: "))
        korean_fee_percentage = float(input("한국 수수료(퍼센트)를 입력하세요: "))

        admin_name = input("관리자 이름을 입력하세요: ")  # Added this line to get the administrator's name

        coin_amount, company_profit = calculate_coin_amount(received_amount, company_fee_percentage, korean_fee_percentage)
        admin_profit = calculate_admin_profit(company_profit)

        print(f"\n받은 계좌 금액: {received_amount:.2f} 원")
        print(f"보내야 할 코인 금액: {coin_amount:.2f} 원")
        print(f"업체 순수익: {company_profit:.2f} 원")
        print(f"관리자 순수익 ({admin_name}): {admin_profit:.2f} 원")

        send_discord_webhook(received_amount, coin_amount, company_profit, admin_profit, admin_name)

        input("Enter 키를 누르면 다음 계산을 진행합니다. (Ctrl+C로 종료)")

if __name__ == "__main__":
    main()
