def Server():

    from flask import Flask, render_template
    from ModSer import ModLogSer
    import time
    import os
    from ModSer import OsID
    
    if OsID.determiner_os() == "Linux":
        Term_clear = ("clear")
    if OsID.determiner_os() == "Windows":
        Term_clear = ("cls")

    #Init

    Version = ("Version 3.")

    print("Bienvenue sur le serveur de Baptiste")

    print(Version)

    input("Appuyez sur sur entrée pour continuer")

    os.system(Term_clear)

    time.sleep(2)

    print("Veuillez patienter SVP...")

    time.sleep(2)

    print("Transfert de la demande au service LoginService...") 

    time.sleep(2)

    input("Appuyez sur entrée pour vous connecter.")

    ModLogSer.LoginService()

    print("Validation en cours")
    time.sleep(5)

    os.system(Term_clear)

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
            print("Server Status : -- Server Maintenance --")
            TemplatePagePrincipale = ("indexBugged.html")
        if Bugged == ("Non"):
            TemplatePagePrincipale = ("index.html")
        Status = ("Ready for Boot")
        time.sleep(2)
        print("Server status : " + Status)
        input("Appuyez sur entrée pour lancer le serveur.")
        os.system(Term_clear)
        print("")
        Status = ("ON")
        time.sleep(2)
        print("Server status : " + Status)
        app = Flask(__name__)
        app.run()

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

        if __name__ == '__main__':
            app.run(debug=True, host='192.168.1.22')
    else:
        Status = ("OFF")
        exit("Attention ! Serveur en opération Shutdown. Veuillez patienter...")
