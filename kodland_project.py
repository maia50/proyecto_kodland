import math
import pygame
import random
import sys


screen = pygame.display.set_mode((1200, 650))
color_fondo = (27, 30, 36)
celeste = (169, 201, 252)
vidas = 3
teclas_aceptadas = [
    "K_SPACE",
    "K_0", "K_1", "K_2", "K_3", "K_4", "K_5", "K_6", "K_7", "K_8", "K_9",
    "K_a", "K_b", "K_c", "K_d", "K_e", "K_f", "K_g", "K_h", "K_i", "K_j",
    "K_k", "K_l", "K_m", "K_n", "K_o", "K_p", "K_q", "K_r", "K_s", "K_t",
    "K_u", "K_v", "K_w", "K_x", "K_y", "K_z",
]
delay_texto = 7000


def main():
    # abre la ventana con pygame y muestra la introducción
    comenzar_juego()

    # muestra el menú de inicio
    display_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == pygame.MOUSEBUTTONDOWN and 375 <= event.pos[0] <= 825:
                if 250 <= event.pos[1] <= 325:
                    enemigo_terremoto()
                    enemigo_lava()
                    enemigo_nube()
                    ganar()
                    return
                elif 350 <= event.pos[1] <= 425:
                    # muestra la información sobre los controles
                    mostrar_controles()
                elif 450 <= event.pos[1] <= 525:
                    # pide confirmación para cerrar el juego
                    confirmar_salida()


def comenzar_juego():
    global screen, celeste, delay_texto, vidas

    vidas = 3

    # abre la ventana
    pygame.init()
    pygame.display.set_icon(pygame.image.load("logo32x32.png"))
    pygame.display.set_caption("Los espíritus del pueblo")
    screen.fill(celeste)

    # muestra la introducción
    imagenes = [
        pygame.image.load("intro1.png"),
        pygame.image.load("intro2.png"),
        pygame.image.load("intro3.png")
    ]
    for i in range(3):
        screen.blit(imagenes[i], (0, 0))
        pygame.display.update()
        pygame.time.delay(delay_texto)
        screen.fill(celeste)


def cerrar_juego():
    pygame.quit()
    sys.exit()


def display_menu():
    global screen, color_fondo

    screen.fill(color_fondo)

    screen.blit(pygame.image.load("nombre.png"), (258, 80))
    screen.blit(pygame.image.load("menu1.png"), (375, 250))
    screen.blit(pygame.image.load("menu2.png"), (375, 350))
    screen.blit(pygame.image.load("menu3.png"), (375, 450))

    pygame.display.update()


def mostrar_controles():
    global screen, color_fondo

    screen.fill(color_fondo)
    screen.blit(pygame.image.load("controles.png"), (0, 0))
    screen.blit(pygame.image.load("flecha.png"), (0, 0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == pygame.MOUSEBUTTONDOWN and 0 <= event.pos[0] <= 125 and 0 <= event.pos[1] <= 125:
                display_menu()
                return


def confirmar_salida():
    global screen, color_fondo

    screen.fill(color_fondo)
    screen.blit(pygame.image.load("confirmarSalir.png"), (300, 150))
    screen.blit(pygame.image.load("volver.png"), (410, 370))
    screen.blit(pygame.image.load("salir.png"), (610, 370))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == pygame.MOUSEBUTTONDOWN and 370 <= event.pos[1] <= 424:
                if 610 <= event.pos[0] <= 790:
                    cerrar_juego()
                elif 410 <= event.pos[0] <= 590:
                    display_menu()
                    return


def jugador_listo():
    global screen, celeste

    screen.blit(pygame.image.load("entendido.png"), (400, 450))
    pygame.display.update()

    # espera que el jugador esté listo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == pygame.MOUSEBUTTONDOWN and 400 <= event.pos[0] <= 800 and 450 <= event.pos[1] <= 525:
                screen.fill(celeste)
                pygame.display.update()
                return


def display_vidas():
    global screen, vidas

    vida = pygame.image.load("vida.png")
    vida_perdida = pygame.image.load("vidaPerdida.png")
    for i in range(3):
        if i < vidas:
            screen.blit(vida, (100 * i, 0))
        else:
            screen.blit(vida_perdida, (100 * i, 0))
    pygame.display.update()


def enemigo_terremoto():
    global screen, color_fondo, celeste, vidas, delay_texto

    if vidas == 0:
        perder()

    intro = [
        pygame.image.load("terremoto1.png"),
        pygame.image.load("terremoto2.png"),
        pygame.image.load("terremoto3.png")
    ]
    for i in range(3):
        screen.fill(celeste)
        screen.blit(intro[i], (0, 0))
        pygame.display.update()
        pygame.time.delay(delay_texto)

    # espera la confirmación del jugador para empezar
    jugador_listo()

    while True:
        if batalla1():
            batalla1_ganada()
            return
        else:
            vidas -= 1
            if vidas != 0:
                if not batalla_perdida():
                    break
            else:
                perder()


def batalla1():
    global screen, color_fondo, celeste, teclas_aceptadas

    # prepara los elementos de la batalla
    check = False
    frame1 = pygame.image.load("terremoto4.png")
    frame2 = pygame.image.load("terremoto5.png")
    cambiar_frame = pygame.USEREVENT + 1
    velocidad = 100
    pygame.time.set_timer(cambiar_frame, velocidad)

    # genera la lista de teclas
    teclas = random.sample(teclas_aceptadas, k=6)
    constantes_teclas = []
    for tecla in teclas:
        constantes_teclas.append(getattr(pygame, tecla))

    perder_por_tiempo = pygame.USEREVENT + 2
    pygame.time.set_timer(perder_por_tiempo, 1500)
    siguiente_tecla = pygame.USEREVENT + 3

    font = pygame.font.Font(None, 150)
    i = 0

    # loop de juego
    while i < 6:
        superficie_texto = font.render(teclas[i].lstrip("K_").upper(), True, color_fondo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == cambiar_frame:

                # actualización del fondo
                screen.fill(celeste)
                if check:
                    screen.blit(frame1, (0, 0))
                    display_vidas()
                    screen.blit(superficie_texto, (565, 150))
                    check = False
                    pygame.display.update()
                else:
                    screen.blit(frame2, (0, 0))
                    display_vidas()
                    screen.blit(superficie_texto, (565, 150))
                    check = True
                    pygame.display.update()
            # procesamiento de las acciones del jugador con las teclas
            elif event.type == pygame.KEYDOWN and event.key == constantes_teclas[i]:
                pygame.time.set_timer(siguiente_tecla, 2500)
                pygame.time.set_timer(perder_por_tiempo, 0)
            elif event.type == pygame.KEYUP and event.key == constantes_teclas[i]:
                pygame.time.set_timer(siguiente_tecla, 0)
                pygame.time.set_timer(perder_por_tiempo, 1500)
            elif event.type == perder_por_tiempo:
                # pierde la batalla
                return False
            elif event.type == siguiente_tecla:
                # cambio de la tecla a mantener
                pygame.time.set_timer(perder_por_tiempo, 1500)
                i += 1
                velocidad += 50 * i
                pygame.time.set_timer(cambiar_frame, velocidad)

        if i == 6:
            pygame.time.set_timer(perder_por_tiempo, 0)

    # gana la batalla
    pygame.time.set_timer(cambiar_frame, 0)
    pygame.time.set_timer(siguiente_tecla, 0)
    return True


def enemigo_lava():
    global screen, celeste, vidas, delay_texto

    if vidas == 0:
        perder()

    intro = [
        pygame.image.load("lava1.png"),
        pygame.image.load("lava2.png"),
        pygame.image.load("lava3.png")
    ]
    for i in range(3):
        screen.fill(celeste)
        screen.blit(intro[i], (0, 0))
        pygame.display.update()
        pygame.time.delay(delay_texto)

    # espera la confirmación del jugador para empezar
    jugador_listo()

    while True:
        if batalla2():
            batalla2_ganada()
            return
        else:
            vidas -= 1
            if vidas != 0:
                if not batalla_perdida():
                    break
            else:
                perder()


def batalla2():
    global screen

    # prepara los elementos de la batalla
    check = False
    frame1 = pygame.image.load("lava4.png")
    frame2 = pygame.image.load("lava5.png")
    cambiar_frame = pygame.USEREVENT + 1
    pygame.time.set_timer(cambiar_frame, 500)

    generar_solido = pygame.USEREVENT + 4
    pygame.time.set_timer(generar_solido, 250)
    posicion_previa = pygame.mouse.get_pos()
    posicion_previa = (posicion_previa[0] - 25, posicion_previa[1] - 25)
    posiciones = [posicion_previa, posicion_previa, posicion_previa, posicion_previa, posicion_previa]

    i = 0
    solidos = [
        pygame.image.load("solido1.png"),
        pygame.image.load("solido2.png"),
        pygame.image.load("solido3.png"),
        pygame.image.load("solido4.png")
    ]

    chequear_mouse = pygame.USEREVENT + 5
    pygame.time.set_timer(chequear_mouse, 500)

    # loop de juego
    while i < 20:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == cambiar_frame:

                # actualización del fondo
                screen.fill((4, 0, 14))
                if check:
                    screen.blit(frame1, (0, 0))
                    display_vidas()
                    posiciones = generar(solidos, posiciones)
                    check = False
                    pygame.display.update()
                else:
                    screen.blit(frame2, (0, 0))
                    display_vidas()
                    posiciones = generar(solidos, posiciones)
                    check = True
                    pygame.display.update()

            elif event.type == generar_solido:
                posiciones = generar(solidos, posiciones)
                i += 1
            elif event.type == chequear_mouse:
                if screen.get_at(pygame.mouse.get_pos()) != (4, 0, 14):
                    # pierde la batalla
                    pygame.time.set_timer(chequear_mouse, 0)
                    return False
        if i == 20:
            pygame.time.set_timer(chequear_mouse, 0)

    # gana la batalla
    pygame.time.set_timer(cambiar_frame, 0)
    pygame.time.set_timer(generar_solido, 0)
    return True


def generar(solidos, posiciones):

    # toma una lista de las coordenadas en las que hay piso sólido,
    # crea una más, se olvida la más antigua y las muestra en la pantalla
    # Las coordenadas nuevas son en una dirección aleatoria, a distancia radio de las coordenadas más recientes

    radio = 35

    grados = random.randint(0, 360)
    cambio_x = round(math.cos(math.radians(grados)) * radio)
    cambio_y = round(-math.sin(math.radians(grados)) * radio)

    # actualiza la lista de coordenadas
    posicion_nueva = (posiciones[0][0] + cambio_x, posiciones[0][1] + cambio_y)
    posiciones[4] = posiciones[3]
    posiciones[3] = posiciones[2]
    posiciones[2] = posiciones[1]
    posiciones[1] = posiciones[0]
    posiciones[0] = posicion_nueva

    for posicion in posiciones:
        screen.blit(random.choice(solidos), posicion)
    pygame.display.update()
    return posiciones


def enemigo_nube():
    global screen, celeste, vidas, delay_texto

    if vidas == 0:
        perder()

    intro = [
        pygame.image.load("nube1.png"),
        pygame.image.load("nube2.png"),
        pygame.image.load("nube3.png")
    ]
    for i in range(3):
        screen.fill(celeste)
        screen.blit(intro[i], (0, 0))
        pygame.display.update()
        pygame.time.delay(delay_texto)

    # espera la confirmación del jugador para empezar
    jugador_listo()

    while True:
        if batalla3():
            batalla3_ganada()
            return
        else:
            vidas -= 1
            if vidas != 0:
                if not batalla_perdida():
                    break
            else:
                perder()


def batalla3():
    global screen, celeste

    nubes = [
        pygame.image.load("nubes1.png"),
        pygame.image.load("nubes2.png"),
        pygame.image.load("nubes3.png"),
        pygame.image.load("nubes4.png"),
        pygame.image.load("nubes5.png")
    ]
    movimientos = 150
    while True:
        if movimientos == 0:
            # gana la batalla
            return True
        elif movimientos > 300:
            # pierde la batalla
            return False
        screen.fill(celeste)

        # actualiza el fondo dependiendo de las acciones del jugador
        if movimientos <= 60:
            screen.blit(nubes[0], (0, 0))
            display_vidas()
            pygame.display.update()
        elif movimientos <= 120:
            screen.blit(nubes[1], (0, 0))
            display_vidas()
            pygame.display.update()
        elif movimientos <= 180:
            screen.blit(nubes[2], (0, 0))
            display_vidas()
            pygame.display.update()
        elif movimientos <= 240:
            screen.blit(nubes[3], (0, 0))
            display_vidas()
            pygame.display.update()
        elif movimientos <= 300:
            screen.blit(nubes[4], (0, 0))
            display_vidas()
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == pygame.MOUSEMOTION:
                # procesa las acciones del jugador
                if variacion(event.rel) > 30:
                    movimientos -= 1
                else:
                    movimientos += 1


def variacion(pos):
    x = pos[0]
    y = pos[1]
    return math.sqrt(x * x + y * y)


def batalla1_ganada():
    global screen, celeste, delay_texto

    screen.fill(celeste)
    batalla_ganada = pygame.image.load("terremoto6.png")
    screen.blit(batalla_ganada, (0, 0))
    pygame.display.update()
    pygame.time.delay(delay_texto)


def batalla2_ganada():
    global screen, celeste, delay_texto

    screen.fill(celeste)
    batalla_ganada = pygame.image.load("lava6.png")
    screen.blit(batalla_ganada, (0, 0))
    pygame.display.update()
    pygame.time.delay(delay_texto)


def batalla3_ganada():
    global screen, celeste, delay_texto

    screen.fill(celeste)
    batalla_ganada = pygame.image.load("nube4.png")
    screen.blit(batalla_ganada, (0, 0))
    pygame.display.update()
    pygame.time.delay(delay_texto)


def batalla_perdida():
    global screen, color_fondo

    # menu de batalla perdida
    screen.fill(color_fondo)
    screen.blit(pygame.image.load("nuevoIntento.png"), (300, 150))
    screen.blit(pygame.image.load("reintentar.png"), (410, 370))
    screen.blit(pygame.image.load("rendirme.png"), (610, 370))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == pygame.MOUSEBUTTONDOWN and 370 <= event.pos[1] <= 424:
                if 610 <= event.pos[0] <= 790:
                    # rendirse y pasar al siguiente enemigo
                    return False
                elif 410 <= event.pos[0] <= 590:
                    # reintentar
                    return True


def ganar():
    global screen, color_fondo, celeste, vidas, delay_texto

    if vidas == 0:
        perder()

    final = [
        pygame.image.load("outro1.png"),
        pygame.image.load("outro2.png"),
        pygame.image.load("outro3.png")
    ]
    for i in range(3):
        screen.fill(celeste)
        screen.blit(final[i], (0, 0))
        pygame.display.update()
        pygame.time.delay(delay_texto)

    # menu final
    screen.blit(pygame.image.load("deNuevo.png"), (150, 200))
    screen.blit(pygame.image.load("final.png"), (650, 200))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == pygame.MOUSEBUTTONDOWN and 200 <= event.pos[1] <= 275:
                if 150 <= event.pos[0] <= 550:
                    # jugar de nuevo
                    main()
                    return
                elif 650 <= event.pos[0] <= 1050:
                    # salir del juego
                    cerrar_juego()
                    return


def perder():
    global screen, celeste, delay_texto

    screen.fill(celeste)
    screen.blit(pygame.image.load("perder.png"), (0, 0))
    pygame.display.update()
    pygame.time.delay(delay_texto)

    # menu final
    screen.blit(pygame.image.load("deNuevo.png"), (150, 250))
    screen.blit(pygame.image.load("final.png"), (650, 250))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
            elif event.type == pygame.MOUSEBUTTONDOWN and 250 <= event.pos[1] <= 325:
                if 150 <= event.pos[0] <= 550:
                    # jugar de nuevo
                    main()
                    return
                elif 650 <= event.pos[0] <= 1050:
                    # salir del juego
                    cerrar_juego()
                    return


if __name__ == "__main__":
    main()
