import hashlib
import time
import os

class Block:
    def _init_(self, index, previous_hash, timestamp, document_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.document_hash = document_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.document_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def _init_(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_document(self, document_hash):
        new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), document_hash)
        self.chain.append(new_block)

    def is_document_valid(self, document_hash):
        for block in self.chain[1:]:  # Skip Genesis
            if block.document_hash == document_hash:
                return True
        return False


# Helper function to hash a file
def hash_file(filename):
    sha = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            sha.update(chunk)
    return sha.hexdigest()


# Example usage
if _name_ == "_main_":
    doc_chain = Blockchain()

    # Example documents
    docs_folder = "example_docs"
    files = ["document1.txt", "document2.txt", "tampered_document1.txt"]

    # Add some documents to blockchain
    doc1 = hash_file(os.path.join(docs_folder, "document1.txt"))
    doc_chain.add_document(doc1)

    doc2 = hash_file(os.path.join(docs_folder, "document2.txt"))
    doc_chain.add_document(doc2)

    # Verify original document
    check_doc = hash_file(os.path.join(docs_folder, "document1.txt"))
    print("Document1 valid?", doc_chain.is_document_valid(check_doc))

    # Verify tampered document
    tampered_doc = hash_file(os.path.join(docs_folder, "tampered_document1.txt"))
    print("Tampered Document valid?", doc_chain.is_document_valid(tampered_doc))
