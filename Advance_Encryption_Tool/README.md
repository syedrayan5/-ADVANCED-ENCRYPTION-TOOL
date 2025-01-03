## FILE-INTEGRITY-CHECKER

**COMPANY** : CODTECH IT SOLUTIONS
**NAME** : SYED RAYAN
**INTERN ID** : CT08HWO
**DOMAIN** : CYBERSECURITY AND ETHICAL HACKING
**BATCH DURATION** : December 30th, 2024 to January 30th, 2025
**MENTOR NAME** : NEELA SANTHOSH

# DESCRIPTION OF THE PROJECT

# Name - AES-256 File Encryptor

## Objective:
The AES-256 File Encryptor is a simple tool to securely encrypt and decrypt files using the AES (Advanced Encryption Standard) algorithm with a 256-bit key in CBC (Cipher Block Chaining) mode. The tool is designed for users who need to protect sensitive files by ensuring their confidentiality using strong encryption. The GUI (Graphical User Interface) allows users to easily encrypt or decrypt files with just a few clicks.

## Key Features:
- **AES-256 Encryption**: Implements AES with a 256-bit key to ensure strong file encryption.
- **CBC Mode**: Uses Cipher Block Chaining (CBC) mode for enhanced security.
- **Secure Key & IV Generation**: Automatically generates a secure key and initialization vector (IV) for encryption.
- **GUI-Based**: User-friendly interface built with Tkinter, making it easy to select files and perform encryption or decryption.
- **File Extension Handling**: Encrypted files are saved with the `.enc` extension, while decrypted files are saved with a `_decrypted` suffix.
- **Padding Support**: Files are padded to ensure they are a multiple of the block size, making it suitable for arbitrary file sizes.

## Libraries Used:
- **cryptography**: Provides the cryptographic primitives (e.g., AES algorithm, padding, CBC mode) used for encryption and decryption.
- **tkinter**: A standard GUI library for Python that is used to create the user interface.
- **os**: Used to generate secure random keys and initialization vectors.
- **base64**: Used for encoding the file data (if needed).
  
## Instructions for Usage:
1. **Installation**:
   - Install the necessary Python libraries by running the following command in your terminal or command prompt:
  
     pip install cryptography
  
2. **Running the Application**:
   - Simply run the Python script in Command prompt:
  
     python aes_file_encryptor.py
  
   - This will launch the graphical user interface (GUI).

3. **Encrypting a File**:
   - Click the "Encrypt File" button on the GUI.
   - A file selection dialog will open. Choose the file you wish to encrypt.
   - The file will be encrypted and saved with a `.enc` extension in the same directory as the original file.

4. **Decrypting a File**:
   - Click the "Decrypt File" button on the GUI.
   - Select an encrypted `.enc` file.
   - The file will be decrypted and saved with a `_decrypted` suffix, restoring the original file content.

5. **File Formats**:
   - Supported file formats include any file type, as the encryption works on binary data.

  ## OUTPUT OF THE TASK :
  ![Advance Encryption Tool output](https://github.com/user-attachments/assets/b53ee524-75de-4c8c-83fd-a02f55dc0a22)


