from datetime import datetime

def conver_date(input_date):
    # Convert 'mm/dd/yy' format to datetime object
    try:
        eta_date = datetime.strptime(input_date, '%m/%d/%y')
        print("ETA date: ", eta_date, " Type: ", type(eta_date))
    except ValueError as e:
        print("Error converting ETA to date:", e)

# Example usage
bol_info = '12/30/23'

conver_date(bol_info)