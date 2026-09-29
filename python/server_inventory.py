#!/usr/bin/env python3
import subprocess

def executar(titulo,comando):
    print("\n============================================== ")
    print(titulo)
    print("\n============================================== ")

    resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True
            )
    if resultado.returncode == 0:
        print(resultado.stdout)
    else:
        print("Err:")
        print(resultado.stderr)

executar("HOSTNAME", ["hostnamectl"])
executar("ENDEREÇOS DE REDE", ["ip","addr"])
executar("USO DE DISCO", ["df","-h"])
executar("MEMORIA RAM", ["free","-h"])


            
