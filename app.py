from flask import Flask, render_template

app = Flask(__name__)

# Simulação de Banco de Dados de Receitas
receitas_db = [
    {
        "id": 1,
        "nome": "Pudim de Leite Condensado",
        "categoria": "Sobremesa",
        "imagem": "images/pudim.jpg",
        "ingredientes": [
            "1 lata de leite condensado",
            "2 medidas de leite",
            "3 ovos",
            "1 xícara de açúcar (para a calda)"
        ],
        "preparo": "Derreta o açúcar para fazer a calda e espalhe na forma. Bata os outros ingredientes no liquidificador, despeje na forma e asse em banho-maria por 1 hora."
    },
    {
        "id": 2,
        "nome": "Pizza de Calabresa",
        "categoria": "Principal",
        "imagem": "images/pizza.jpg",
        "ingredientes": [
            "Massa de pizza",
            "Molho de tomate",
            "Queijo mussarela",
            "Calabresa fatiada",
            "Cebola",
            "Orégano"
        ],
        "preparo": "Abra a massa, espalhe o molho, adicione os ingredientes e asse em forno pré-aquecido a 220°C por cerca de 20 minutos."
    },
    {
        "id": 3,
        "nome": "Bolo de Chocolate",
        "categoria": "Sobremesa",
        "imagem": "images/bolo.jpg",
        "ingredientes": [
            "2 xícaras de farinha",
            "1 xícara de açúcar",
            "1 xícara de chocolate em pó",
            "3 ovos",
            "1 xícara de leite",
            "1 colher de fermento"
        ],
        "preparo": "Misture os ingredientes, coloque em forma untada e asse a 180°C por 35 minutos."
    },
    {
        "id": 4,
        "nome": "Mousse de Maracujá",
        "categoria": "Sobremesa",
        "imagem": "images/mousse.jpg",
        "ingredientes": [
            "1 lata de leite condensado",
            "1 caixa de creme de leite",
            "1 xícara de suco de maracujá"
        ],
        "preparo": "Bata tudo no liquidificador por 3 minutos e leve à geladeira por 2 horas."
    },
    {
        "id": 5,
        "nome": "Hambúrguer Caseiro",
        "categoria": "Lanches",
        "imagem": "images/hamburguer.jpg",
        "ingredientes": [
            "Carne moída",
            "Sal",
            "Pimenta",
            "Pão de hambúrguer",
            "Queijo",
            "Alface",
            "Tomate"
        ],
        "preparo": "Modele os hambúrgueres, frite ou grelhe e monte no pão com os acompanhamentos."
    },
    {
        "id": 6,
        "nome": "Lasanha à Bolonhesa",
        "categoria": "Principal",
        "imagem": "images/lasanha.jpg",
        "ingredientes": [
            "Massa de lasanha",
            "Carne moída",
            "Molho de tomate",
            "Queijo mussarela",
            "Presunto",
            "Molho branco"
        ],
        "preparo": "Monte camadas de massa, molho e recheio em uma travessa e asse por 30 minutos a 200°C."
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receitas')
def receitas():
    return render_template('receitas.html', receitas=receitas_db)

@app.route('/receita/<int:id>')
def receita_detalhe(id):
    # Busca a receita específica pelo ID
    receita = next((r for r in receitas_db if r['id'] == id), None)
    return render_template('detalhes_receita.html', receita=receita)

@app.route('/categorias')
def categorias():
    # Extrai categorias únicas
    lista_categorias = list(set(r['categoria'] for r in receitas_db))
    return render_template('categorias.html', categorias=lista_categorias)

if __name__ == '__main__':
    app.run(debug=True)