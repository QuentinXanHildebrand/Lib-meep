def main():

    f= open("meep.txt", "w")

    f.write("Mep mepp meep")
        
    f.close()

    f = open("meep.txt", "r")
    
    lines = f.read()
    
    print(lines)
    
    f.close()
#______________________________________________________________________________________________________________________________ 

new_list = [23, 'meepy']

new_dictionary = {'a':'mep', 'b':'meepy'}

f_name = "meep.py"

main()