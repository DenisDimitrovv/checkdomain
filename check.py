import whois
from datetime import datetime
import time

def check_domain_expiry(domain):
    try:
        domain_info = whois.whois(domain)
        expiry_date = domain_info.expiration_date

        if isinstance(expiry_date, list):
            expiry_date = expiry_date[0]

        return expiry_date
    except Exception as e:
        print(f"Error retrieving WHOIS information for {domain}: {e}")
        return None

def main():
    domains = [
        "atlantisimoti.com",
        "euphoriaburgas.com",
        "atlantisbarcode.com",
        "atlantisresort-bg.com",
        "atlantisbulgaria.com",
        "atlantisdomino.com",
        "vintinvest.com",
        "horizontburgas.com"
        # Add more domains as needed
    ]

    other_domains = {
        "euphoriaburgas.bg": datetime(2024, 10, 11),  # Example: "domain": expiry_date yy/mm/dd
        "atlantisdomino.bg": datetime(2025, 4, 9),
        "horizontimoti.bg": datetime(2024, 10, 11),
        "atlantisaria.bg": datetime(2025, 3, 15),
        "horizontproperties.bg": datetime(2024, 10, 11),
        "iestates.bg": datetime(2024, 8, 17),
        "atlantisbulgaria.bg": datetime(2024, 10, 21),
        "designdistrict.bg": datetime(2031, 9, 20),
        "horizontburgas.bg": datetime(2025, 1, 12),
        "nama.bg": datetime(2024, 12, 1),
        "ah1.bg": datetime(2025, 1, 15),
        "proektstroi.bg": datetime(2025, 4, 11),
        "atmosphere.bg": datetime(2027, 12, 1),
        "atlantisestates.bg": datetime(2027, 1, 22),
        "atlantisimoti.bg": datetime(2024, 10, 11),
        "h88.bg": datetime(2026, 8, 23),
        "themix.bg": datetime(2025, 4, 9),
        "hent.bg": datetime(2025, 3, 22),
        "mizumi.bg": datetime(2024, 6, 1)

        # Add more domains and their expiry dates as needed
    }

    for domain in domains:
        expiry_date = check_domain_expiry(domain)
        if expiry_date:
            days_left = (expiry_date - datetime.now()).days
            print(f"Домейнът {domain} изтича на: {expiry_date}, (остават {days_left} дни.)")
        else:
            print(f"Could not retrieve expiration date for {domain}")

    for domain, expiry_date in other_domains.items():
        time.sleep(1)
        days_left = (expiry_date - datetime.now()).days
        print(f"Домейнът {domain} изтича на: {expiry_date}, (остават {days_left} дни.)")

if __name__ == "__main__":
    main()