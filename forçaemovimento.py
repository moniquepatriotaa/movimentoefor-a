scene = canvas(width=800, height=600)

aceleracao = 3.58
dt = 0.01

link1 = vector(0, 0, 5)
link2 = vector(2, 3, 5)
link3 = vector(0, 5, 5)
link4 = vector(2, 5, 5)

polia = cylinder(pos=vector(1, 5, 5), axis=vector(0, 0, 2), radius=1)
bloco1 = box(pos=link1, size=vector(1, 1, 1), color=color.cyan, mass=1.3)
bloco2 = box(pos=link2, size=vector(1, 1, 1), color=color.orange, mass=2.8)

# Criação dos rótulos das massas dos blocos
rotulo_bloco1 = label(pos=link1, text=f"Massa: {bloco1.mass} kg", xoffset=-20, yoffset=40, space=30, color=color.cyan)
rotulo_bloco2 = label(pos=link2, text=f"Massa: {bloco2.mass} kg", xoffset=-20, yoffset=40, space=30, color=color.orange)

corda = curve(link1, link3, link4 , link2)


def atualizarBloco(bloco, link):
    bloco.pos.y = link.y

while True:
    rate(100) 
    
    if link1.y >= 3.5:
        break
    
    aceleracao_bloco1 = aceleracao * bloco2.mass / (bloco1.mass + bloco2.mass)
    aceleracao_bloco2 = -aceleracao * bloco1.mass / (bloco1.mass + bloco2.mass)
    
    link1.y += aceleracao_bloco1 * dt
    link2.y += aceleracao_bloco2 * dt
    atualizarBloco(bloco1, link1)
    atualizarBloco(bloco2, link2)
    
    corda.clear()
    corda = curve(link1, link3, link4 , link2)
    
    # Atualização dos rótulos das massas dos blocos
    rotulo_bloco1.pos = link1 + vector(0, 0.5, 0)
    rotulo_bloco1.text = f"Massa: {bloco1.mass} kg"
    
    rotulo_bloco2.pos = link2 + vector(0, 0.5, 0)
    rotulo_bloco2.text = f"Massa: {bloco2.mass} kg"
