#!/bin/bash

if [ -e $HOME/".15122-s18-setup-done" ]; then
    echo "You've already completed the setup!"
else

    # Make sure all students have bash as their default shell.. Makes things a lot easier for us
    if [ "$SHELL" != "/bin/bash" ]
    then
        chsh -s /bin/bash
    fi

    # Backing up config files in case they exist
    if [ -e $HOME/.bashrc ]; then cp -b $HOME/.bashrc $HOME/.bashrc-before-15122; fi
    if [ -e $HOME/.vimrc ]; then cp -b $HOME/.vimrc $HOME/.vimrc-before-15122; fi
    if [ -e $HOME/.emacs ]; then cp -b $HOME/.emacs $HOME/.emacs-before-15122; fi

    # Setup the bashrc
    echo 'export PATH=$PATH:/afs/andrew/course/15/122/bin' >> $HOME/.bashrc
    echo "source ~/.bashrc" >> $HOME/.bash_login

    # Setup both vim and emacs because why not
    /afs/andrew.cmu.edu/course/15/122/bin/editor_config/emacs/setup.sh
    /afs/andrew.cmu.edu/course/15/122/bin/editor_config/vim/setup.sh

    echo ""
    echo "Set-up for 15-122 complete:"
    echo "- files modified: ~/.bashrc, ~/emacs, ~/.vimrc (older versions are backed up)"
    echo "- your default shell will now be bash"
    echo "You do *not* need to run this script again"

    touch $HOME/".15122-s18-setup-done"

    # Start up bash just so everyone is on the same playing field..
    # note that this means that if someone is ssh'd this will require
    # an additional `exit` before they can actually exit
    bash
fi
