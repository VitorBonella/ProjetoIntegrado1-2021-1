

def test_index_page(test_app):
    """
    Testando pagina principal
    """
    assert test_app.get('/').status_code == 200


def test_infocafe_page(test_app):
    """
    Testando pagina de informações
    """
    assert test_app.get('/infocafe/geral').status_code == 200


def test_login_page(test_app):
    """
    Testando pagina de login
    """
    response = test_app.get('/login').status_code

    assert response == 200


def test_register_page(test_app):
    """
    Testando pagina de registro
    """
    response1 = test_app.get('/signup').status_code
    response2 = test_app.get('/register').status_code

    assert response1 == 200 and response2 == 200
