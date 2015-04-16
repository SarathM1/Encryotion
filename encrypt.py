#!/usr/bin/python
from subprocess import call as c

def main():
	com1c = 'tar zcvf test.tar --exclude=flasky --exclude=*.sig ../test/'
	com2c = 'gpg -c test.tar'
	com3c = 'git push origin master'
	p1 = c(com1c.split())
	p2 = c(com2c.split())

	ch = raw_input("Push march29 to github/march29?(y/n):")
	if(ch=='y'):
		p3 = c(com3c.split()) 


if __name__ == '__main__':
	main()