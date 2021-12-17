### Clientes-APP

Esta aplicação retorna informações de clientes e também retorna o tamanho de um payload envaido a ela.

|método | chamada | payload | retorno |
|------|------|---------|---------|
|GET| / | - |Mensagem "hello world" | 
|GET| /clientes | - |json - todos os clientes cadastrados na aplicação response | 
|GET| /clientes/{id} | - |json - retorna um clientes especifico relacionado ao id requisitado |
|POST| /clientes | id,nome,email,endereco | Sucesso ou erro ao criar um novo cliente |
|POST| /payloadprint | payload json | Tamanho do payload enviado |


Esta aplicação de teste tem a finalidade de servir como base para estudos DevOps de deployment, CI e afins. 