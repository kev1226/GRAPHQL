from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema

# Define el esquema de GraphQL
class Query(ObjectType):
    hello = String(description="Una consulta que devuelve un saludo")

    def resolve_hello(parent, info):
        return "¡Hola, Mundo desde GraphQL en Python!"

schema = Schema(query=Query)


# Configuración del servidor Flask
app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Habilita la interfaz gráfica de GraphQL
    )
)

@app.route('/')
def home():
    return "Bienvenido a la API GraphQL. Ve a http://127.0.0.1:5000/graphql para usar la interfaz."


if __name__ == '__main__':
    app.run(port=5000, debug=True)
