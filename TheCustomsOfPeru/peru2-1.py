import requests


def get_list():
    url = "http://www.aduanet.gob.pe/itarancel/JSPDetallePartidaArancel.jsp"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'TS01577d4a=014dc399cbbcffe5c190cd0a6ad2df063bf84705f4322d3dfb366f9c1cb9952e71c1f3d15ea6ff23e314268308a2e949f569c669a4f4f25030372060c6c560382b10fdacde; ITARANCELTEMPSESSION=qsYyp5GTgyjLfXzhFQ1FBRr36fhMySTbMvNG9wpLhsdV2crW1ns4tTpL9Q0hG1TrMnRppJL1RHntnNyJ7TsW0139fVyK11s1kFn9nZPyGhp69hfQn3YWHgwvwn6FY0NjTLHLz51f0sTHgS7LkJJ7NTLptyjVhl2mbGyFhSd4mPBL2xcwLXny622lP1b36MnybGLWsG3hRgCMxQQpLyl3vFqL1TmLpbddR7qwTbqNNyVpvyBSlnlwRmYGty6QkGpb!-1653864741!1337442711',
        'Host': 'www.aduanet.gob.pe',
        'Pragma': 'no-cache',
        'Referer': 'http://www.aduanet.gob.pe/itarancel/arancelS01Alias?accion=buscarPartida&esframe=1&cod_partida=101210000',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def main():
    for i in range(0, 10):
        get_list()


if __name__ == '__main__':
    main()
