# Título: Hashzap

# importar flet
import flet as ft

# criar função principal
def main(pagina):
    # criar funcionalidades

    # criar elemento
    titulo = ft.Text("Hashzap")

    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")


    chat = ft.Column()

    # Criar função túnel de comunicação
    def enviar_mensagem_tunel(mensagem):
        texto_do_chat = ft.Text(mensagem)
        chat.controls.append(texto_do_chat)
        pagina.update()
    
    #Chamar túnel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)

        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False

        pagina.add(chat)
        pagina.add(linha_mensagem)

        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)

        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

    # colocar elemento na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# rodas aplicativo
ft.app(main, view=ft.WEB_BROWSER)