#Grant bashrc begin;
#bash startup commands 

#Adding directories to PATH
export PATH="$PATH:$HOME/bashscripts"

#bring vim as default editor
export EDITOR=vim


#enables core dumps on this system
ulimit -c unlimited

#bash aliases and functions
alias clip='xclip -sel clip'
alias cmakeinit='touch CMakeLists.txt'
alias mat22AL='ssh -x m22als6-6@point.math.ucdavis.edu'
alias csif='ssh ggilson@pc3.cs.ucdavis.edu'

#bash functions
count(){
	ARG1=${1:-./}
	ls -1 $ARG1 | wc -l
}
ccat() {
pygmentize -g $1 | perl -e 'print ++$i." $_" for <>'
}
#Grant bashrc end;
