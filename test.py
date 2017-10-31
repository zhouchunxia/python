# coding=utf-8
import base64

def test():
        filea = open('C:\Users\zhouchunxia\Desktop\\test.txt','r')
        lines = filea.read()
        print lines
        writefile = open("C:\Users\zhouchunxia\Desktop\jiemi.txt","w")
        base64.decode(filea,writefile)
        #writefile.close()
        #filea.close()


def test1():
    a = base64.b64decode("VjJ0a1lXSkdiRFpTV0dSUFlXdEtkRlJzWkZOaFZUVkZWVlJTWVZaRlJUQlVNVkpoWVZad1JWRlVVbUZXUlZwelZHMXdVbVZzY0VWVlZFSk9WakZLY2xSclVtcE5NREZJVlZSV1drMXNhM3BVVmxKRFlURndkRk5VUW1GaGJYaHlWRzV3VWsxR2NGaFNiWGhQVmpGVmQxZHNaRlprTURGeFVtMW9UMDFzYTNkWGExSnZZVEF4Y1dGSGFGcE5hMVV4Vkd4a1YyRnJOVmhUVkZaYVlXeHJNRlJzVWt0aFJuQklVMVJPVG1Wc2EzZFhWekZPVFdzMVJWRlVUbHBOYkd3elZHMHhXazVGTVRaU1ZFNVFVa1ZGZDFSc1pFdGhiSEJ4VlZSV1RtRnRaRFJYVm1SVFlUQXhXRmRVUmxwbGEzQnhWMnhrUjJKVk1WaFZWRlpoVmpGYWIxZFdaRlpOVm14WVZXMXdUMVl4V25CWGJHUlhZa1V4V0ZadE1VNWhiVTQwVkZod1JtVlZOWFJVV0doYVlXdHJkMVF3VWtKbGJIQjBWMVJHWVZKR1NuUlVWM0JDVFVVNVJWVnRNVTlTTUd3MlYydGtUbVF4Y0ZWWFdHaGhZbFZhY2xReFpGcGxiR3hZVjIweFQxWkZjSEpYVkVwU1pXeHdjVkZVVW1GV1IyTjNWMnRTVGs1Vk1YUlZXR2hRVmtkamQxZHRjRkpOYkd0NVVsaHNUbVZzY0hKWFdIQnlUa1UxZEZKVVVscE5hMncwVjFod2JrMVZPVWhVVkVaUVVrVktjMWRZY0U5aGJHdzJVMWhvV2sxcmF6QlhhMUpPWlVad1ZWSlVVazVoYkZZMVZEQmtUbVZWTVhSVVZGSlBZbFV3ZWxReFpGSmxhelZ4VjFST1dtSlZjRzlVVmxKdVpERnNkRlJZY0ZCV1JrVXdWMjF3UTJFeGNFVlZXR2hoVmtVd01WUlljRXBsYXpWeFYyMXdUMVpHUmpWWFdIQlhZbFp3Y1ZGVVZrNVdNRFZ5VjFSS1YyRnJNVlZVVkZKYVRXdGFkRmRzVWt0aVFUMDk=")
    print a
if __name__ == '__main__':
    test()
    test1()
