# My 2D RPG – Python + Pygame

Pequeno protótipo de **RPG 2D top-down** feito em Python usando Pygame.

---

## 🎮 Features atuais

- Player se movendo no mapa
- Colisão com paredes
- Mapa baseado em tiles (carregado de arquivo .txt)
- Câmera que segue o jogador
- HUD simples exibindo HP
- Estrutura modular do projeto (entities, world, ui)

## 🎮 Roadmap (próximas features)

 - NPC parado no mapa
 - Sistema de interação (tecla E)
 - Sistema de diálogos simples
 - NPCs com patrol/IA básica
 - Inventário e itens
 - Facções e reputação
 - Sistemas de atributos e skills
 - Vários mapas com transição entre áreas
 - Menu inicial (Start/Exit)

---

## 🗺 Estrutura do projeto

```text
my-2d-rpg/
├── src/
│   ├── main.py         # Loop principal do jogo
│   ├── settings.py     # Configurações gerais
│   ├── entities/
│   │   └── player.py   # Lógica do jogador
│   ├── world/
│   │   └── tiles.py    # Tiles + carregamento de mapa
│   └── ui/
│       └── hud.py      # HUD simples
│
├── data/
│   └── maps/
│       └── map1.txt    # Mapa em formato texto
│
├── requirements.txt
└── .gitignore


## 🗺 Estrutura do projeto

- Python 3.10+ (recomendado)
- Pygame

## Instalação das dependências:

pip install -r requirements.txt

## Como rodar o jogo:

python src/main.py


