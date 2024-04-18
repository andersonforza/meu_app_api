from pydantic import BaseModel

from model.pedido import Pedido
from schemas.produto import ProdutoSchema


class PedidoSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    produto_id: int = 1
    
    
class PedidoViewSchema(BaseModel):
    """ Define como um pedido será retornado para o cliente
    """
    id: int = 1
    produto: ProdutoSchema    
    
def apresenta_pedido(pedido: Pedido):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": pedido.id,
        "data_cadastro": pedido.data_cadastro,
        "produto": pedido.produto.description
    }          