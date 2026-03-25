usuarios = ["admin", "convidado", "suporte", "teste"]

usuarios.remove ("teste")
del usuarios[0]

print (f"Lista atualizada: {usuarios}")