Feature: Buscar productos en MercadoLibre

  Scenario: Verificar búsqueda de iPhone 13
    Given que el usuario está en la página de inicio de MercadoLibre
    When busca el producto "iPhone 13"
    Then se muestran resultados que contienen "iPhone"
