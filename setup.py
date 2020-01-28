from subprocess import run


def main():

    print("Have you enabled passwordless sudo yet. (this script requires sudo)")

    answer = input("[y]es [n]o")

    if answer == 'n':
        print("exiting")
        return 0

    if answer == 'y':
        installer()

    print("unknown input exiting...")
    return 1


def installer():
    with open("packages.txt", "r") as file:
        run([])
        #//TODO//

if __name__ == "__main__":
   main() 