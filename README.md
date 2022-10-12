# STIM
Descrição do projeto.

## Como desenvolver?

1. Clone do repositório
2. Crie um virtualenv com Python 3.10
3. Ative o ambiente
4. Instale as dependências
5. Faça uma cópia do env_sample na raiz do projeto e configure as variáveis sensiveis
6. Execute as migrations
7. Crie um super usuário
8. Execute a aplicação

```console
git clone https://github.com/gomaaygo/stim.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp ENV_SAMPLE .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
