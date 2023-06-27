def Server():

    from flask import Flask, render_template
    from ModSer import ModLogSer
    import time
    import os

    #Init

    Version = ("Version 2.")

    print("Bienvenue sur le serveur de Baptiste")

    print(Version)

    input("Appuyez sur entrée pour continuer")

    os.system("cls")

    time.sleep(2)

    print("Veuillez patienter SVP...")

    time.sleep(2)

    input("Appuyez sur entrée pour vous connecter.")

    ModLogSer.LoginService()

    print("Validation en cours")
    time.sleep(5)

    os.system("cls")

    Status = ("OFF")
    time.sleep(2)
    print("Server status : " + Status)

    print("Interface Administrateur")
    print("Voulez vous vraiment démarrer le serveur ? ")
    OnOff = input("Oui/Non : ")
    if OnOff == ("Oui"):
        Status = ("Loading...")
        time.sleep(2)
        print("Server status : " + Status)
        Bugged = input("Voulez vous mettre le serveur en maintenance ? Oui/Non : ")
        if Bugged == ("Oui"):
            TemplatePagePrincipale = ("indexBugged.html")
        if Bugged == ("Non"):
            TemplatePagePrincipale = ("index.html")
        Status = ("Ready for Boot")
        time.sleep(2)
        print("Server status : " + Status)
        input("Appuyez sur entrée pour lancer le serveur.")
        os.system("cls")
        print("")
        Status = ("ON")
        time.sleep(2)
        print("Server status : " + Status)
        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template(TemplatePagePrincipale)

        @app.route('/Login_Service')
        def Login_Service():
            return render_template('index_Login_Service.html')
    
        @app.route('/APropos')
        def APropos():
            return render_template('indexAPropos.html')

        @app.route('/hello/<name>')
        def hello(name):
            return render_template('Hello_Name.html', name=name)
    
        @app.route('/upload', methods=['GET', 'POST'])
        def upload_file():
            if request.method == 'POST':
                f = request.files['the_file']
                f.save('I:Python\webapp\ModLogSer.py')

        if __name__ == '__main__':
           app.run(debug=False, host='192.168.1.22')
    else:
        Status = ("OFF")
        exit("Attention ! Serveur en opération Shutdown. Veuillez patienter...")