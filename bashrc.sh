#Grant bashrc begin;
#bash startup commands 

#Adding directories to PATH
export PATH="$PATH:/home/grant/setup/bashscripts"
export PATH="$PATH:/home/grant/Matlab/bin"

#bring vim as default editor
export EDITOR=vim


#enables core dumps on this system
ulimit -c unlimited

#bash aliases and functions
alias clip='xclip -sel clip'
alias cmakeinit='touch CMakeLists.txt'
alias mat22AL='ssh -x m22als6-6@point.math.ucdavis.edu'
alias csif='ssh ggilson@pc3.cs.ucdavis.edu'
alias pip='pip3'
#bash functions
count(){
	ARG1=${1:-./}
	ls -1 $ARG1 | wc -l
}
ccat() {
pygmentize -g $1 | perl -e 'print ++$i." $_" for <>'
}

source ~/.cargo/env
source ~/setup/goExport.sh
#Grant bashrc end;

