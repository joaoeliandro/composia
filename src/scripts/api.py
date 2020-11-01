import json
from aitextgen import aitextgen
from flask import Flask, request, jsonify



# importa o modelo
ai = aitextgen(model="models/pytorch_model_luiz_gonzaga.bin", config="models/config_luiz_gonzaga.json")




# cria a API
app = Flask("composia")


@app.route("/estrofe", methods=["GET"])
def estrofe():
    text_raw = ai.generate_one(batch_size=100,
                        prompt=request.args['input'],
                        max_length=100,
                        temperature=1.5,
                        top_k=0,
                        top_p=1)
                      
    text_clean = {'estrofe': text_raw.split('\n')[:-1]}
    return text_clean

app.run()
