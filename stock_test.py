from nsetools import Nse
from pprint import pprint
from time import sleep

def get_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--cmd', required=True,
        help='command for what need to be done...')
    parser.add_argument(
        '--stock', required=False,
        help='Name of the stock to navigate...')
 
    return parser.parse_args()


#def do_nothing():

def find_upper_circuit(nse):
	print(nse)

	all_stock_codes = nse.get_stock_codes()

	print("############UPPER CIRCUIT LIST ##################")

	for stock in all_stock_codes:
		try:
			q = nse.get_quote(stock)
			closePrice = q['closePrice']
			pricebandupper = q['pricebandupper']
			if closePrice == pricebandupper:
				print(stock)
		except:
			sleep(0)

def get_quote_of_stock(nse, stock):
	pprint(nse.get_quote(stock))

def main():
	args = get_args()

	nse = Nse()
	if args.cmd == "find-upper":
		find_upper_circuit(nse)
	elif args.cmd == "get-quote":
		get_quote_of_stock(nse, args.stock)
	else:
		print('unknown command...')

if __name__ == "__main__":
    main()