# App do Café

O app do café é um projeto voltado para fomentar o comercio do café no Espirito Santo. 
Foi desenvolvida uma aplicação web para comportar as funcionalidades do app. Através da aplicação podem ser criados anúncios mediantes a um registro no site, anúncios estes que permitem gerar demandas de venda ou compra dos três tipos de saca de café comercializado no estado do Espirito Santo ( Arábica Dura, Arábica Rio, Conillon).

## Como usar

A aplicação e suas funcionalidades podem ser acessadas publicamente neste [link](cafe-app-pi.herokuapp.com).

Além disso a documentação está disponivel através do github Pages [link](https://vitorbonella.github.io/ProjetoIntegrado1-2021-1/).

## Como contribuir

### Ambiente de Desenvolvimento

Primeiro temos que clonar o repositório.
```
git clone https://github.com/VitorBonella/ProjetoIntegrado1-2021-1
```
Depois basta fazer o build, que já instala automaticamente todas dependências.
```
python setup.py install
```
Para rodar o servidor de teste basta executar
```
python run.py
```
OBS: *Caso queira que as mudanças no código feitas reflitam sem que seja necessário reiniciar o servidos bastar acessar o arquivo config.py e alterar a variável Debug = True*

### Como contribuir

Para contribuir basta dar um commit, que depois de revisado pelos criadores do app, irá ser incluído ou não ao projeto.

É importante que sejam realizados teste antes de enviar, para realizar o teste use os comandos:

```
pytest -v test/ 
```

## Versions

|Data|Versão|Log|
|--|--|--|
|01/10/2021|1.0|Primeira Versão |
|08/10/2021|1.0|Documentação Final Lançada|

## License

Esta aplicação possui a licença do MIT :
Uma licença permissiva curta e simples com condições que exigem apenas a preservação de direitos autorais e avisos de licença. Obras licenciadas, modificações e obras maiores podem ser distribuídas em termos diferentes e sem código-fonte.

## Sobre Nós

Este trabalho for feito por Luis Eduardo Camara e Vitor Bonella para a matéria de Projeto Integrado I 2021/1.

**Luis Eduardo Camara**: Graduando desde 2019 em Ciência da Computação na Universidade Federal do Espirito Santo. Áreas de Interesse: Programação Competitiva.

**Vitor Bonella**: Graduando desde 2019 em Ciência da Computação na Universidade Federal do Espirito Santo.  Áreas de Interesse: Aprendizado de Máquina, Ciência de Dados, Redes de Computadores.