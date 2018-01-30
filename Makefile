all: dot repo
dot:
	cp ~/.aliases _aliases
	cp ~/.gitignore_global _gitignore_global
	cp ~/.vimrc _vimrc
	cp ~/.aliases _aliases
	cp ~/.astylerc _astylerc
	cp ~/.gitconfig _gitconfig
repo:
	zypper lr -e openSUSE.repo
up: #Upload to remote repo
	git commit -a -m "Updating Conf"
	git push origin master
jupyterfont:
	sudo bash jupyterfont.sh
