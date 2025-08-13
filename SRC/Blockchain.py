from simple_demo.Block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block("Genesis Block", "0") # data, previous hash
        self.chain.append(genesis)
        print("Genesis block created!")

    def get_latest_block(self): # Get the last block in the chain
        return self.chain[-1]

    def add_block(self, data, difficulty=0):
        print(f"\nADDING NEW BLOCK #{len(self.chain)}")
        
        # Create new block
        previous_hash = self.get_latest_block().hash
        new_block = Block(data, previous_hash)
        
        # Mine the block if difficulty is specified
        if difficulty > 0:
            new_block.mine_block(difficulty)
        else:
            print(f"Block added without mining")
            print(f"Hash: {new_block.hash}")
        
        # Add to chain
        self.chain.append(new_block)
        print(f"Block #{len(self.chain)-1} added to blockchain!")

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Check if current block points to previous block
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True

    def print_chain(self):
        print(f"\n{'='*60}")
        print(f"BLOCKCHAIN (Total Blocks: {len(self.chain)})")
        print(f"{'='*60}")
        
        for i, block in enumerate(self.chain): # providing both the index and the value
            print(f"\nBLOCK #{i}:")
            print(block)
        
        print(f"{'='*60}")
        print(f"Blockchain Valid: {self.is_valid()}")
        print(f"{'='*60}")

    def demonstrate_tampering(self):
        if len(self.chain) > 1:
            print(f"\nTAMPERING DEMONSTRATION")
            print(f"Original data: {self.chain[1].data}")
            
            # Tamper with the data
            self.chain[1].data = "HACKED DATA!"
            print(f"Tampered data: {self.chain[1].data}")
