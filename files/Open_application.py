import os

with open("apps location list.txt" , "r") as file:
    List = str(file.read()).split(">>")
try:
    app_dic = {}
    for i in range(len(List)):
        if i % 2 == 0:
            app_dic[str(List[i])] = str(List[i + 1])
except:
    pass

def open_func():
    print("""
you can change path of exe file of  applaications to be able to open them
entet \"add.path\" to add a new application and its path
enter \"change.path\" to change the path
enter \"apps\" to see entered apps with their paths
enter \"open\" to open an application
NOTE:After adding or changing sth. here you need to restart open section""")

    def add_path():
        print("enter \"stop\" to stop adding path")
        while True:
            app_list = open("apps location list.txt", "a")
            app_name = str(input("enter the name of the application : "))
            if app_name == "stop":
                break
            new_path = str(input("enter the path of the application : "))
            if new_path == "stop" or app_name == "stop":
                break
            else:
                app_list.write(app_name)
                app_list.write(">>")
                app_list.write(new_path)
                app_list.write(">>")
                app_list.close()

    def change_path():
        for i in range(len(List)):
            print(List[i])
        target = str(input("which app do you want to change : "))
        if target in List:
            i = List.index(target)
            List[i+1] = str(input("enter new path : "))
            print("Done!")
        with open("apps location list.txt" , "w") as file:
            pass
        with open("apps location list.txt" , "a") as file:
            
            for detail in List:
                file.write("%s>>" %(detail))
        print("here is the new list of apps and their paths:")
        for i in range(len(List)):
            print(List[i])

    def apps_name():
        name_list = list(app_dic.keys())
        for i in range(len(name_list)):
            print(name_list[i])

    def apps_path():
        name_list = list(app_dic.values())
        for i in range(len(name_list)):
            print(name_list[i])

    def apps():
        for i in range(len(List)):
            print(List[i])

    def open_app():
        name = str(input("name of app : "))
        try:
            os.startfile(app_dic[name])
        except KeyError:
            print("""no such app name found in path list
you can change path of .exe file of  applaications to be able to open them
entet \"add.path\" to add a new application and its path
enter \"change.path\" to change the path
enter \"apps\" to see entered apps with their paths""")
        except FileNotFoundError:
            print("""wrong path for this application
you can change path of .exe file of  applaications to be able to open them
entet \"add.path\" to add a new application and its path
enter \"change.path\" to change the path
enter \"apps\" to see entered apps with their paths""")


    while True:
        open_com = str(input("<open section>enter a command : "))

        if open_com == "exit.open":
            break
        if open_com == "change.path":
            change_path()
        if open_com == "add.path":
            add_path()
        if open_com == "apps.name":
            apps_name()
        if open_com == "apps.path":
            apps_path()
        if open_com == "apps":
            apps()
        if open_com == "open":
            open_app()