#!/usr/bin/python3

STACK = []
def push():
	element = input('Enter the element : ')
	STACK.append(element)
	print(STACK)

def pop():
	if not STACK:
		print('STACK is empty!')
	else:
		e = STACK.pop()
		print('Removed element : ',e)
		print(STACK)


def main():
	while True :
		print('Select the operation : 1.push 2.pop 3.quit')
		choice = int(input())
		if choice == 1:
			push()
		elif choice == 2:
			pop()
		elif choice == 3:
			break
		else :
			print('Invalid Operation')


if __name__ == '__main__':
	main()