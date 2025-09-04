from langchain.chat_models import init_chat_model


def get_chat_model(model="gemini-2.5-flash-lite", model_provider="google_vertexai"):
    """ Chat model

    Args:
        model (str, optional): _description_. Defaults to "gemini-2.5-flash-lite".
        model_provider (str, optional): _description_. Defaults to "google_vertexai".

    Returns:
        _type_: _description_
    """
    return init_chat_model(model=model,model_provider=model_provider)