from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    descricao = Column(String(140), unique=True)
    valor = Column(Float)
    disponivel = Column(Boolean, default=True)
    data_cadastro = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o produto e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.

    def __init__(self, descricao:str, valor:float, disponivel: Union[bool, None] = None,
                 data_cadastro:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            descricao: descricao do produto.
            quantidade: quantidade que se espera comprar daquele produto
            valor: valor esperado para o produto
            disponivel: indicador se o produto estará disponível para venda
            data_insercao: data de quando o produto foi inserido à base
        """
        self.descricao = descricao
        self.valor = valor

        # se não for informada, será o data exata da inserção no banco
        if data_cadastro:
            self.data_insercao = data_cadastro
            
        if disponivel:
            self.disponivel = True
