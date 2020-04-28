import web
import app
import json
import csv

class Alumnos:
	file="/static/csv/alumnos.csv"
	version="1.0.0"
	def __init__(self):
		pass

	def GET(self):
		try:
			datos=web.input()
			if datos['token']=="1234": 
				
				if datos['action']=="get": 
					resultAB=self.actionGet(self.version,self.file)
					return json.dumps(resultAB) 
				
				elif datos['action']=="search":
					matricula=datos['matricula']
					resultAB=self.actionSearch(self.version,self.file,matricula)
					return json.dumps(resultAB) 
				
				elif datos['action']=="put": #insertar
					matricula=datos['matricula']
					nombre=datos['nombre']
					primer_apellido=datos['apellido1']
					segundo_apellido=datos['apellido2']
					carrera=datos['carrera']
					resultAB=self.actionInput(self.version,self.file,matricula,nombre,primer_apellido,segundo_apellido,carrera)
					return json.dumps(resultAB)#
				
				elif datos['action']=="delete":
					matricula=datos['matricula']
					resultAB=self.actionDelete(self.version,self.file,matricula)
					return json.dumps(resultAB) 
				else: 
					resultAB={}
					resultAB['status']="Command not match, try again"
					return json.dumps(resultAB)
			else: #por si el token es incorrecto
				resultA={}
				resultA['status']="Token invalido"
				return json.dumps(resultA)
		except Exception as e:
			resultA={}
			resultA['status']="Ingresa valores validos, revisa"
			return json.dumps(resultA)

#GET
	@staticmethod
	def actionGet(version,file):
		try:
				resultA=[]
				resultAB={}
				with open('static/csv/alumnos.csv','r') as csvfile: #csv
					reader = csv.DictReader(csvfile)
					for row in reader: 
						resultA.append(row)
						resultAB['version']=version
						resultAB['status']="200 ok" 
						resultAB['alumnos']=resultA
				return resultAB 
		except Exception as e: 
			resultA={}
			resultA['version']=version
			resultA['status']="Error"
			return json.dumps(resultA)
	
#SEARCH
	@staticmethod
	def actionSearch(version,file,matricula):
		try:
				resultA=[]
				resultAB={}
				with open('static/csv/alumnos.csv','r') as csvfile: 
					reader = csv.DictReader(csvfile)
					for row in reader:
						if(matricula==row['matricula']): 
							print(matricula)
							resultA.append(row) 
							resultAB['version']=version
							resultAB['status']="200 ok"
							resultAB['alumnos']=resultA
							break
						else:
							resultAB={}
							resultAB['status']="matricula no encontrada" 
				return resultAB 
		except Exception as e: 
			resultA={}
			resultA['version']=version
			resultA['status']="Error"
			return json.dumps(resultA)


#INPUT
	@staticmethod
	def actionInput(version,file,matricula,nombre,primer_apellido,segundo_apellido,carrera):
		try:
			resultA=[]
			resultAIN=[]
			resultAB={}
			resultAIN.append(matricula)
			resultAIN.append(nombre)
			resultAIN.append(primer_apellido)
			resultAIN.append(segundo_apellido)
			resultAIN.append(carrera)
			with open('static/csv/alumnos.csv','a',newline='') as csvfile: 
				writer=csv.writer(csvfile)
				# The writerow() method writes a row of data into the specified file
				writer.writerow(resultAIN)
			with open('static/csv/alumnos.csv','r') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					resultA.append(row)
					resultAB['version']=version
					resultAB['status']="200 ok" 
					resultAB['alumnos']=resultA
			return resultAB 
		except Exception as e:
			resultA={} 
			resultA['version']=version
			resultA['status']="Error"
			return json.dumps(resultA)

	@staticmethod
	def actionDelete(file, matricula):
		try:
			result = []
			resultC = {}
			with open('static/csv/alumnos.csv', 'r') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					if(row['matricula'] != matricula):
						resultC['status'] = "200 Ok"
						result.append(row)
						resultC['alumnos'] = result
			longitud = (len(result))
			with open('static/csv/alumnos.csv', 'w', newline='') as csvfile:
				writer = csv.writer(csvfile)
				bye = []
				bye.append("matricula")
				bye.append("nombre")
				bye.append("primer_apellido")
				bye.append("segundo_apellido")
				bye.append("carrera")
				writer.writerow(bye)
				data = []
				for x in range(0, longitud):
					data.append(result[x]['matricula'])
					data.append(result[x]['nombre'])
					data.append(result[x]['primer_apellido'])
					data.append(result[x]['segundo_apellido'])
					data.append(result[x]['carrera'])
					writer.writerow(data)
					data = []
			results = []
			resultsC = {}
			with open('static/csv/alumnos.csv', 'r') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					results.append(row)
					resultsC['status'] = "200 Ok"
					resultsC['alumnos'] = result
			return resultsC
		except Exception as e:
			result = {}
			result['status']="Error"
		return result
