class Bank:

    def __init__(self, 
                 name: str = "банк", 
                 clients: int = 0, 
                 loans: int = 0,
                 country: str = "Україна",
                 rating: int = 0):
        self.__name = name
        self.__clients = clients
        self.__loans = loans
        self.rating = 5
        
        self.country = country
        self.rating = rating

    def get_name(self):
        return self.__name

    def get_clients(self):
            return self.__clients

    def get_loans(self):
            return self.__loans

    def __str__(self):
          return f"Банк {self.__name} має {self.__clients} клієнтів та видав {self.__loans} кредитів. \nКраїна - {self.country}\nРейтинг - {self.rating}"

    def __repr__(self):
          return f"Bank(name={self.__name!r}, clients={self.__clients!r}, loans={self.__loans!r}, country={self.country!r}, rating={self.rating!r})"

    def __del__(self):
          print(f"деструктор банку: {self.__name}")


def main():
    banks = [Bank(), Bank("ПриватБанк", 100500, 228, "Україна", 4), Bank("АБанк", 100500, 100, "Україна", -1)]

    for bank in banks:
        print('\n')
        print(bank)
        print(repr(bank))
    
    print('\n')


if __name__ == "__main__":
    main()