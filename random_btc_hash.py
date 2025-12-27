# Generate a random number based on bitcoin last block hash
import requests
import random

def get_latest_bitcoin_block_number():
    """
    Get bitcoin last block number using Blockchain.info API.

    Return:
        int: bitcoin last block number, or None if error.
    """
    try:
        response = requests.get('https://blockchain.info/latestblock')
        response.raise_for_status()  # Lança exceção para códigos de status de erro
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar o bloco: {e}")
        return None

def get_bitcoin_block_data(block):
    """
    Get bitcoin block data by block number using Blockchain.info API.

    Retorna:
        int: bitcoin block data, or None if error.
    """
    try:
        height = str(block)
        response = requests.get('https://blockchain.info/block-height/'+height)
        response.raise_for_status()  # Lança exceção para códigos de status de erro
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar o bloco: {e}")
        return None


def randomize(start, end):
    result = None
    latest_block_number = 1
    default_seed = 1024
    random_seed = random.randint(start, end)
	
	# latest block number
    latest_block_data = get_latest_bitcoin_block_number()
    if latest_block_data is not None:
        latest_block_number = int(latest_block_data['height'])
    
    if latest_block_number != 1:
        # get block hash
        block_hash_data = get_bitcoin_block_data(latest_block_number)
        block_hash = block_hash_data['blocks'][0]['hash']
        hash_integer = int(block_hash, 16)
        
        # Use the hash integer to derive a number within the desired range
        result = ((hash_integer + random_seed)% (end - start + 1)) + start
    else:
        result = ((default_seed + random_seed)% (end - start + 1)) + start
    return result
