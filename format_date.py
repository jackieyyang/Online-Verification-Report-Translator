from datetime import datetime, timedelta


# format date
def format_date(date: str) -> str:
    date = [int(s) for s in date.split("/")]
    renewal_date = datetime(date[0], date[1], date[2])
    formatted_time = renewal_date.strftime("%b. %d, %Y")
    return formatted_time


# get renewal date
def get_renewal_date(date: str) -> str:
    date = [int(s) for s in date.split("/")]
    renewal_date = datetime(date[0], date[1], date[2])
    formatted_time = renewal_date.strftime("%b. %d, %Y")
    return formatted_time


# get expiry date
def get_expiry_date(days: str) -> str:
    current_time = datetime.now()
    next_year_time = current_time + timedelta(days=int(days))
    formatted_time = next_year_time.strftime("%b. %d, %Y")
    return formatted_time
