from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base
from model.produto import Produto


class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True)
    data_cadastro = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o comentário e um produto.
    # Aqui está sendo definido a coluna 'produto' que vai guardar
    # a referencia ao produto, a chave estrangeira que relaciona
    # um produto ao comentário.
    produto = Column(Integer, ForeignKey("produto.pk_produto"), nullable=False)

    def __init__(self, data_cadastro:Union[DateTime, None] = None):
        """
        Cria um Pedido

        Arguments:
            data_insercao: data de quando o pedido foi feito na base
        """
        if data_cadastro:
            self.data_cadastro = data_cadastro
            
    def adicionar_produto(self, produto:Produto):
        """
        Adiciona produto ao pedido

        Arguments:
            produto: produto que foi selecionado
        """
        self.produto = produto