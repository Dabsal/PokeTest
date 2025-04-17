Testes Automatizados da API - PokeAPI Excel Generator

Este repositório contém um projeto em Flask que consome dados da [PokeAPI](https://pokeapi.co/) e gera um arquivo Excel com as informações dos Pokemons informados. Também inclui testes automatizados com `pytest` para validar os diferentes comportamentos da API.

---

Como executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação Flask

```bash
python main.py
```

A aplicação estará¡ disponível em:  
`http://localhost:8000/pokemon`

---

Como executar os testes automatizados

```bash
pytest test_poke.py --html=relatorio.html
```

O arquivo `relatorio.html` será¡ gerado com os resultados dos testes.

---

Mapeamento de Cenários de Teste

### Endpoint: `POST /pokemon`

| Cenário                        | Objetivo                                                                  |
|--------------------------------|---------------------------------------------------------------------------|
| IDs válidos                    | Validar se retorna status 200 e base64 de arquivo Excel válido           |
| Lista vazia                    | Validar se retorna status 200 e gera planilha sem conteúdo               |
| ID inexistente                 | Verificar se falhas da PokeAPI são tratadas                              |
| Tipo inválido no campo `json`  | Simular erro 500 por estrutura incorreta do payload                      |
| IDs negativos                  | Validar tratamento de entradas inválidas                                 |
| IDs decimais                   | Verificar se valores não inteiros causam erro ou são tratados            |
| Lista parcialmente válida      | Testar se apenas os válidos são processados                              |

---

Casos de Teste Implementados

| Teste                          | DescriÃ§Ã£o                                                                |
|--------------------------------|---------------------------------------------------------------------------|
| `test_post_valid_ids`          | Envia [1, 4, 7] e espera Excel válido                                     |
| `test_post_empty_list`         | Envia lista vazia e espera retorno 200                                   |
| `test_post_invalid_id`         | Envia ID 999999 e verifica se a API trata erro da PokeAPI                |
| `test_post_negative_id`        | Envia IDs negativos e espera retorno                                     |
| `test_post_not_all_valid_ids`  | Envia lista com IDs válidos e inválidos                                  |
| `test_post_decimal_id`         | Envia IDs com ponto flutuante (ex: 2.2)                                   |
| `test_post_invalid_type`       | Envia string no lugar de lista e espera erro 500                         |

---

Exemplo de Requisição (Postman ou Python)

```json
POST /pokemon
Content-Type: application/json

{
  "json": [1, 4, 7],
  "filename": "starter_pokemon.xlsx"
}
```

**Resposta esperada:**

```json
{
  "excel_base64": "<base64_do_arquivo_excel>"
}
```

---

Autor

Davi Brandão Saldanha 
Simulador de testes automatizados com API REST e PokeAPI.
