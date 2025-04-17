import json
import requests
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify
from pokemon import Pokemon
from excel import Excel

app = Flask(__name__)

def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data["sprites"]["front_default"]
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            return Pokemon(
                name=data["name"].capitalize(),
                pokemon_id=data["id"],
                types=[t["type"]["name"] for t in data["types"]],
                image_data=image_response.content
            )
    else:
        raise Exception(f'PokeAPI retornou erro {response.status_code} para o ID {pokemon_id}')    
    return None

@app.route('/pokemon', methods=['POST'])
def generate_pokemon_excel():
    data = request.json

    try:
        numeros = data.get('json', [])  # Se 'json' não estiver presente, use uma lista vazia
        pokelist = []

        # Consulta a API para cada numero (ID de Pokemon) na lista e extrai dados
        with ThreadPoolExecutor() as executor:
            results = executor.map(get_pokemon_data, numeros)
            for result in results:
                if result:
                    pokelist.append(result)

        filename = data.get('filename', 'pokedata.xlsx')
        
        # Escreve os dados em uma planilha do Excel
        Excel.write_to_excel(pokelist, filename)
        #Converte o Excel gerado em base64
        excel64 = Excel.excel_to_base64(filename)

        return jsonify({'excel_base64': excel64})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
