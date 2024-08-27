# Ceaser-Cipher-E-D

## Overview

This repository contains a Python script for implementing the Caesar cipher, a classic encryption technique. The Caesar cipher shifts each letter in the plaintext by a fixed number of positions down the alphabet. This repository includes functionality for both encryption and decryption of text using this technique.

## Features

- **Encryption**: Convert plaintext into ciphertext by shifting letters by a specified key.
- **Decryption**: Convert ciphertext back into plaintext using the same key.
- Supports both uppercase and lowercase letters and preserves spaces and non-alphabetic characters.

## How It Works

1. **Encryption**: Each letter in the plaintext is shifted by the key value (e.g., a shift of 3 converts 'a' to 'd').
2. **Decryption**: Each letter in the ciphertext is shifted back by the key value to retrieve the original plaintext.

## Usage

1. **Clone this Repository**:

2. **Run the Script**:

    ```bash
    python caesar_cipher.py
    ```

3. **Follow the Prompts**:

    - Choose `E` for Encryption or `D` for Decryption.
    - Enter the key (an integer between 1 and 26).
    - Enter the text to encrypt or decrypt.

### Example

**Encryption**

- **Input:**
