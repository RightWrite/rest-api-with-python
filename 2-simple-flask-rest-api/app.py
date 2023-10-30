from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

# Swagger configuration
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Create a Swagger UI blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Backstage POC REST API  using Flask"
    }
)

# Register the Swagger UI blueprint
app.register_blueprint(swaggerui_blueprint)

# Sample data
stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "chair",
                "price": 15.99
            }
        ]
    }
]



# Endpoint to get a list of stores
@app.route("/store", methods=['GET'])
def get_stores():
    """
    Get a list of stores.
    ---
    responses:
      200:
        description: A list of stores.
    """
    return {"stores": stores}


# Endpoint to create a new store
@app.route("/store", methods=['POST'])
def create_store():
    """
    Create a new store.
    ---
    parameters:
      - in: body
        name: store
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      201:
        description: The newly created store.
    """
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


# Endpoint to create a new item in a store
@app.route("/store/<string:name>/item", methods=['POST'])
def create_item(name):
    """
    Create a new item in a store.
    ---
    parameters:
      - in: path
        name: name
        type: string
        required: true
      - in: body
        name: item
        schema:
          type: object
          properties:
            name:
              type: string
            price:
              type: number
    responses:
      201:
        description: The newly created item.
      404:
        description: Store not found.
    """
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201

    return {"message": "Store not found"}, 404


# Endpoint to get details of a specific store
@app.route("/store/<string:name>", methods=['GET'])
def get_store(name):
    """
    Get details of a specific store.
    ---
    parameters:
      - in: path
        name: name
        type: string
        required: true
    responses:
      200:
        description: Details of the store.
      404:
        description: Store not found.
    """
    for store in stores:
        if store["name"] == name:
            return store

    return {"message": "Store not found"}, 404


# Endpoint to get items in a specific store
@app.route("/store/<string:name>/item", methods=['GET'])
def get_items_in_store(name):
    """
    Get items in a specific store.
    ---
    parameters:
      - in: path
        name: name
        type: string
        required: true
    responses:
      200:
        description: Items in the store.
      404:
        description: Store not found.
    """
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404


# Generate Swagger JSON
@app.route('/swagger')
def generate_swagger():
    swag = swagger(app, from_file_key='swagger')
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Backstage POC REST API using Flask"
    return swag

# if __name__ == '__main__':
#     app.run(debug=True)

