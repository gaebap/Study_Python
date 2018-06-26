class Contact:
    def __init__(self,name,phone,email,addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.add = addr
    def print_info(self):
        print("name: ",self.name)
        print("phone number: ",self.phone)
        print("E-mail: ",self.email)
        print("Address: ",self.add)

def set_contact():
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name,phone,email,addr)
    return contact

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list,name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def store_contact(contact_list):
    File = open("contact_db.txt","wt")
    for contact in contact_list:
        File.write(contact.name + '\n')
        File.write(contact.phone + '\n')
        File.write(contact.email + '\n')
        File.write(contact.add + '\n')
    File.close()

def load_contact(contact_list):

    try:
        File = open("contact_db.txt","rt")

    except FileNotFoundError as e:
        print(str(e))
    except (ZeroDivisionError, OverflowError, FloatingPointError):
        print('에러 발생')
    else:
        lines = File.readlines()
        num = len(lines) / 4
        num = int(num)

        for i in range(num):
            name = lines[4*i].rstrip('\n')
            phone = lines[4 * i+1].rstrip('\n')
            email = lines[4 * i+2].rstrip('\n')
            addr = lines[4 * i+3].rstrip('\n')
            contract = Contact(name,phone,email,addr)
            contract.print_info()
            contact_list.append(contract)
        File.close()
    finally:
        print('return : load_contact')
# raise  TypeError #강제로 예외처리 발생


def run():
    # set_contact()
    contact_list = []

    load_contact(contact_list)

    while True:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
            # print(contact_list)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("삭제할 이름: ")
            delete_contact(contact_list,name)
        elif menu == 4:
            store_contact(contact_list)
            break

if __name__ == "__main__":
    run()