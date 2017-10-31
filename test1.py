#-*- coding: utf-8 -*-
import base64
import binascii
import des

KEY = binascii.a2b_hex('CEC801199468CB678C1A983131628F20F1165BBFE5FD7310')

def encode(text,time=4):
    dOBJ = des.DES()
    dOBJ.input_key(KEY)
    encoded=dOBJ.encode(text)
    #print encoded
    while time:
       time=time-1
       encoded=base64.b64encode(encoded)
    print encoded
    return encoded
def decode(text,time=4):
    decoded = text
    while time:
        time=time-1
        decoded=base64.b64decode(decoded)
    dOBJ = des.DES()
    dOBJ.input_key(KEY)
    decoded=dOBJ.decode(decoded)
    #print decoded
    return decoded


if __name__ == '__main__':
    encode("VjJ0a1lXSkdiRFpTV0dSUFlXdEtkRlJzWkZOaFZUVkZWVlJTWVZaRlJUQlVNVkpoWVZad1JWRlVVbUZXUlZwelZHMXdVbVZzY0VWVlZFSk9WakZLY2xSclVtcE5NREZJVlZSV1drMXNhM3BVVmxKRFlURndkRk5VUW1GaGJYaHlWRzV3VWsxR2NGaFNiWGhQVmpGVmQxZHNaRlprTURGeFVtMW9UMDFzYTNkWGExSnZZVEF4Y1dGSGFGcE5hMVV4Vkd4a1YyRnJOVmhUVkZaYVlXeHJNRlJzVWt0aFJuQklVMVJPVG1Wc2EzZFhWekZPVFdzMVJWRlVUbHBOYkd3elZHMHhXazVGTVRaU1ZFNVFVa1ZGZDFSc1pFdGhiSEJ4VlZSV1RtRnRaRFJYVm1SVFlUQXhXRmRVUmxwbGEzQnhWMnhrUjJKVk1WaFZWRlpoVmpGYWIxZFdaRlpOVm14WVZXMXdUMVl4V25CWGJHUlhZa1V4V0ZadE1VNWhiVTQwVkZod1JtVlZOWFJVV0doYVlXdHJkMVF3VWtKbGJIQjBWMVJHWVZKR1NuUlVWM0JDVFVVNVJWVnRNVTlTTUd3MlYydGtUbVF4Y0ZWWFdHaGhZbFZhY2xReFpGcGxiR3hZVjIweFQxWkZjSEpYVkVwU1pXeHdjVkZVVW1GV1IyTjNWMnRTVGs1Vk1YUlZXR2hRVmtkamQxZHRjRkpOYkd0NVVsaHNUbVZzY0hKWFdIQnlUa1UxZEZKVVVscE5hMncwVjFod2JrMVZPVWhVVkVaUVVrVktjMWRZY0U5aGJHdzJVMWhvV2sxcmF6QlhhMUpPWlVad1ZWSlVVazVoYkZZMVZEQmtUbVZWTVhSVVZGSlBZbFV3ZWxReFpGSmxhelZ4VjFST1dtSlZjRzlVVmxKdVpERnNkRlJZY0ZCV1JrVXdWMjF3UTJFeGNFVlZXR2hoVmtVd01WUlljRXBsYXpWeFYyMXdUMVpHUmpWWFdIQlhZbFp3Y1ZGVVZrNVdNRFZ5VjFSS1YyRnJNVlZVVkZKYVRXdGFkRmRzVWt0aVFUMDk=")