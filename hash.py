#hash function
import hashlib
hashlib.algorithms_available

h=hashlib.sha3_256()
h.update(b"Hello")
h.hexdigest()
h.update(b"hello")
h.hexdigest()

#encryption and decryption

from cryptography.fernet import Fernet 
key=Fernet.generate_key()
key
cipher_send=Fernet(key)
cipher_send.encrypt(b"hello")
cipher_receiver=Fernet(b'c1GyIQ63YJ2_Vbp_AbkjsFmBo97K0QhHBfFbhJ4oKOg=')
cipher_send.decrypt(b'gAAAAABdqpatAR6Ora5Y4QZRjYljb8ZHBSk-PAR2HaLfk8i5t_ZK-9BUNWTQnLag_LK7M5zYe1CprwCw1_13KA-M87aT2D1FYQ==')
#create our own key
import hashlib
keyword=b"123"
key=hashlib.sha3_256(keyword)
key
key.digest()
import base64
key_bytes=key.digest()
fernet_key=base64.urlsafe_b64encode(key_bytes)
fernet_key
cipher_custom=Fernet(fernet_key)
cipher_custom.encrypt(b"Hie")
cipher_custom.decrypt(b'gAAAAABdqplOHMwbZJYNjY-evMUmDbyu9CcoaUnCKWTzusn1JIhGF0DuEap-gG2TZ-Lnaw8AV_tmHdvb0VnDCIWFb_6jzaU3OQ==')