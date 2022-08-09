import click
from cryptography.fernet import Fernet


def generate_symmetric_encryption_key():
    return Fernet.generate_key()


def encrypt(key, text):
    f = Fernet(key)
    return f.encrypt(text)


def decrypt(key, text):
    f = Fernet(key)
    return f.decrypt(text)


@click.group()
def app():
    """Awesome app doing awesome things."""


@app.command(name="new_key")
def new_key():
    """Generate a new symmetric AES-256 encryption key"""
    encryption_key = generate_symmetric_encryption_key().decode("utf-8")
    print(encryption_key)


@app.command(name="encrypt_text")
@click.argument("key")
@click.argument("text")
def encrypt_text(key, text):
    """Go ahead, encrypt some text!"""
    encrypted_text = encrypt(bytes(key, "utf-8"), bytes(text, "utf-8")).decode("utf-8")
    print(encrypted_text)   


@app.command(name="decrypt_text")
@click.argument("key")
@click.argument("encrypted_text")
def decrypt_text(key, encrypted_text):
    """Go ahead, decrypt some text!"""
    decrypted_text = decrypt(bytes(key, "utf-8"), bytes(encrypted_text, "utf-8")).decode("utf-8")
    print(decrypted_text) 


if __name__ == "__main__":
    app()
