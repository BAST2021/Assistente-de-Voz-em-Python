

import speech_recognition as sr
import os
import subprocess
import sys
import logging
from datetime import datetime
import json
import webbrowser

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('assistente_voz.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AssistenteVoz:
    """Classe principal do Assistente de Voz"""
    
    def __init__(self):
        self.reconhecedor = sr.Recognizer()
        self.executando = True
        self.comandos = self._carregar_comandos()
        self.historico = []
        
    def _carregar_comandos(self):
        """Carrega os comandos disponíveis"""
        return {
            'navegador': {
                'nomes': ['chrome', 'navegador', 'google chrome', 'abrir navegador', 'abra o navegador'],
                'acao': self._abrir_navegador
            },
            'excel': {
                'nomes': ['excel', 'planilha', 'abrir excel', 'abra o excel', 'microsoft excel'],
                'acao': self._abrir_excel
            },
            'powerpoint': {
                'nomes': ['powerpoint', 'apresentação', 'ppt', 'power point', 'abrir powerpoint'],
                'acao': self._abrir_powerpoint
            },
            'edge': {
                'nomes': ['edge', 'microsoft edge', 'abrir edge', 'abra o edge'],
                'acao': self._abrir_edge
            },
            'vs_code': {
                'nomes': ['visual studio code', 'vs code', 'code', 'abrir code', 'editor de código'],
                'acao': self._abrir_vscode
            },
            'notepad': {
                'nomes': ['bloco de notas', 'notepad', 'editor de texto', 'abrir bloco de notas'],
                'acao': self._abrir_notepad
            },
            'calculadora': {
                'nomes': ['calculadora', 'abrir calculadora', 'calcular'],
                'acao': self._abrir_calculadora
            },
            'youtube': {
                'nomes': ['youtube', 'abrir youtube', 'ver vídeos'],
                'acao': self._abrir_youtube
            },
            'github': {
                'nomes': ['github', 'abrir github', 'repositório'],
                'acao': self._abrir_github
            },
            'fechar': {
                'nomes': ['fechar', 'sair', 'encerrar', 'terminar', 'parar', 'exit', 'quit'],
                'acao': self._fechar_programa
            },
            'ajuda': {
                'nomes': ['ajuda', 'comandos', 'o que você faz', 'o que pode fazer'],
                'acao': self._mostrar_ajuda
            },
            'horas': {
                'nomes': ['que horas são', 'hora atual', 'horas'],
                'acao': self._dizer_horas
            }
        }
    
    # Métodos para executar ações
    def _abrir_navegador(self):
        """Abre o navegador Chrome"""
        try:
            logger.info("Abrindo navegador Chrome...")
            # Tenta múltiplas formas de abrir o Chrome
            caminhos = [
                "start chrome.exe",
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            ]
            
            for caminho in caminhos:
                try:
                    if caminho.startswith("start"):
                        os.system(caminho)
                    else:
                        subprocess.Popen([caminho])
                    return True
                except:
                    continue
            
            # Se não encontrar, usa o webbrowser padrão
            webbrowser.open('https://www.google.com')
            return True
            
        except Exception as e:
            logger.error(f"Erro ao abrir navegador: {e}")
            return False
    
    def _abrir_excel(self):
        """Abre o Microsoft Excel"""
        try:
            logger.info("Abrindo Microsoft Excel...")
            os.system("start excel.exe")
            return True
        except Exception as e:
            logger.error(f"Erro ao abrir Excel: {e}")
            return False
    
    def _abrir_powerpoint(self):
        """Abre o Microsoft PowerPoint"""
        try:
            logger.info("Abrindo Microsoft PowerPoint...")
            os.system("start powerpnt.exe")
            return True
        except Exception as e:
            logger.error(f"Erro ao abrir PowerPoint: {e}")
            return False
    
    def _abrir_edge(self):
        """Abre o Microsoft Edge"""
        try:
            logger.info("Abrindo Microsoft Edge...")
            os.system("start msedge.exe")
            return True
        except Exception as e:
            logger.error(f"Erro ao abrir Edge: {e}")
            return False
    
    def _abrir_vscode(self):
        """Abre o Visual Studio Code"""
        try:
            logger.info("Abrindo Visual Studio Code...")
            os.system("code")
            return True
        except Exception as e:
            logger.error(f"Erro ao abrir VS Code: {e}")
            return False
    
    def _abrir_notepad(self):
        """Abre o Bloco de Notas"""
        try:
            logger.info("Abrindo Bloco de Notas...")
            os.system("start notepad.exe")
            return True
        except Exception as e:
            logger.error(f"Erro ao abrir Notepad: {e}")
            return False
    
    def _abrir_calculadora(self):
        """Abre a Calculadora"""
        try:
            logger.info("Abrindo Calculadora...")
            os.system("start calc.exe")
            return True
        except Exception as e:
            logger.error(f"Erro ao abrir calculadora: {e}")
            return False
    
    def _abrir_youtube(self):
        """Abre o YouTube no navegador"""
        try:
            logger.info("Abrindo YouTube...")
            webbrowser.open('https://www.youtube.com')
            return True
        except Exception as e:
            logger.error(f"Erro ao abrir YouTube: {e}")
            return False
    
    def _abrir_github(self):
        """Abre o GitHub no navegador"""
        try:
            logger.info("Abrindo GitHub...")
            webbrowser.open('https://www.github.com')
            return True
        except Exception as e:
            logger.error(f"Erro ao abrir GitHub: {e}")
            return False
    
    def _fechar_programa(self):
        """Fecha o programa"""
        logger.info("Encerrando programa por comando de voz...")
        self.executando = False
        return True
    
    def _mostrar_ajuda(self):
        """Mostra os comandos disponíveis"""
        ajuda_texto = """
        📋 COMANDOS DISPONÍVEIS:
        
        🚀 APLICATIVOS:
        • "Navegador" ou "Chrome" - Abre o Google Chrome
        • "Excel" - Abre o Microsoft Excel
        • "PowerPoint" - Abre o Microsoft PowerPoint
        • "Edge" - Abre o Microsoft Edge
        • "VS Code" - Abre o Visual Studio Code
        • "Bloco de Notas" - Abre o editor de texto
        • "Calculadora" - Abre a calculadora
        
        🌐 SITES:
        • "YouTube" - Abre o YouTube
        • "GitHub" - Abre o GitHub
        
        ⚙️  CONTROLE:
        • "Fechar" ou "Sair" - Encerra o programa
        • "Ajuda" - Mostra esta mensagem
        • "Que horas são?" - Mostra a hora atual
        
        🔊 Diga um comando após o sinal sonoro!
        """
        print(ajuda_texto)
        return True
    
    def _dizer_horas(self):
        """Informa a hora atual"""
        hora_atual = datetime.now().strftime("%H:%M")
        mensagem = f"🕐 São {hora_atual} horas"
        print(mensagem)
        logger.info(f"Hora informada: {hora_atual}")
        return True
    
    def _processar_comando(self, frase):
        """Processa a frase reconhecida e executa o comando correspondente"""
        frase = frase.lower().strip()
        self.historico.append(frase)
        
        logger.info(f"Frase reconhecida: {frase}")
        
        # Busca por correspondência nos comandos
        for nome_comando, dados in self.comandos.items():
            for palavra_chave in dados['nomes']:
                if palavra_chave in frase:
                    logger.info(f"Executando comando: {nome_comando}")
                    print(f"✅ Executando: {nome_comando.upper()}")
                    dados['acao']()
                    return True
        
        # Se não encontrou comando
        logger.warning(f"Comando não reconhecido: {frase}")
        print("🤔 Comando não reconhecido. Diga 'ajuda' para ver os comandos disponíveis.")
        return False
    
    def ouvir_microfone(self):
        """Ouve o microfone e reconhece a fala"""
        try:
            with sr.Microphone() as fonte:
                # Ajusta para ruído ambiente
                print("🔇 Ajustando para ruído ambiente...")
                self.reconhecedor.adjust_for_ambient_noise(fonte, duration=1)
                
                # Sinal sonoro (opcional)
                print("\n🎤 Pode falar agora!")
                print("📞 (Falando...)")
                
                # Captura áudio com timeout
                audio = self.reconhecedor.listen(
                    fonte, 
                    timeout=8, 
                    phrase_time_limit=15
                )
                
                try:
                    # Reconhece a fala
                    frase = self.reconhecedor.recognize_google(
                        audio, 
                        language='pt-BR'
                    )
                    
                    print(f"👤 Você disse: {frase}")
                    return frase
                    
                except sr.UnknownValueError:
                    print("❓ Não consegui entender. Pode repetir?")
                    logger.warning("Não foi possível entender a fala")
                    return None
                    
                except sr.RequestError as e:
                    print(f"🔌 Erro de conexão: {e}")
                    logger.error(f"Erro no serviço de reconhecimento: {e}")
                    return None
                    
        except sr.WaitTimeoutError:
            print("⏰ Tempo esgotado. Nenhuma fala detectada.")
            logger.warning("Timeout na captura de áudio")
            return None
            
        except Exception as e:
            print(f"💥 Erro inesperado: {e}")
            logger.error(f"Erro no microfone: {e}")
            return None
    
    def exibir_banner(self):
        """Exibe o banner inicial"""
        banner = """
        ╔══════════════════════════════════════════╗
        ║        🎤 ASSISTENTE DE VOZ  🎤         ║
        ║        ==========================        ║
        ║  Comandos em Português • Python Powered  ║
        ╚══════════════════════════════════════════╝
        📍 Diga 'ajuda' para ver todos os comandos
        📍 Diga 'fechar' para encerrar o programa
        📍 Logs salvos em: assistente_voz.log
        
        """
        print(banner)
    
    def salvar_historico(self):
        """Salva o histórico de comandos em um arquivo"""
        try:
            with open('historico_comandos.json', 'w', encoding='utf-8') as f:
                json.dump(self.historico, f, ensure_ascii=False, indent=2)
            logger.info("Histórico salvo com sucesso")
        except Exception as e:
            logger.error(f"Erro ao salvar histórico: {e}")
    
    def executar(self):
        """Método principal de execução"""
        self.exibir_banner()
        
        try:
            while self.executando:
                # Aguarda comando de voz
                frase = self.ouvir_microfone()
                
                if frase:
                    # Processa o comando
                    self._processar_comando(frase)
                
                # Pequena pausa entre comandos
                print("\n" + "─" * 50 + "\n")
                
        except KeyboardInterrupt:
            print("\n\n🛑 Programa interrompido pelo usuário")
            logger.info("Programa interrompido pelo usuário (Ctrl+C)")
        
        finally:
            # Salva histórico antes de sair
            if self.historico:
                self.salvar_historico()
            
            print("\n" + "=" * 50)
            print("📊 ESTATÍSTICAS DA SESSÃO:")
            print(f"   Comandos executados: {len(self.historico)}")
            print(f"   Histórico salvo em: historico_comandos.json")
            print(f"   Logs salvos em: assistente_voz.log")
            print("=" * 50)
            print("\n👋 Até logo! Obrigado por usar o Assistente de Voz!")
            logger.info("Programa encerrado normalmente")


def verificar_dependencias():
    """Verifica se todas as dependências estão instaladas"""
    dependencias = ['speech_recognition', 'pyaudio']
    
    print("🔍 Verificando dependências...")
    
    for dependencia in dependencias:
        try:
            __import__(dependencia.replace('-', '_'))
            print(f"✅ {dependencia} - OK")
        except ImportError:
            print(f"❌ {dependencia} - FALTANDO")
            print(f"   Instale com: pip install {dependencia}")
            
            if dependencia == 'pyaudio':
                print("   Ou tente: pip install pipwin && pipwin install pyaudio")
    
    print("\n" + "─" * 50)


def main():
    """Função principal do programa"""
    print("🚀 Inicializando Assistente de Voz...")
    
    # Verifica dependências
    verificar_dependencias()
    
    # Cria e executa o assistente
    assistente = AssistenteVoz()
    
    try:
        assistente.executar()
    except Exception as e:
        logger.critical(f"Erro crítico: {e}")
        print(f"💥 Erro crítico: {e}")
        print("📋 Verifique o arquivo de log para mais detalhes")


if __name__ == "__main__":
    main()