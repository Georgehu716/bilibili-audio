import requests


def main():
    """Test
    """
    r = requests.get('https://www.bilibili.com/video/BV1fh4y1G78k/')
    print(r.encoding)


if __name__ == '__main__':
    main()
