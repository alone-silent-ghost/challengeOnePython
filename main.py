# main.py
import menu


def main():
    while True:
        option = menu.show_menu()
        if option == 1:
            menu.add_experiment()
        elif option == 2:
            menu.view_experiments()
        elif option == 3:
            menu.analyze_experiment()
        elif option == 4:
            menu.generate_report()
        elif option == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    main()
