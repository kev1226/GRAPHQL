# GraphQL Hola Mundo en Python

Este proyecto es un ejemplo básico de un servidor GraphQL utilizando Flask y Graphene en Python.

## Cómo usar

1. **Instala las dependencias**:
   ```bash
   pip install flask flask-graphql graphene
   ```

2. **Ejecuta el servidor**:
   ```bash
   python app.py
   ```

3. **Accede a la interfaz de GraphQL**:
   ```
   http://localhost:5000/graphql
   ```

4. **Prueba la consulta**:
   En la interfaz de GraphQL, ejecuta la siguiente consulta:
   ```graphql
   {
     hello
   }
   ```
   Deberías obtener la respuesta:
   ```json
   {
     "data": {
       "hello": "¡Hola, Mundo desde GraphQL en Python!"
     }
   }
   ```

## Uso de ngrok

1. **Configura ngrok**:
   ```bash
   ./ngrok.exe config add-authtoken 2paOcYZfXpFBNZomR8oIeU9q6O2_452i8m58SWgrcyRxG1iht
   ```

2. **Expon el servidor**:
   ```bash
   ./ngrok.exe http 5000
   ```

3. **Usa la URL generada** para acceder a tu API desde cualquier lugar.