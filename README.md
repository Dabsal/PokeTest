Testes Automatizados da API - PokeAPI Excel Generator

Este reposit�rio cont�m um projeto em Flask que consome dados da [PokeAPI](https://pokeapi.co/) e gera um arquivo Excel com as informa��es dos Pokemons informados. Tamb�m inclui testes automatizados com `pytest` para validar os diferentes comportamentos da API.

---

Como executar a API

### 1. Clone o reposit�rio

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as depend�ncias

```bash
pip install -r requirements.txt
```

### 3. Execute a aplica��o Flask

```bash
python main.py
```

A aplica��o estar� dispon�vel em:  
`http://localhost:8000/pokemon`

---

Como executar os testes automatizados

```bash
pytest test_poke.py --html=relatorio.html
```

O arquivo `relatorio.html` ser� gerado com os resultados dos testes.

---

Mapeamento de Cen�rios de Teste

### Endpoint: `POST /pokemon`

| Cen�rio                        | Objetivo                                                                  |
|--------------------------------|---------------------------------------------------------------------------|
| IDs v�lidos                    | Validar se retorna status 200 e base64 de arquivo Excel v�lido           |
| Lista vazia                    | Validar se retorna status 200 e gera planilha sem conte�do               |
| ID inexistente                 | Verificar se falhas da PokeAPI s�o tratadas                              |
| Tipo inv�lido no campo `json`  | Simular erro 500 por estrutura incorreta do payload                      |
| IDs negativos                  | Validar tratamento de entradas inv�lidas                                 |
| IDs decimais                   | Verificar se valores n�o inteiros causam erro ou s�o tratados            |
| Lista parcialmente v�lida      | Testar se apenas os v�lidos s�o processados                              |

---

Casos de Teste Implementados

| Teste                          | Descrição                                                                |
|--------------------------------|---------------------------------------------------------------------------|
| `test_post_valid_ids`          | Envia [1, 4, 7] e espera Excel v�lido                                     |
| `test_post_empty_list`         | Envia lista vazia e espera retorno 200                                   |
| `test_post_invalid_id`         | Envia ID 999999 e verifica se a API trata erro da PokeAPI                |
| `test_post_negative_id`        | Envia IDs negativos e espera retorno                                     |
| `test_post_not_all_valid_ids`  | Envia lista com IDs v�lidos e inv�lidos                                  |
| `test_post_decimal_id`         | Envia IDs com ponto flutuante (ex: 2.2)                                   |
| `test_post_invalid_type`       | Envia string no lugar de lista e espera erro 500                         |

---

Exemplo de Requisi��o (Postman ou Python)

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

Davi Brand�o Saldanha 
Simulador de testes automatizados com API REST e PokeAPI.
