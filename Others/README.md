brew reinstall nvm

# NVM Stuff
export NVM_DIR="$HOME/.nvm"
. "/usr/local/opt/nvm/nvm.sh"


Remove existing Node/NPM
If you installed Node directly using Homebrew, then uninstall it by running:

brew uninstall node
Now, clean up the rest:
```
sudo
rm -rf /usr/local/lib/node
rm -rf /usr/local/lib/node_modules
rm -rf /usr/local/include/node
rm -rf /usr/local/include/node_modules
rm /usr/local/bin/npm
rm /usr/local/lib/dtrace/node.d
rm -rf ~/.npm
rm -rf ~/.node-gyp
rm /opt/local/bin/node
rm /opt/local/include/node
rm -rf /opt/local/lib/node_modules
```
Install Node/NPM via Homebrew
It's recommended to install Node using nvm, which can be done via Homebrew by:

# install nvm
```
brew update
brew install nvm
# Follow the post install instructions to include nvm in your startup scripts.  I usually do the following:
echo 'export NVM_DIR=~/.nvm' >> .bash_profile
echo 'source $(brew --prefix nvm)/nvm.sh' >> .bash_profile
```

# install your favorite version of node and set it as the default
```
nvm install 0.12
nvm alias default 0.12
```

# in .bash_profile, .zshrc
```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm
```
