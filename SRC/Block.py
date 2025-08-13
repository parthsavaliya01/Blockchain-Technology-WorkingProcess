import hashlib
import time

class Block:
    def __init__(self, data, previous_hash="0"): # Default previous hash is "0" for the genesis block
        self.data = data                    # Transaction data
        self.previous_hash = previous_hash  # Previous block's hash
        self.timestamp = int(time.time())   # Current Unix timestamp
        self.nonce = 0                      # Number used once (for mining)
        self.hash = self.calculate_hash()   # This block's hash

    def calculate_hash(self):
        block_string = f"{self.data}{self.previous_hash}{self.timestamp}{self.nonce}" # Example: "nirmal->shivangi 10 books"
        return hashlib.md5(block_string.encode()).hexdigest() # using md5, hexadigest: Example output: "5d41402abc4b2a76b9719d911017c592" 128 bit hash value
        # return hashlib.sha256(block_string.encode()).hexdigest() # using sha256, hexadigest: Example output: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" 256 bit hash value

    def mine_block(self, difficulty):
        target = "0" * difficulty # for 2 difficulty, target is "00"
        
        print(f"\nMINING STARTED")
        print(f"Data: {self.data}")
        print(f"Target: Hash starting with '{target}' ({difficulty} zeros)")
        print(f"Mining in progress...\n")
        
        attempts = 0
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1
            print(f"Attempt {attempts:4d}: nonce={self.nonce:6d} | hash={self.hash} | match={self.hash[:difficulty]}")
        
        print(f"\nBLOCK SUCCESSFULLY MINED!")
        print(f"Final hash: {self.hash}")
        print(f"Nonce used: {self.nonce}")
        print(f"Total attempts: {attempts}")
        print("-" * 70)

    def __str__(self):
        return (f"BLOCK INFO:\n"
                f"   Data: {self.data}\n"
                f"   Previous Hash: {self.previous_hash}\n"
                f"   Timestamp: {self.timestamp}\n"
                f"   Nonce: {self.nonce}\n"
                f"   Hash: {self.hash}\n")
