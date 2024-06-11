import whois
from datetime import datetime

def check_domain_expiry(domain):
    try:
        domain_info = whois.whois(domain)
        expiry_date = domain_info.expiration_date

        # expiry_date could be a list or a single datetime object
        if isinstance(expiry_date, list):
            expiry_date = expiry_date[0]

        return expiry_date
    except Exception as e:
        print(f"Error retrieving WHOIS information for {domain}: {e}")
        return None

def main():
    domains = [
        "https://www.atlantisbulgaria.com/",
        "https://atlantisbarcode.com/",
        "https://l6.club/"
        # Add more domains as needed
    ]

    for domain in domains:
        expiry_date = check_domain_expiry(domain)
        if expiry_date:
            days_left = (expiry_date - datetime.now()).days
            print(f"The domain {domain} expires on: {expiry_date}, ({days_left} days left)")
        else:
            print(f"Could not retrieve expiration date for {domain}")

if __name__ == "__main__":
    main()