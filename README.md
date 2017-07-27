# Etapas da pipeline de processamento de dados

1. Captação de dados do banco Mysql
2. Armazenamento em formato processável
3. Validação e Transformação dos dados
4. Formatação dos dados em outra estrutura de dados
5. Convergência das estruturas de dados em uma única estrutura
6. Enriquecimento do dataset com informações vindas do Elasticsearch

## Iniciando o worker do Celery

    celery -A updater worker -l info

## Testando as tasks criadas

Abrir o `ipython` em um terminal e executar as seguintes instruções:

    > from updater.tasks import query_rows, jsonify_records
    > (query_rows.s('SELECT * FROM processo') | jsonify_records.s(('soi', 'tipo', 'juizado', 'classe')))()
