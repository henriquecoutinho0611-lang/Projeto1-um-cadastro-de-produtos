import pygame
import sys
import math
import random
import time
# ==========================================
# 1. INICIALIZAÇÃO E CONFIGURAÇÕES DE PC
# ==========================================
pygame.init()

LARG, ALT = 1920, 1080  # Resolução widescreen ideal para PC
tela = pygame.display.set_mode((LARG, ALT))
pygame.display.set_caption("🔫 DOOM 3D - PC EDITION")
relogio = pygame.time.Clock()

# Paleta de Cores
PRETO = (0, 0, 0)
VERM = (220, 30, 30)
ROXO_CHEFE = (160, 20, 220)
BRANCO = (255, 255, 255)
VERDE = (40, 220, 80)
AMARELO = (255, 200, 0)
while True:
# ==========================================
# 2. GERADOR DE TEXTURAS HD PROCEDURAIS
# ==========================================
 def criar_textura(tipo):
    surf = pygame.Surface((128, 128))
    if tipo == 1:  # Tijolos de Pedra
        surf.fill((70, 70, 80))
        for y in range(0, 128, 32):
            pygame.draw.line(surf, (30, 30, 40), (0, y), (128, y), 3)
            offset = 32 if (y // 32) % 2 != 0 else 0
            for x in range(offset, 128, 64):
                pygame.draw.line(surf, (30, 30, 40), (x, y), (x, y+32), 3)
                pygame.draw.line(surf, (100, 100, 110), (x+2, y+2), (x+62, y+2), 2)
    elif tipo == 2:  # Metal Tecnológico
        surf.fill((40, 50, 60))
        pygame.draw.rect(surf, (20, 25, 30), (8, 8, 112, 112), 6)
        pygame.draw.circle(surf, (0, 150, 255), (64, 64), 25)
        pygame.draw.circle(surf, (255, 255, 255), (64, 64), 10)
        for ponto in [(20,20), (108,20), (20,108), (108,108)]:
            pygame.draw.circle(surf, (90, 100, 110), ponto, 6)
    elif tipo == 3:  # Parede do Chefe
        surf.fill((60, 15, 15))
        for _ in range(40):
            p1 = (random.randint(0,128), random.randint(0,128))
            p2 = (p1[0] + random.randint(-20,20), p1[1] + random.randint(-20,20))
            pygame.draw.line(surf, (120, 20, 20), p1, p2, random.randint(2,5))
        for y in range(0, 128, 16):
            pygame.draw.line(surf, (30, 5, 5), (0, y), (128, y), 2)
    return surf.convert()

 TEXTURAS = {1: criar_textura(1), 2: criar_textura(2), 3: criar_textura(3)}
 TAM_TEX = 128
 TAM_BLOCO = 64

# ==========================================
# 3. MAPA DO JOGO
# ==========================================
 MAPA = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,2,0,1,1,1,0,2,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],
    [1,2,2,0,1,0,2,0,1,1,1,1,1,1,0,1,2,2,0,1],
    [1,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# ==========================================
# 4. ENTIDADES: JOGADOR E INIMIGOS
# ==========================================
 class Jogador:
    def __init__(self):
        self.x, self.y = 1.5 * TAM_BLOCO, 1.5 * TAM_BLOCO
        self.z = 0.0          
        self.vel_z = 0.0
        self.pitch = 0.0      
        self.angulo = 0.0
        self.vel_andar = 4.5
        self.vel_girar = 0.05
        self.vida = 100
        self.municao = 60
        self.arma_anim = 0
        self.dano_tela = 0 
        self.andando = False
        self.no_chao = True

    def mover(self, dx, dy):
        sen, cos = math.sin(self.angulo), math.cos(self.angulo)
        mov_x = cos * dx - sen * dy
        mov_y = sen * dx + cos * dy
        self.andando = (abs(dx) > 0 or abs(dy) > 0)
        
        nx = int((self.x + mov_x + (15 if mov_x > 0 else -15)) / TAM_BLOCO)
        ny = int((self.y + mov_y + (15 if mov_y > 0 else -15)) / TAM_BLOCO)
        
        if MAPA[int(self.y / TAM_BLOCO)][nx] == 0: self.x += mov_x
        if MAPA[ny][int(self.x / TAM_BLOCO)] == 0: self.y += mov_y

    def girar(self, valor):
        self.angulo += valor

    def pular(self):
        if self.no_chao:
            self.vel_z = 12.0
            self.no_chao = False

    def atualizar_fisica(self):
        if not self.no_chao:
            self.z += self.vel_z
            self.vel_z -= 1.0  
            if self.z <= 0.0:
                self.z = 0.0
                self.vel_z = 0.0
                self.no_chao = True

    def atirar(self):
        if self.municao > 0 and self.arma_anim == 0:
            self.municao -= 1
            self.arma_anim = 12
            return True
        return False

 class Inimigo:
    def __init__(self, x, y, chefe=False):
        self.x, self.y = x * TAM_BLOCO + 32, y * TAM_BLOCO + 32
        self.chefe = chefe
        self.vida = self.vida_max = 300 if chefe else 60
        self.vivo = True
        self.raiva = False
        self.ultimo_ataque = 0
        self.piscar = 0

    def atualizar(self, jog):
        if not self.vivo: return
        if self.piscar > 0: self.piscar -= 1
        
        dx, dy = jog.x - self.x, jog.y - self.y
        dist = math.hypot(dx, dy)
        
        alcance_visao = 500 if self.chefe else 350
        vel = 3.0 if (self.chefe and self.raiva) else (1.8 if not self.chefe else 1.4)

        if dist < alcance_visao and dist > (100 if self.chefe else 50):
            mov_x, mov_y = (dx/dist) * vel, (dy/dist) * vel
            nx = int((self.x + mov_x + (20 if mov_x > 0 else -20)) / TAM_BLOCO)
            ny = int((self.y + mov_y + (20 if mov_y > 0 else -20)) / TAM_BLOCO)
            
            if MAPA[int(self.y / TAM_BLOCO)][nx] == 0: self.x += mov_x
            if MAPA[ny][int(self.x / TAM_BLOCO)] == 0: self.y += mov_y

        if self.chefe and self.vida < 150: self.raiva = True
            
        alcance_ataque = 150 if self.chefe else 80
        dano = random.randint(15, 25) if self.chefe else random.randint(5, 12)

        if dist < alcance_ataque and pygame.time.get_ticks() - self.ultimo_ataque > 1000:
            jog.vida -= dano
            jog.dano_tela = 15
            self.ultimo_ataque = pygame.time.get_ticks()

# ==========================================
# 5. RENDERIZAÇÃO 3D AVANÇADA (PC)
# ==========================================
 def desenhar_cena(jog, inimigos, tela):
    bobbing = math.sin(pygame.time.get_ticks() * 0.015) * 10 if jog.andando else 0
    horizonte = (ALT // 2) + int(jog.pitch) + int(bobbing)

    deslocamento_ceu = int(jog.angulo * 250) % LARG
    tela.fill((10, 5, 20))
    for i in range(LARG):
        cor_ceu = max(5, 40 - abs((i + deslocamento_ceu) % LARG - LARG//2) // 12)
        pygame.draw.line(tela, (cor_ceu, cor_ceu//2, 35), (i, 0), (i, max(0, horizonte)))
    
    for y in range(max(0, horizonte), ALT, 4):
        dist_chao = y - horizonte
        brilho = min(60, max(10, dist_chao))
        pygame.draw.rect(tela, (brilho - 10, brilho - 5, brilho), (0, y, LARG, 4))

    lista_render = []
    passo = 3  

    for i in range(0, LARG, passo):
        ang = jog.angulo - 0.5 + (i / LARG)
        dist, batida = 0.1, False
        rx, ry, mx, my = jog.x, jog.y, 0, 0
        
        while not batida and dist < 1500:
            dist += 4
            rx = jog.x + math.cos(ang) * dist
            ry = jog.y + math.sin(ang) * dist
            mx, my = int(rx/TAM_BLOCO), int(ry/TAM_BLOCO)
            if mx<0 or mx>=20 or my<0 or my>=9 or MAPA[my][mx]>0: batida=True
        
        d_corr = dist * math.cos(ang - jog.angulo)
        alt_parede = min(ALT*2, TAM_BLOCO * (ALT//2) / (d_corr + 0.0001))
        
        tipo_parede = MAPA[my][mx] if (0 <= mx < 20 and 0 <= my < 9) else 1
        if tipo_parede == 0: tipo_parede = 1
        
        hit_x, hit_y = rx % TAM_BLOCO, ry % TAM_BLOCO
        horizontal = abs(hit_x - TAM_BLOCO/2) > abs(hit_y - TAM_BLOCO/2)
        tex_x = int(hit_y if horizontal else hit_x)
        tex_x = int((tex_x / TAM_BLOCO) * TAM_TEX)
        tex_x = max(0, min(TAM_TEX-1, tex_x))
        
        coluna_tex = TEXTURAS[tipo_parede].subsurface((tex_x, 0, 1, TAM_TEX))
        strip = pygame.transform.scale(coluna_tex, (passo, int(alt_parede)))
        
        escurecer = max(20, min(255, 255 - int((d_corr / 1000) * 255)))
        if horizontal: escurecer = int(escurecer * 0.6)
        strip.fill((escurecer, escurecer, escurecer), special_flags=pygame.BLEND_RGB_SUB)

        lista_render.append((d_corr, "parede", i, alt_parede, strip))

    for ini in inimigos:
        if not ini.vivo: continue
        dx, dy = ini.x - jog.x, ini.y - jog.y
        dist = math.hypot(dx, dy)
        dif_ang = math.atan2(dy, dx) - jog.angulo
        
        while dif_ang > math.pi: dif_ang -= 2*math.pi
        while dif_ang < -math.pi: dif_ang += 2*math.pi
        
        if abs(dif_ang) < 0.8:
            lista_render.append((dist, "inimigo", dif_ang, ini))

    lista_render.sort(key=lambda x: x[0], reverse=True)
    
    for item in lista_render:
        if item[1] == "parede":
            _, _, i, alt_parede, strip = item
            z_proj = (jog.z / item[0]) * 35.0 if item[0] > 0 else 0
            topo = horizonte - (alt_parede / 2) + z_proj
            tela.blit(strip, (i, int(topo)))
        else:
            dist, _, dif_ang, ini = item
            x = LARG//2 + (dif_ang / 0.5) * (LARG//2)
            
            escala = 2.0 if ini.chefe else 1.2
            alt_ini = min(ALT*1.5, 120 * escala * (ALT//2) / (dist + 0.001))
            lar_ini = alt_ini * 0.7
            
            z_proj = (jog.z / dist) * 35.0 if dist > 0 else 0
            rect_x, rect_y = int(x - lar_ini//2), int(horizonte - alt_ini//2 + alt_ini*0.2 + z_proj)
            rect_w, rect_h = max(4, int(lar_ini)), max(4, int(alt_ini*0.8))
            
            pygame.draw.ellipse(tela, (20,20,20), (rect_x, rect_y + rect_h - 15, rect_w, 30))
            
            cor_ini = BRANCO if ini.piscar > 0 else (ROXO_CHEFE if ini.chefe else VERM)
            pygame.draw.ellipse(tela, cor_ini, (rect_x, rect_y, rect_w, rect_h))
            pygame.draw.ellipse(tela, PRETO, (rect_x, rect_y, rect_w, rect_h), 4) 
            
            cor_olho = VERM if ini.chefe and ini.raiva else AMARELO
            pygame.draw.circle(tela, cor_olho, (int(x - rect_w*0.15), int(rect_y + rect_h*0.3)), max(2, int(rect_w*0.15)))
            pygame.draw.circle(tela, cor_olho, (int(x + rect_w*0.15), int(rect_y + rect_h*0.3)), max(2, int(rect_w*0.15)))
            
            pygame.draw.rect(tela, (80,0,0), (rect_x, rect_y - 20, rect_w, 10))
            pygame.draw.rect(tela, VERDE, (rect_x, rect_y - 20, int(rect_w*(ini.vida/ini.vida_max)), 10))

    return horizonte

# ==========================================
# 6. INTERFACE E HUD (PC)
# ==========================================
 def desenhar_ui(jog, tela, fps, horizonte):
    bob_arma = math.sin(pygame.time.get_ticks() * 0.015) * 15 if jog.andando else 0
    desl = jog.arma_anim * 10
    cx, cy = LARG//2 + 40 + int(bob_arma), ALT - 150 + desl + int(jog.pitch * 0.4) + int(jog.z * 1.5)
    
    pygame.draw.polygon(tela, (20,20,20), [(cx-30, cy), (cx+30, cy), (cx+60, ALT), (cx-60, ALT)])
    pygame.draw.polygon(tela, (70,75,80), [(cx-15, cy), (cx+15, cy), (cx+25, ALT), (cx-25, ALT)])
    
    if jog.arma_anim > 8:
        pygame.draw.circle(tela, (255, 100, 0), (cx, cy - 30), 50)
        pygame.draw.circle(tela, AMARELO, (cx, cy - 30), 30)
        pygame.draw.circle(tela, BRANCO, (cx, cy - 30), 15)

    if jog.arma_anim > 0: jog.arma_anim -= 1

    if jog.dano_tela > 0:
        s = pygame.Surface((LARG, ALT), pygame.SRCALPHA)
        s.fill((255, 0, 0, min(150, jog.dano_tela * 10)))
        tela.blit(s, (0,0))
        jog.dano_tela -= 1

    pygame.draw.circle(tela, (0,255,0), (LARG//2, horizonte), 4, 1)
    pygame.draw.line(tela, (0,255,0), (LARG//2 - 12, horizonte), (LARG//2 + 12, horizonte), 2)
    pygame.draw.line(tela, (0,255,0), (LARG//2, horizonte - 12), (LARG//2, horizonte + 12), 2)

    f_hud = pygame.font.Font(None, 36)
    pygame.draw.rect(tela, (0,0,0), (20, 20, 220, 35), border_radius=5)
    pygame.draw.rect(tela, VERM, (20, 20, int(220*(max(0, jog.vida)/100)), 35), border_radius=5)
    tela.blit(f_hud.render(f"HP: {max(0,jog.vida)}", True, BRANCO), (30, 25))
    
    pygame.draw.rect(tela, (0,0,0), (LARG - 180, 20, 160, 35), border_radius=5)
    tela.blit(f_hud.render(f"BALAS: {jog.municao}", True, AMARELO), (LARG - 170, 25))

    f_fps = pygame.font.Font(None, 28)
    tela.blit(f_fps.render(f"FPS: {fps}", True, VERDE), (LARG - 180, 65))
    
    txt_controles = f_fps.render("W,A,S,D: Andar | SETAS: Girar/Olhar | ESPAÇO: Pular | CLIQUE: Atirar", True, (200, 200, 200))
    tela.blit(txt_controles, (20, ALT - 30))

# ==========================================
# 7. LOOP PRINCIPAL (PC)
# ==========================================
 def main():
    jog = Jogador()
    inimigos = [Inimigo(4,1), Inimigo(9,3), Inimigo(13,5), Inimigo(3,7), Inimigo(17,7, chefe=True)]

    while True:
        mov_frente = mov_lado = girar = 0
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    jog.pular()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:  
                    if jog.atirar():
                        for ini in inimigos:
                            if not ini.vivo: continue
                            dx, dy = ini.x - jog.x, ini.y - jog.y
                            dist = math.hypot(dx, dy)
                            dif = math.atan2(dy, dx) - jog.angulo
                            while dif > math.pi: dif -= 2*math.pi
                            while dif < -math.pi: dif += 2*math.pi
                            if dist < 600.0 and abs(dif) < 0.35:
                                ini.vida -= 30
                                ini.piscar = 6
                                if ini.vida <= 0: ini.vivo = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] or teclas[pygame.K_UP]: mov_frente = jog.vel_andar
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]: mov_frente = -jog.vel_andar
        if teclas[pygame.K_a]: mov_lado = -jog.vel_andar
        if teclas[pygame.K_d]: mov_lado = jog.vel_andar
        if teclas[pygame.K_LEFT]: jog.girar(-jog.vel_girar)
        if teclas[pygame.K_RIGHT]: jog.girar(jog.vel_girar)
        
        if teclas[pygame.K_r]: jog.pitch = min(200.0, jog.pitch + 6.0)
        if teclas[pygame.K_f]: jog.pitch = max(-200.0, jog.pitch - 6.0)

        if jog.vida > 0:
            jog.mover(mov_frente, mov_lado)
            jog.atualizar_fisica()
            for ini in inimigos: ini.atualizar(jog)

        fps_atual = int(relogio.get_fps())
        horizonte = desenhar_cena(jog, inimigos, tela)
        desenhar_ui(jog, tela, fps_atual, horizonte)
        
        if jog.vida <= 0:
            sombra = pygame.Surface((LARG, ALT))
            sombra.fill((0,0,0))
            sombra.set_alpha(150)
            tela.blit(sombra, (0,0))
            txt_morte = pygame.font.Font(None, 80).render("VOCÊ MORREU", True, VERM)
            tela.blit(txt_morte, txt_morte.get_rect(center=(LARG//2, ALT//2)))
           
        pygame.display.flip()
        relogio.tick(30)

 if __name__ == "__main__":
    main()
         
 time.time_ns(100)
 if input("Deseja jogar novamente? (s/n): ").lower() != 's':
        break