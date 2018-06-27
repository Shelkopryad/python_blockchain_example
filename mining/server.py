import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')
my_blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    last_block = my_blockchain.last_block
    last_proof = last_block['proof']
    proof = my_blockchain.proof_of_work(last_proof)
    my_blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )
    block = my_blockchain.new_block(proof)
    response = {
        'message': "New Block Forgeg",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    index = my_blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': my_blockchain.chain,
        'length': len(my_blockchain.chain),
    }
    return jsonify(response), 200
