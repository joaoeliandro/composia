<h1 align="center">
    <img src="https://res.cloudinary.com/dy7l1wk3y/image/upload/v1604272538/Group_172_g6kyur.png" alt="plataform-composia" />
    <br>
    ComposIA: conexões criativas entre fãs e artistas
    <br>
</h1>

<h4 align="center">
  Uma plataforma que usa da tecnologia para aprimorar a interação entre fãs e artistas durante a produção musical.
</h4>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/joaoeliandro/composia.svg">

  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/joaoeliandro/composia.svg">

  <a href="https://www.codacy.com/app/joaoeliandro/composia?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=joaoeliandro/composia&amp;utm_campaign=Badge_Grade">
    <img alt="Codacy grade" src="https://api.codacy.com/project/badge/Grade/691b85e51bf240b997ae6ff82ea41590">
  </a>

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/joaoeliandro/composia.svg">
  <a href="https://github.com/joaoeliandro/composia/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/joaoeliandro/composia.svg">
  </a>

  <a href="https://github.com/joaoeliandro/composia/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/joaoeliandro/composia.svg">
  </a>

  <a href="https://github.com/joaoeliandro/composia/blob/master/LICENSE">
    <img alt="GitHub License" src="https://img.shields.io/github/license/joaoeliandro/composia.svg">
  </a>
</p>

<p align="center">
  <a href="#octocat-o-projeto">O Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#information_source-como-utilizar">Como utilizar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>

## Sobre

**Já imaginou ouvir uma música daquele artista que tanto ama mais uma vez ou ajudar aquele artista que não sai da sua playlist a criar uma nova música?**
> **ComposIA**, uma plataforma que usa Inteligencia Artificial para aprimorar a interação entre fãs e artistas durante a produção musical, com um intuito de melhorar a experiência do fã e ajudar artistas com novos sucessos criados pelos próprios fãs. Aqui, é usado:
> - Javascript
> - Node
> - ExpressJs
> - Python 3
> - Flask Framework
> - Pytorch-lightning
> - GPT-2 (Rede Neural)
> - Google Colab
> - API Genius
> - Pacote Iatextgen
>
> Entre outras funcionalidades.

---

## :octocat: O Projeto

<h3 align="center">Aplicação mobile do ComposIA</h3>
<p align="center">
    <img src="https://drive.google.com/uc?export=view&id=15krmtBk-AjxkCl4PiwAQFWk3TpOVPjO1" alt="composia-demo" />
</p>

<h3 align="center">Serviço de inteligencia artificial do ComposIA</h3>
<p align="center">
    <img src="https://drive.google.com/uc?export=view&id=1o_9oDsJnDwMpD-LJvYs4_01SGvnDfOmj" alt="composia-demo" />
</p>

---

Veja também uma letra organizada por nós e feita inteiramente com a Inteligencia Artificial simulando Luiz Gonzaga na composição, aqui:

<h3 align="center">Letra para uma composição gerada pelo ComposIA</h3>
<p align="center">
    <img src="https://res.cloudinary.com/dy7l1wk3y/image/upload/v1604281378/WhatsApp_Image_2020-11-01_at_22.37.47_h7xl60.jpg" alt="composia-lyrics-demo" />
</p>

## :rocket: Tecnologias

Esta plataforma foi desenvolvida com as seguintes tecnologias:

> - [NodeJS](https://nodejs.org)
> - [Python](https://www.python.org/)
> - [VS Code](https://code.visualstudio.com/)
> - [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true)
> - E outras tecnologias...

## :information_source: Como utilizar

Para clonar e executar esta api, você precisará do [Git](https://git-scm.com), [Node.js v12.18][nodejs] acima + [Yarn v1.22][yarn] acima, [Python v3.7][python], [Pip v20.2.4](https://pypi.org/project/pip/) instalado no seu computador, copie a url do [composia](https://github.com/joaoeliandro/composia) e clone na sua máquina.

Baixe também os modelos de um artista inicialmente do Luiz Gonzaga [Modelo](https://we.tl/t-rOC10fnmeT).

No seu terminal:

```bash
# Clone este repositório
$ git clone https://github.com/joaoeliandro/composia.git

# Entre no repositório clonado
$ cd composia

# Instale as dependências da api do Node
$ yarn

# Entre na pasta scripts e instale os pacotes do python
$ cd src/scripts
$ pip install flask
$ pip install -q aitextgen
$ pip install pytorch-lightning==0.8.4

# Copie e cole os modelos baixados do Luiz Gonzaga dentro da pasta models

# Entre na pasta scripts dentro de src e execute o servidor python
$ cd src/scripts
$ python api.py

# Execute e utilize usando a rota passando uma palavra qualquer Ex.: (http://localhost:3333/estrofe?input=felicidade)
$ yarn start
```

## :memo: Licença

Este projeto está sob o MIT license. Veja a [LICENSE](https://github.com/joaoeliandro/composia/blob/master/LICENSE) para mais informações.

[nodejs]: https://nodejs.org/
[yarn]: https://yarnpkg.com/
[python]: https://www.python.org/downloads/release/python-370/
