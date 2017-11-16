#Installing dependencies:
sudo apt-get install build-essential libssl-dev libffi-dev libgmp-dev libsecp256k1-dev
sudo apt-get install python3-pip git 

#Installing python dependencies:
sudo pip3 install coincurve bitcoin

#cloning viper repo
git clone https://github.com/ethereum/viper.git
cd viper

# installing viper
sudo python3 setup.py install

# A better Python REPL
sudo pip3 install ptpython
