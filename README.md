# Symmetric Encryption Example

This repository is also available a Docker image if you just want to run the code without building it yourself 

It is meant to accompany the blog article which can be found at [https://nortronon.com/2022/08/09/symmetric-encryption-101/](https://nortronon.com/2022/08/09/symmetric-encryption-101/)

## Building the container
`docker build -t python-encrypt .`

## Pulling the container
If you do not want to build the container, you can still pull and run it locally:
```
docker pull n0rtr0n/symmetric-encryption-example:latest
docker tag n0rtr0n/symmetric-encryption-example:latest python-encrypt
```

## Generate a new encryption key
```
ENCRYPTION_KEY=`docker run --rm python-encrypt new_key`
```

## Encrypt some text
```
ENCRYPTED_TEXT=`docker run --rm python-encrypt encrypt_text $ENCRYPTION_KEY some_text_you_want_to_encrypt` && echo $ENCRYPTED_TEXT
```

## Decrypt some text
```
docker run --rm python-encrypt decrypt_text $ENCRYPTION_KEY $ENCRYPTED_TEXT
```
