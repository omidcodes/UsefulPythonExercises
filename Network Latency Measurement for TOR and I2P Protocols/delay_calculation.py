import random
import secrets
import string
import time
from os import urandom

import numpy as np
import pandas as pd
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Others.elgamal_new.constants import (MAX_COMMUNICATION_INTERVAL_VALUE,
                                          MAX_SEED_LATENCY, MAX_SEED_NODEID,
                                          MIN_COMMUNICATION_INTERVAL_VALUE,
                                          MIN_SEED_LATENCY, MIN_SEED_NODEID,
                                          TEST_ID_NODE_COUNT_MAPPINGS)
from sympy import isprime, mod_inverse


class Elgamal:

    @staticmethod
    def encrypt(public_key, m) -> tuple:
        p, g, h = public_key
        y = random.randint(2, p - 2)
        s = pow(h, y, p)
        c1 = pow(g, y, p)
        c2 = (m * s) % p
        return c1, c2

    @staticmethod
    def decrypt(private_key, encrypted_message, p):
        c1, c2 = encrypted_message
        x = private_key
        s = pow(c1, x, p)
        m = (c2 * mod_inverse(s, p)) % p
        return m

    @staticmethod
    def generate_keys(key_size=256) -> dict:
        p = RandomGenerator.generate_prime_number(key_size)
        g = RandomGenerator.find_primitive_root(p)
        x = random.randint(2, p - 2)  # Private key
        h = pow(g, x, p)  # Public key
        return {'publicKey': (p, g, h), 'privateKey': x}


class AES:

    @staticmethod
    def encrypt(key, plaintext):
        iv = urandom(16)  # AES block size is 16 bytes
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return iv + ciphertext  # Prepend IV for use in decryption

    @staticmethod
    def decrypt(key, ciphertext):
        iv = ciphertext[:16]  # Extract the IV from the beginning
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext[16:]) + decryptor.finalize()
        return plaintext.decode()

    @staticmethod
    def generate_key():
        return urandom(32)  # Generate a 256-bit key

    @classmethod
    def aes_key_sharing(cls) -> tuple:
        """ get_encrypted_and_decrypted_aes_keys """

        start = time.time()
        # Example usage
        key_size = 256  # Key size in bits for ElGamal
        keys = Elgamal.generate_keys(key_size)
        public_key = keys['publicKey']
        private_key = keys['privateKey']

        # Generate AES key and encrypt it with ElGamal
        aes_key = cls.generate_key()
        # Simulate converting AES key to an integer for ElGamal encryption
        aes_key_int = int.from_bytes(aes_key, byteorder='big', signed=False)
        encrypted_aes_key = Elgamal.encrypt(public_key, aes_key_int)
        # Decrypt AES key with ElGamal
        decrypted_aes_key_int = Elgamal.decrypt(private_key, encrypted_aes_key, public_key[0])
        decrypted_aes_key = decrypted_aes_key_int.to_bytes((decrypted_aes_key_int.bit_length() + 7) // 8,
                                                           byteorder='big')

        end = time.time()
        execution_time_in_ms = end - start
        return aes_key, execution_time_in_ms

    @classmethod
    def encrypt_and_decrypt_message_with_aes(cls, decrypted_aes_key) -> float:
        """ returns execution_time_in_ms """
        start = time.time()
        some_plaintext = '&>tsX@(3BjsAepZW'
        ciphertext = cls.encrypt(decrypted_aes_key, some_plaintext)
        decrypted_text = cls.decrypt(decrypted_aes_key, ciphertext)
        end = time.time()
        execution_time_in_ms = end - start
        return execution_time_in_ms


class RandomGenerator:

    @staticmethod
    def generate_prime_number(bits):
        while True:
            p = random.getrandbits(bits)
            if isprime(p):
                return p

    @staticmethod
    def find_primitive_root(p):
        if p == 2:
            return 1
        p1 = 2
        p2 = (p - 1) // p1

        while True:
            g = random.randint(2, p - 1)
            if not pow(g, (p - 1) // p1, p) == 1 and not pow(g, (p - 1) // p2, p) == 1:
                return g

    @staticmethod
    def generate_random_string(length: int) -> str:
        """
        https://www.educative.io/edpresso/how-to-generate-a-random-string-in-python

        :param length: positive integer
        :Example:
            generate_random_string(10) => "Qk_qLAC}v?"
        """
        assert isinstance(length, int) and length > 0, "`length` argument must be positive integer."

        letters = string.ascii_letters + string.digits + string.punctuation
        # secrets.choice used instead of random.choice for more security.
        random_str = ''.join(secrets.choice(letters) for _ in range(length))
        return random_str

    @staticmethod
    def generate_random_seed():
        return random.randint(MIN_SEED_NODEID, MAX_SEED_NODEID)


class SimulationModel:
    @staticmethod
    def generate_nodes():
        return pd.DataFrame({
            'NodeID': range(1, 101),
            'LatencyToNextNode_ms': np.random.uniform(MIN_SEED_LATENCY, MAX_SEED_LATENCY, size=100)
        }).assign(IPAddress=['.'.join(map(str, np.random.randint(1, 255, size=4))) for _ in range(100)])

    @staticmethod
    def __get_node_count_for_the_simulation_protocol(simulation_protocol_name: str):
        return TEST_ID_NODE_COUNT_MAPPINGS[simulation_protocol_name]

    @classmethod
    def select_random_nodes(cls, nodes, simulation_protocol_name):
        seed_02, seed_03 = RandomGenerator.generate_random_seed(), RandomGenerator.generate_random_seed()
        selected_nodes = [nodes.iloc[seed_02]]  # Sender
        _node_count_for_the_simulation_protocol: int = cls.__get_node_count_for_the_simulation_protocol(
            simulation_protocol_name
        )
        node_count_for_the_simulation_protocol_without_sender_and_receiver = _node_count_for_the_simulation_protocol - 2
        for _ in range(node_count_for_the_simulation_protocol_without_sender_and_receiver - 2):
            selected_nodes.append(nodes.iloc[np.random.randint(1, 99)])
        selected_nodes.append(nodes.iloc[seed_03])  # Receiver
        return selected_nodes

    @classmethod
    def calculate_latency_for_node(cls, selected_nodes, test_id, communication_interval_max_range):
        """ in seconds """
        sum_latency_for_node, process_time_for_node = 0, 0
        for _ in range(communication_interval_max_range):
            decrypted_aes_key, execution_time_aes = AES.aes_key_sharing()
            execution_time_communication = AES.encrypt_and_decrypt_message_with_aes(decrypted_aes_key)
            process_times = cls.calculate_process_time(test_id, execution_time_aes, execution_time_communication)

            sum_latency_for_node += sum(process_times) + sum(
                node.LatencyToNextNode_ms / 1000 for node in selected_nodes)
        return sum_latency_for_node / communication_interval_max_range

    @staticmethod
    def calculate_process_time(test_id, execution_time_aes, communication_delay):
        if test_id == 'TOR':
            #
            return [execution_time_aes + 3 * communication_delay]
        if test_id == 'I2P':
            return [2 * execution_time_aes + 4 * communication_delay]
        raise NotImplementedError

    @staticmethod
    def calculate_communication_interval_random_number() -> int:
        return random.randint(MIN_COMMUNICATION_INTERVAL_VALUE, MAX_COMMUNICATION_INTERVAL_VALUE)


class ExcelWriter:

    @staticmethod
    def write(results, excel_file_path: str) -> None:
        """ Save results to an Excel file """
        data = np.array(results, dtype=np.float32)
        df = pd.DataFrame(data).T
        df.to_excel(excel_writer=excel_file_path)
