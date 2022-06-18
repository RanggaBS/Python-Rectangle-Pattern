def DrawRectangle(row, col, char):
	for r in range(1, row+1):
		for c in range(1, col+1):
			print(char, end='')
		print()
		
def main():
	EXIT = 'y'
	while EXIT == 'y':
		ROW = int(input("How many rows?\nAnswer: "))
		COL = int(input("How many columns?\nAnswer: "))
		CHAR = input("Enter a character to display it(ex: #, O, +): ")
		DrawRectangle(ROW, COL, CHAR)
		while True:
			EXIT = input("Again? (y/n)\nAnswer: ").lower()
			if EXIT == 'n' or EXIT == 'y':
				break
			elif EXIT != 'n' and EXIT != 'y':
				print("Please choose y or n only.")
		if EXIT == 'n':
			break
		print()

if __name__ == "__main__":
	main()
