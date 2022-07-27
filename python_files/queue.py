!/usr/bin/python3

QUEUE = []

def enqueue():
	element = input('Enter the element : ')
	QUEUE.append(element)
	print(element, ' is added to the QUEUE')

def dequeue():
	if not QUEUE:
		print('QUEUE is empty!')
	else :
		e = QUEUE.pop(0)
		print('Removed element : ',e)

def display():
	print(QUEUE)


def main():
	while True :
		print('Select the operation : 1.add 2.remove 3.show 4.quit')
		choice = int(input())
		if choice==1:
			enqueue()
		elif choice==2:
			dequeue()
		elif choice==3:
			display()
		elif choice==4:
			break
		else :
			print('Invalid Operation')

if __name__ == '__main__':
	main()

