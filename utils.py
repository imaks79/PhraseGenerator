import hashlib, binascii


from rich.console import Console


def getmsg(add_set:str = None):
	console = Console()
	console.clear()

	if add_set:
		console.print(" [yellow]---------------------------------------------------------[/yellow]")
		console.print('[purple]  Количество загруженных адресов для поиска : [/purple]',str(len(add_set)))
		console.print(" [yellow]---------------------------------------------------------[/yellow]")
		console.print(" [purple]             SEED PHRASE GENERATOR V 3.05                 [/purple]")
		console.print(" [yellow]---------------------------------------------------------[/yellow]")
	else:
		console.print(" [yellow]------------------------------------------------------")
		console.print('[yellow] | [purple]              Загрузка адресов, подождите... [/purple]      | [/yellow]')
		console.print(" [yellow]------------------------------------------------------[/yellow]")
		console.print('[yellow] |  [purple]             SEED PHRASE GENERATOR V 3.05        [/purple] [yellow] | ')
		console.print(" [yellow]------------------------------------------------------[/yellow]")


def isOk(ws, nums):
    N = 0
    for w in ws:
        N = (N << 11) + nums.get(w.lower(), 0)
    nhex = format(N, '033x')
    h = hashlib.sha256(binascii.unhexlify(nhex[:-1])).hexdigest()
    return h[0] == nhex[-1]
