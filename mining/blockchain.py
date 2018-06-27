from hashlib import sha256
import json
from time import time
from uuid import uuid4

class Blockchain(object):

# типичный блок
# block = {
#     'index': 1,
#     'timestamp': 1506057125.900785,
#     'transactions': [
#         {
#             'sender': "8527147fe1f5426f9dd545de4b27ee00",
#             'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
#             'amount': 5,
#         }
#     ],
#     'proof': 324984774000,
#     'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
# }

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=None)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        print(block_string)
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 0
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


# b = Blockchain()
# b.new_transaction("Mr. Smith", "Mrs. Berry", 5000)
# block = b.new_block("Birthday")
# b.new_transaction("Mrs. Berry", "Mr. Smith", 4999)
# block = b.new_block("TV")
# b.new_transaction("Mr. Smith", "Mrs. Berry", 4000)
# block = b.new_block("Auto")
#
# b.hash(block)

# x = 5
# y = 0  # We don't know what y should be yet...
# while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
#     print("hash({} * {}) = {}".format(x, y, sha256(f'{x*y}'.encode()).hexdigest()))
#     y += 1
# print("hash({} * {}) = {}".format(x, y, sha256(f'{x*y}'.encode()).hexdigest()))
# print(f'The solution is y = {y}')
