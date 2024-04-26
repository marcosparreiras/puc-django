# CRUD de estudantes com o Django

## Modelo de dados

```sql
CREATE TABLE Student (
    student_code INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at DATE DEFAULT CURRENT_TIMESTAMP,
    address_street VARCHAR(80) NOT NULL,
    address_number INT NOT NULL
);
```

## Teste a aplicação em sua máquina

Certifique-se de ter o Docker instalado em sua máquina antes de prosseguir.

- [Docker](https://www.docker.com/)

1. Faça o clone do projeto

```bash
git clone https://github.com/marcosparreiras/puc-django.git
```

2. Navegue até diretório do projeto e execute os containers docker com o comando:

```bash
docker compose up -d --build
```

3. Verifique a os containers foram executados com sucesso com o comando:

```bash
docker compose logs
```

4. Com os conatiners em execução, você pode:

- Testar a API REST (Uma breve documentação das rotas se encontra no arquivo `api.http`).
- Acessar a aplicação pela rota:

```bash
http://localhost:8000/api/student/app/home
```
