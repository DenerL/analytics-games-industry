import sqlite3

def exibir_top_10():
    conn = sqlite3.connect('portfolio_games.db')
    cursor = conn.cursor()
    
    # Consulta SQL para buscar os 10 primeiros do ranking
    cursor.execute('''
        SELECT posicao_ranking, jogo, genero, horas_semana, taxa_conclusao
        FROM jogos
        ORDER BY posicao_ranking ASC
        LIMIT 10
    ''')
    
    resultados = cursor.fetchall()
    
    print("\n" + "="*60)
    print("🏆 TOP 10 JOGOS MAIS RELEVANTES DE 2025 (RANKING CALCULADO) 🏆")
    print("="*60)
    print(f"{'Pos':<4} | {'Jogo':<25} | {'Gênero':<12} | {'Horas/Sem':<9} | {'Conclusão'}")
    print("-"*60)
    
    for r in resultados:
        # Formata a exibição das linhas em colunas alinhadas
        print(f"{r[0]:<4} | {r[1]:<25} | {r[2]:<12} | {r[3]:<9.1f} | {r[4]:.1f}%")
        
    print("="*60 + "\n")
    conn.close()

if __name__ == "__main__":
    exibir_top_10()