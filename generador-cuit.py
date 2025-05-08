import random

def calcular_digito_verificador(cuit_base):
    multiplicadores = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    suma = sum(int(d) * m for d, m in zip(cuit_base, multiplicadores))
    resto = suma % 11
    if resto == 0:
        return '0'
    elif resto == 1:
        return '9'
    else:
        return str(11 - resto)

def generar_cuit(persona_humana=True):
    if persona_humana:
        prefijos = ['20', '23', '24', '27']
    else:
        prefijos = ['30', '33', '34']
    prefijo = random.choice(prefijos)
    dni = f"{random.randint(10000000, 49999999):08d}"
    cuit_base = prefijo + dni
    verificador = calcular_digito_verificador(cuit_base)
    return f"{prefijo}-{dni}-{verificador}"

def main():
    print("Generador de CUITs (Enter para generar uno nuevo o Ctrl+C para salir)")
    try:
        while True:
            input() # enter
            cuit = generar_cuit(persona_humana=True)
            print(f"CUIT generado: {cuit}")
    except KeyboardInterrupt:
        print("\nbye")

if __name__ == "__main__":
    main()
