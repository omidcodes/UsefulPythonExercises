# Project Title: Network Latency Measurement for TOR and I2P Protocols

## Overview

This project aims to accurately calculate the transmission time, also known as message delivery time or network latency, between sender and receiver nodes using TOR and I2P protocols. A significant focus is placed on accounting for encryption and decryption times at various points in the transmission path. By analyzing the latency implications of TOR's multilayer encryption/decryption and I2P's tunneling approach, we provide insights into the performance and security trade-offs of each protocol.

## Getting Started

### Prerequisites

Ensure you have Python 3 installed on your machine. This project relies on specific Python packages, which are listed in the `requirements.txt` file.

### Installation

1. Clone this repository or download the source code to your local machine.
2. Open a terminal in the project directory.
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Configuration
You can customize the simulation parameters by editing the settings section in constants.py. Available settings include MAX_ITERATION_NUMBER and MAX_ROUND_NUMBER among others. Adjust these values to fine-tune the accuracy and performance of the simulation.

### Running the Simulation
Execute the main script to start the simulation:

```bash
python3 main.py
```

After completion, the program generates an Excel file (*.xlsx) containing the results of the transmission time calculations. Review this file to analyze the latency data for both TOR and I2P protocols.


## Project Details

#### Protocols and Encryption
1. TOR (The Onion Router): Implements multilayer encryption/decryption, providing anonymity by routing internet traffic through a worldwide overlay network.
2. I2P (Invisible Internet Project): Utilizes tunneling encryption/decryption to offer a private network layer, enabling secure communication.
#### Encryption Algorithms
1. AES (Advanced Encryption Standard): A symmetric encryption algorithm used for securing data.
2. Elgamal: An asymmetric encryption algorithm that employs two keys (public and private) for encryption and decryption.
### Symmetric vs. Asymmetric Encryption
1. Symmetric Encryption: Utilizes a single key (SharedKey) for both encryption and decryption. It is generally faster but requires the secure exchange of the encryption key.
2. Asymmetric Encryption: Employs a pair of keys (Publickey/PrivateKey) for encryption and decryption. This method is more secure for distributing keys over unsecured channels.
Output
The simulation results, including the calculated transmission times considering encryption and decryption delays, are outputted to an Excel file for further analysis and comparison between TOR and I2P protocols.

For more information on TOR and I2P, including a detailed comparison, visit the official I2P comparison page.
https://geti2p.net/en/comparison/tor
