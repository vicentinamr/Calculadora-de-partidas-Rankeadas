def calcular_saldo_ranked(vitorias, derrotas):
  """
  Calcula o saldo de partidas ranqueadas de um jogador.

  Args:
    vitorias: Quantidade de vitórias do jogador.
    derrotas: Quantidade de derrotas do jogador.

  Returns:
    O saldo de partidas ranqueadas do jogador.
  """

  saldo_vitorias = vitorias - derrotas
  nivel = None

  if saldo_vitorias < 10:
    nivel = "Ferro"
  elif saldo_vitorias < 21:
    nivel = "Bronze"
  elif saldo_vitorias < 51:
    nivel = "Prata"
  elif saldo_vitorias < 81:
    nivel = "Ouro"
  elif saldo_vitorias < 91:
    nivel = "Diamante"
  elif saldo_vitorias < 101:
    nivel = "Lendário"
  else:
    nivel = "Imortal"

  return saldo_vitorias, nivel

