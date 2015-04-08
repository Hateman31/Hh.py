import urllib.request #избавиться
# import request #использвать это
import json

class API:
	def query(self,query=''):
		base = 'https://api.hh.ru/'
		# r = requests.get(base+query, params=None)
		r = urllib.request.urlopen(base+query)
		return json.loads(r.read().decode('utf8'))
		# return json.loads(r.json())
	def vacancies(params):
		''' Функция поиска по вакансиям'''
		return self.query('vacancies/'+params)
		#написать функцию перевода словаря params в get-запрос
		#{ key1:value1,key2:value2 }  ==> <uri>?key1=value1&key2=value2
	#def 
if __name__ == '__main__':
    pass
