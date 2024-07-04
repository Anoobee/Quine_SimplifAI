from mindsdb_sdk import connect

def create_ml_engine(server):
    try:
        server.ml_engines.create(
            'ollama_engine',
            'ollama',
            connection_data={
                'ollama_serve_url': 'http://172.17.0.1:11434'
            }
        )
        print("ML engine created successfully")
    except Exception as e:
        print(f"Error creating ML engine: {str(e)}")

def create_model(server):
    try:
        model = server.models.create(
            name='simplifai',
            predict='completion',
            engine='ollama_engine',
            model_name='anoob/simp2:latest',
            ollama_serve_url='http://172.17.0.1:11434'
        )
        print("Model created successfully")
        return model
    except Exception as e:
        print(f"Error creating model: {str(e)}")
        return None

def connect_to_mindsdb():
    try:
        server = connect('http://127.0.0.1:47334')
        return server
    except Exception as e:
        print(f"Error connecting to MindsDB: {str(e)}")
        return None

def setup_mindsdb():
    server = connect_to_mindsdb()
    if server:
        create_ml_engine(server)
        model = create_model(server)
        return server, model
    return None, None


if __name__ == "__main__":
    server, model = setup_mindsdb()
