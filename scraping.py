from requests_html import HTMLSession

def start(perfil):
	url = 'https://www.olx.com.br/perfil/' + perfil
	try:
		s = HTMLSession()
		r = s.get(url)
		r.html.render(timeout=20)
	except:
		start(perfil)

	lista_de_ads = {
        'anuncios' : []
    }
	lista_de_todas_fotos = []

	XPATH_TITLE_ADS = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[4]'
	XPATH_TITLE = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[2]'
	XPATH_PRECO = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[7]/div/div/h2'
	XPATH_DESC = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[17]/div/div[2]/div/p/span'
	XPATH_CATEG = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[4]/div/div[2]/span[2]'
	XPATH_ANO = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[5]/div/div[2]/a'
	XPATH_KM = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[6]/div/div[2]/span[2]'
	XPATH_PMOTOR = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[7]/div/div[2]/span[2]'
	XPATH_FUEL = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[8]/div/div[2]/a'
	XPATH_CAMBIO = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[9]/div/div[2]/span[2]'
	XPATH_DIREC = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[10]/div/div[2]/span[2]'
	XPATH_COR = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[11]/div/div[2]/span[2]'
	XPATH_PORT = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[12]/div/div[2]/span[2]'
	XPATH_PLACA = '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[30]/div/div[4]/div[13]/div/div[2]/span[2]'
	XPATH_PRODUTO = '//*[@id="__next"]/div[2]/div[2]/div[2]/div'

	produtos = r.html.xpath(XPATH_PRODUTO, first=True)
	count = 1
	count_list = 0

	try:
		for links in produtos.absolute_links:
			lista_fotos = []
			contents = s.get(links)
			foto = contents.html.find('div.sc-28oze1-12')
			for links_foto in foto:
				url_img = str(links_foto.find('img'))
				url = url_img.split("img' src='")
				url = url[1]
				url = url.split("' class=(")
				url = url[0]
				lista_fotos.append(url)
			else:
				lista_de_todas_fotos.append(lista_fotos)
				del lista_fotos

			title = contents.html.xpath(XPATH_TITLE, first=True).text
			title_ads = contents.html.xpath(XPATH_TITLE_ADS, first=True).text
			preco_ads = contents.html.xpath(XPATH_PRECO, first=True).text
			desc = contents.html.xpath(XPATH_DESC, first=True).text
			categ = contents.html.xpath(XPATH_CATEG, first=True).text
			ano = contents.html.xpath(XPATH_ANO, first=True).text
			km = contents.html.xpath(XPATH_KM, first=True).text
			pmotor = contents.html.xpath(XPATH_PMOTOR, first=True).text
			fuel = contents.html.xpath(XPATH_FUEL, first=True).text
			cambio = contents.html.xpath(XPATH_CAMBIO, first=True).text
			direc = contents.html.xpath(XPATH_DIREC, first=True).text
			cor = contents.html.xpath(XPATH_COR, first=True).text
			port = contents.html.xpath(XPATH_PORT, first=True).text
			final_placa = contents.html.xpath(XPATH_PLACA, first=True).text
			dict = {'ads':count,
				'title':title,
				'title_ads':title_ads,
				'url_img': lista_de_todas_fotos[count_list][:],
				'preco':preco_ads,
				'description':desc,
				'categ':categ,
				'ano':ano,
				'km':km,
				'potencia_motor':pmotor,
				'combustivel':fuel,
				'cambio':cambio,
				'direcao':direc,
				'cor':cor,
				'portas':port,
				'final_placa':final_placa}
					
			lista_de_ads['anuncios'].append(dict)
			count += 1
			count_list += 1
		else:
			return lista_de_ads
	except:
		start(perfil)