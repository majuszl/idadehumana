from flask import Flask, render_template, request
app = Flask(__name__) #instancia o flask no aplicativo

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/resultado/', methods=['POST'])
def resultado():


  idadeanimal = int(request.form['idade'])
  esp = request.form['especie']

  if esp == "Cachorro":

    if idadeanimal == 1:
      mensagem = f"Seu cachorro tem 15 anos humanos."
    if idadeanimal == 2:
      mensagem = ("Seu cachorro tem 24 anos humanos.")
    if idadeanimal == 3:
      mensagem = ("Seu cachorro tem 28 anos humanos.")
    if idadeanimal == 4:
      mensagem = ("Seu cachorro tem 32 anos humanos.")
    if idadeanimal == 5:
      mensagem = ("Seu cachorro tem 36 anos humanos.")
    if idadeanimal == 6:
      mensagem = ("Seu cachorro tem 40 anos humanos.")
    if idadeanimal == 7:
      mensagem = ("Seu cachorro tem 44 anos humanos.")
    if idadeanimal > 7:
      count = 44 + ((idadeanimal - 7)*5)
      mensagem = (f'Seu gato tem {count} anos humanos.')
    else:
      quantidade = f'Valor inválido'

  elif esp == "Gato":

    if idadeanimal == 1:
      idade = 15
      mensagem = (f"Seu gato tem {idadeanimal} anos humanos.")
    elif idadeanimal > 1:
      idade = 4*idadeanimal + 16
      mensagem = ("Seu gato tem 24 anos humanos.")
    else:
      quantidade = f'Valor inválido'


  return render_template('index.html', resultado=f'{mensagem}')

if __name__== '__main__':
    app.run(debug=True) #executando o aplicativo flask