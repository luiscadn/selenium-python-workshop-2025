Feature: Verificar el título de un artículo en Wikipedia

  Scenario: Buscar "Python (lenguaje de programación)" y validar el título
    Given que el usuario está en la página de inicio de Wikipedia
    When busca el término "Python (lenguaje de programación)"
    Then el título del artículo debe ser "Python (lenguaje de programación)"
