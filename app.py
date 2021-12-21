from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message


#objeto
app = Flask(__name__)


#config objeto
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']='ventas.entrehumoos@gmail.com'
app.config['MAIL_PASSWORD']='Entrehumoos23'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

#obejto mail
mail = Mail(app)





@app.route('/')

def  Index():
    
    return render_template('index.html')



@app.route('/tabacos', methods=['GET','POST'])

def Tabacos():

    if request.method == 'POST':
        producto = request.form['carrito']

       

        
        return redirect('/formulario/'+producto)

    else:
        return render_template('tabacos.html')



@app.route('/formulario/<producto>', methods=['GET','POST'])

def Formulario(producto):

    if request.method == 'POST':
        correo = request.form['correo']
        return Correo(correo, producto)

    else:
        
        return render_template('formulario.html')

def Correo(correo, producto):

    msg = Message('Solicitud de Compra', sender='tienda.entrehumoos@gmail.com', recipients = [correo, "ventas.entrehumoos@gmail.com"])
    msg.body = 'Hola, tu solicitud:" '+producto+' " ha sido enviada a Entrehumoos y está siendo procesada. Solicitante: '+correo
    mail.send(msg)


    return redirect('/')



@app.route('/papelillos', methods=['GET','POST'])


def Papelillos():

    if request.method == 'POST':
        producto = request.form['carrito']

       

        
        return redirect('/formulario/'+producto)

    else:
        return render_template('papelillos.html')



@app.route('/parafernalia', methods=['GET','POST'])


def Parafernalia():

    if request.method == 'POST':
        producto = request.form['carrito']

       

        
        return redirect('/formulario/'+producto)

    else:
        return render_template('parafernalia.html')


@app.route('/filtros', methods=['GET','POST'])


def Filtros():

    if request.method == 'POST':
        producto = request.form['carrito']

       

        
        return redirect('/formulario/'+producto)

    else:
        return render_template('filtros.html')











if __name__ == '__main__':
    app.run(port=3000, debug=True)
    
    
