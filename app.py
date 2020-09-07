

from flask import Flask, render_template, request, url_for, jsonify
from http import HTTPStatus
from calcul import les_choix, sommaire

app = Flask(__name__)

total = sommaire.to_dict()



@app.route("/")
def index():
	return render_template('index.html')


@app.route("/classement", methods=['GET', 'POST'])
def classement():
	return render_template('classement.html',total=total)

@app.route("/pointage")
def pointage():
	return render_template('pointage.html')

@app.route('/classement/<pooler_name>', methods=['GET'])
def get_pooler_point(pooler_name):
	try:
		pooler = sommaire.loc[pooler_name]
		#pooler = next((index for index in sommaire.iterrows() == pooler_name), None)
		pooler = pooler.to_dict()
		
		
	except:
		return 'Il n\'y a pas de pooler de ce nom'
	les_choix_pooler = les_choix[les_choix['pooler'] == pooler_name]
	les_choix_pooler = les_choix_pooler.to_dict()
	pooler_complet = {'sommaire': pooler, 'choix': les_choix_pooler }
	return jsonify(pooler_complet)




if __name__ == '__main__':
	app.run()