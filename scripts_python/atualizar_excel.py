import pandas as pd

def atualizar_planilha_excel():
    nome_arquivo = 'projeto1.jogos.xlsx'
    
    try:
        # 1. Abre o Excel mantendo a formatação original das colunas
        df = pd.read_excel(nome_arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    # Mapeamento exato dos seus jogos
    atualizacoes = {
        'Battlefield 6': {'plataforma': 'Multiplataforma'},
        'Counter-Strike 2': {'plataforma': 'PC'},
        'ARC Raiders': {'plataforma': 'Multiplataforma'},
        'Fortnite': {'plataforma': 'Multiplataforma'},
        'Minecraft': {'plataforma': 'Multiplataforma'},
        'Roblox': {'plataforma': 'Multiplataforma'},
        'Marvel Rivals': {'plataforma': 'Multiplataforma'},
        'GTA Online (Expansao)': {'plataforma': 'Multiplataforma'},
        'Elden Ring: Nightreign': {'plataforma': 'Multiplataforma'},
        'EA FC 26': {'plataforma': 'Multiplataforma'},
        'Baldur\'s Gate 3': {'plataforma': 'Multiplataforma'},
        'Clair Obscur: Expedition 33': {'plataforma': 'Multiplataforma'},
        'Where Winds Meet': {'plataforma': 'Multiplataforma'},
        'Wuthering Waves': {'plataforma': 'Multiplataforma'},
        'Apex Legends': {'plataforma': 'Multiplataforma'},
        'Honkai: Star Rail': {'plataforma': 'Multiplataforma'},
        'Valorant': {'plataforma': 'Multiplataforma'},
        'Call of Duty: Black Ops 7': {'plataforma': 'Multiplataforma'},
        'Metroid Prime 4: Beyond': {'plataforma': 'Console'},
        'Path of Exile 2': {'plataforma': 'Multiplataforma'},
        'Dota 2': {'plataforma': 'PC'},
        'Zzz (Zenless Zone Zero)': {'plataforma': 'Multiplataforma'},
        'Stardew Valley': {'plataforma': 'Multiplataforma'},
        'Deadlock': {'plataforma': 'PC'},
        'Warframe': {'plataforma': 'Multiplataforma'},
        'Cyberpunk 2077': {'plataforma': 'Multiplataforma'},
        'Hades II': {'plataforma': 'Multiplataforma'},
        'Hollow Knight: Silksong': {'plataforma': 'Multiplataforma'},
        'Helldivers 2': {'plataforma': 'Multiplataforma'},
        'Sea of Thieves': {'plataforma': 'Multiplataforma'},
        'Destiny 2': {'plataforma': 'Multiplataforma'},
        'World of Warcraft': {'plataforma': 'PC'},
        'Final Fantasy XIV': {'plataforma': 'Multiplataforma'},
        'The Sims 4': {'plataforma': 'Multiplataforma'},
        'Garry\'s Mod': {'plataforma': 'PC'},
        'Assetto Corsa EVO': {'plataforma': 'Multiplataforma'},
        'Forza Horizon 5': {'plataforma': 'Multiplataforma'},
        'Monster Hunter Wilds': {'plataforma': 'Multiplataforma'},
        'Dragon Ball: Sparking! Zero': {'plataforma': 'Multiplataforma'},
        'Street Fighter 6': {'plataforma': 'Multiplataforma'},
        'Tekken 8': {'plataforma': 'Multiplataforma'},
        'Mortal Kombat 1': {'plataforma': 'Multiplataforma'},
        'Rust': {'plataforma': 'Multiplataforma'},
        'Ark: Survival Ascended': {'plataforma': 'Multiplataforma'},
        'DayZ': {'plataforma': 'Multiplataforma'},
        'Escape from Tarkov': {'plataforma': 'PC'},
        'Rainbow Six Siege': {'plataforma': 'Multiplataforma'},
        'Overwatch': {'plataforma': 'Multiplataforma'},
        'Team Fortress 2': {'plataforma': 'PC'},
        'The Finals': {'plataforma': 'Multiplataforma'},
        'Phasmophobia': {'plataforma': 'Multiplataforma'},
        'Dead by Daylight': {'plataforma': 'Multiplataforma'},
        'Lethal Company': {'plataforma': 'PC'},
        'Silent Hill 2 (Remake)': {'plataforma': 'Multiplataforma'},
        'Project Zomboid': {'plataforma': 'PC'},
        'Factorio: Space Age': {'plataforma': 'PC'},
        'Satisfactory': {'plataforma': 'Multiplataforma'},
        'Cities: Skylines II': {'plataforma': 'Multiplataforma'},
        'RimWorld': {'plataforma': 'Multiplataforma'},
        'Civilization VII': {'plataforma': 'Multiplataforma'},
        'Hearts of Iron IV': {'plataforma': 'PC'},
        'Manor Lords': {'plataforma': 'Multiplataforma'},
        'Age of Empires IV': {'plataforma': 'Multiplataforma'},
        'Football Manager 2026': {'plataforma': 'Multiplataforma'},
        'Rocket League': {'plataforma': 'Multiplataforma'},
        'Clash Royale': {'plataforma': 'Mobile'},
        'Brawl Stars': {'plataforma': 'Mobile'},
        'Pokemon GO': {'plataforma': 'Mobile'},
        'Monopoly Go!': {'plataforma': 'Mobile'},
        'TFT': {'plataforma': 'Mobile'},
        'Slay the Spire 2': {'plataforma': 'PC'},
        'Balatro': {'plataforma': 'Multiplataforma'},
        'Marvel Snap': {'plataforma': 'Multiplataforma'},
        'Black Myth: Wukong': {'plataforma': 'Multiplataforma'},
        'Star Wars Outlaws': {'plataforma': 'Multiplataforma'},
        'Assassin\'s Creed Shadows': {'plataforma': 'Multiplataforma'},
        'Dragon Age: The Veilguard': {'plataforma': 'Multiplataforma'},
        'Ghost of Yotei': {'plataforma': 'Console'},
        'Terraria': {'plataforma': 'Multiplataforma'},
        'Subnautica 2': {'plataforma': 'Multiplataforma'},
        'Deep Rock Galactic': {'plataforma': 'Multiplataforma'},
        'Left 4 Dead 2': {'plataforma': 'Multiplataforma'},
        'Euro Truck Simulator 2': {'plataforma': 'Multiplataforma'},
        'Inzoi': {'plataforma': 'Multiplataforma'},
        'The First Descendant': {'plataforma': 'Multiplataforma'},
        'War Thunder': {'plataforma': 'Multiplataforma'},
        'Kingdom Come: Del. II': {'plataforma': 'Multiplataforma'},
        'Portal 2': {'plataforma': 'PC'},
        'Half-Life: Alyx': {'plataforma': 'VR'},
        'Vampire Survivors': {'plataforma': 'Multiplataforma'},
        'Dave the Diver': {'plataforma': 'Multiplataforma'},
        'Palworld': {'plataforma': 'Multiplataforma'},
        'Enshrouded': {'plataforma': 'Multiplataforma'},
        'Abyss World': {'plataforma': 'Multiplataforma'},
        'No Man\'s Sky (Update)': {'plataforma': 'Multiplataforma'},
        'The Witcher 3 (Update)': {'plataforma': 'Multiplataforma'},
        'GTA Online (Update)': {'plataforma': 'Multiplataforma'},
    }

    # Identifica dinamicamente os nomes REAIS das colunas no seu Excel
    coluna_jogo_real = [c for c in df.columns if c.lower().strip() == 'jogo'][0]
    coluna_plat_real = [c for c in df.columns if c.lower().strip() == 'plataforma'][0]

    print("Aplicando as atualizações nas linhas do Excel...")
    
    # Loop direto pelas chaves do dicionário
    for jogo, alteracoes in atualizacoes.items():
        # Cria o filtro comparando o texto exato da coluna real
        filtro = df[coluna_jogo_real].astype(str).str.strip() == jogo
        
        if filtro.any():
            # Atualiza o valor na coluna real de plataforma
            df.loc[filtro, coluna_plat_real] = alteracoes['plataforma']
            print(f"-> {jogo} atualizado para '{alteracoes['plataforma']}'")
        else:
            print(f"Aviso: O jogo '{jogo}' não foi encontrado na planilha.")

    # Salva o arquivo sem alterar nenhuma outra coluna ou cabeçalho
    df.to_excel(nome_arquivo, index=False)
    print(f"\n✨ Planilha '{nome_arquivo}' atualizada e salva com sucesso para o Power BI!")

if __name__ == "__main__":
    atualizar_planilha_excel()